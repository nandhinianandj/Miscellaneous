{-# LANGUAGE
      OverloadedStrings
      , TypeFamilies
      , QuasiQuotes
      , TemplateHaskell
      , GADTs
      , FlexibleContexts
      , MultiParamTypeClasses 
 #-}
 
import Yesod
import Yesod.Auth
import Yesod.Form.Nic (YesodNic, nicHtmlField)
import Yesod.Auth.BrowserId (authBrowserId)
import Data.Text (Text)
import Network.HTTP.Conduit (Manager, newManager, def)
import Database.Persist.Sqlite
     ( ConnectionPool, SqlPersist, runSqlPool, runMigration
     , createSqlitePool
     )

import Data.Time (UTCTime, getCurrentTime)
import Control.Applicative ((<$>), (<*>), pure)

share [mkPersist sqlSettings, mkMigrate "migrateAll"] 
[persistLowerCase|

  User
     email Text
     UniqueUser email
  
  Entry
     title Text
     posted UTCTime
--     content Html   deriving
  
  Comment
     entry EntryId
     posted UTCTime
     user UserId
     name Text
     text Textarea 
  |]
  
data Blog = Blog
   { connPool :: ConnectionPool
   , httpManager :: Manager
   }

mkMessage "Blog" "../messages-blog" "en"


mkYesod "Blog" [parseRoutes|
/ RootR GET
/blog BlogR GET POST
/blog/#EntryId EntryR GET POST
/auth AuthR Auth getAuth
|]

instance Yesod Blog where

approot = ApprootStatic "http://localhost:3000"


isAuthorized BlogR True = do
        mauth <- maybeAuth
        case mauth of
            Nothing -> return AuthenticationRequired
            Just (Entity _ user)
               | isAdmin user -> return Authorized
               | otherwise    -> unauthorizedI 
MsgNotAnAdmin

isAuthorized (EntryR _) True = do
        mauth <- maybeAuth
        case mauth of
              Nothing -> return AuthenticationRequired
              Just _  -> return Authorized

isAuthorized _ _ = return Authorized

authRoute _ = Just (AuthR LoginR)

defaultLayout inside = do
mmsg <- getMessage


pc <- widgetToPageContent $ do
            toWidget [lucius|
body {
    width: 760px;
    margin: 1em auto;
    font-family: sans-serif;
}

textarea {
     width: 400px;
     height: 200px;
}

#message {
     color: #900;
}
|]
            inside

hamletToRepHtml [hamlet|
$doctype 5
<html>
    <head>
       <title>#{pageTitle pc}
       ^{pageHead pc}
    <body>
       $maybe msg <- mmsg
           <div #message>#{msg}
       ^{pageBody pc}
|]

--isAdmin :: User -> Bool
--isAdmin user = userEmail user == "michael@snoyman.com"

instance YesodPersist Blog where
   type YesodPersistBackend Blog = SqlPersist
   runDB f = do 
      master <- getYesod
      let pool = connPool master
      runSqlPool f pool

type Form x = Html -> MForm Blog Blog (FormResult x, Widget)


instance RenderMessage Blog FormMessage where
    renderMessage _ _ = defaultFormMessage

instance YesodNic Blog

instance YesodAuth Blog where
    type AuthId Blog = UserId
    loginDest _ = RootR
    logoutDest _ = RootR
    authHttpManager = httpManager


authPlugins _ = [authBrowserId]

getAuthId creds = do
        let email = credsIdent creds
            user = User email
        res <- runDB $ insertBy user
        return $ Just $ either entityKey id res



getRootR :: Handler RepHtml
getRootR = defaultLayout $ do
    setTitleI MsgHomepageTitle
    [whamlet|
<p>_{MsgWelcomeHomepage}
<p>
    <a href=@{BlogR}>_{MsgSeeArchive}
|]

entryForm :: Form Entry
entryForm = renderDivs $ Entry
    <$> areq textField (fieldSettingsLabel MsgNewEntryTitle) Nothing
    <*> aformM (liftIO getCurrentTime)
    <*> areq nicHtmlField (fieldSettingsLabel MsgNewEntryContent) Nothing



getBlogR :: Handler RepHtml
getBlogR = do
    muser <- maybeAuth
    entries <- runDB $ selectList [] [Desc EntryPosted]
    ((_, entryWidget), enctype) <- generateFormPost entryForm
    defaultLayout $ do
      setTitleI MsgBlogArchiveTitle
      [whamlet|
$if null entries
  <p>_{MsgNoEntries}
$else
  <ul>
      $forall Entity entryId entry <- entries
          <li>
            <a href=@{EntryR entryId}>#{entryTitle entry}


$maybe Entity _ user <- muser
    $if isAdmin user
        <form method=post enctype=#{enctype}>
            ^{entryWidget}
            <div>
                <input type=submit value=_{MsgNewEntry}>
$nothing
  <p>
     <a href=@{AuthR LoginR}>_{MsgLoginToPost}
|]


postBlogR :: Handler RepHtml
postBlogR = do
    ((res, entryWidget), enctype) <- runFormPost entryForm
    case res of
        FormSuccess entry -> do
             entryId <- runDB $ insert entry
             setMessageI $ MsgEntryCreated $ entryTitle entry
             redirect $ EntryR entryId
         _ -> defaultLayout $ do
             setTitleI MsgPleaseCorrectEntry
             [whamlet|
<form method=post enctype=#{enctype}>
    ^{entryWidget}
    <div>
        <input type=submit value=_{MsgNewEntry}>
|]

commentForm :: EntryId -> Form Comment
commentForm entryId = renderDivs $ Comment
    <$> pure entryId
    <*> aformM (liftIO getCurrentTime)
    <*> aformM requireAuthId
    <*> areq textField (fieldSettingsLabel MsgCommentName) Nothing
    <*> areq textareaField (fieldSettingsLabel MsgCommentText) Nothing


getEntryR :: EntryId -> Handler RepHtml
getEntryR entryId = do
    (entry, comments) <- runDB $ do
        entry <- get404 entryId
        comments <- selectList [CommentEntry ==. entryId] [Asc CommentPosted]
        return (entry, map entityVal comments)
    muser <- maybeAuth
    ((_, commentWidget), enctype) <-
        generateFormPost (commentForm entryId)
    defaultLayout $ do
        setTitleI $ MsgEntryTitle $ entryTitle entry
        [whamlet|
<h1>#{entryTitle entry}
<article>#{entryContent entry}
     <section .comments>
         <h1>_{MsgCommentsHeading}
         $if null comments
            <p>_{MsgNoComments}
         $else
            $forall Comment _entry posted _user name text <- comments
                <div .comment>
                    <span .by>#{name}
                    <span .at>#{show posted}
                    <div .content>#{text}
            <section>
              <h1>_{MsgAddCommentHeading}
              $maybe _ <- muser
                 <form method=post enctype=#{enctype}>
                     ^{commentWidget}
                     <div>
                        <input type=submit value=_{MsgAddCommentButton}>
              $nothing
                  <p>
                     <a href=@{AuthR LoginR}>_{MsgLoginToComment}
|]



postEntryR :: EntryId -> Handler RepHtml
postEntryR entryId = do
    ((res, commentWidget), enctype) <-
        runFormPost (commentForm entryId)
    case res of
        FormSuccess comment -> do
        _ <- runDB $ insert comment
        setMessageI MsgCommentAdded
        redirect $ EntryR entryId
    _ -> defaultLayout $ do
        setTitleI MsgPleaseCorrectComment
        [whamlet|
<form method=post enctype=#{enctype}>
   ^{commentWidget}
   <div>
       <input type=submit value=_{MsgAddCommentButton}>
|]

main :: IO ()
main = do
    pool <- createSqlitePool "blog.db3" 10 -- create a new pool
        -- perform any necessary migration
        runSqlPool (runMigration migrateAll) pool
        manager <- newManager def -- create a new HTTP manager
        warpDebug 3000 $ Blog pool manager -- start our server
