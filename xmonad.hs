import XMonad
import qualified XMonad.StackSet as S
import qualified Data.Map        as M
import Control.Monad
import System.IO
import System.IO.Unsafe
import Data.List
import Data.Ratio ((%))

import Xmonad.Config.Gnome

-- Actions
import XMonad.Actions.CycleWS
import XMonad.Actions.Plane
import XMonad.Actions.TopicSpace
import XMonad.Actions.SpawnOn
import XMonad.Actions.OnScreen
import XMonad.Actions.SwapWorkspaces
import XMonad.Actions.FindEmptyWorkspace
 
-- Hooks
import XMonad.Hooks.ManageHelpers
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.ManageDocks
import XMonad.Hooks.SetWMName
import XMonad.Hooks.FadeInactive
import XMonad.Hooks.UrgencyHook hiding (Never)
 
-- Layouts
import XMonad.Layout.PerWorkspace
import XMonad.Layout.IM
import XMonad.Layout.Grid
import XMonad.Layout.TwoPane
import XMonad.Layout.NoBorders
import XMonad.Layout.Reflect
import XMonad.Layout.Named
import XMonad.Layout.LayoutModifier

 
-- Prompts
import XMonad.Prompt
import XMonad.Prompt.Input
import XMonad.Prompt.Workspace
import XMonad.Prompt.Shell
import XMonad.Prompt.XMonad
import XMonad.Prompt.RunOrRaise
import XMonad.Prompt.AppendFile
 
-- Util
import XMonad.Util.Run(spawnPipe)
import XMonad.Util.EZConfig(additionalKeysP, additionalKeys)


-- | Data type for LayoutModifier which converts given layout to IM-layout
-- (with dedicated space for the roster and original layout for chat windows)
data AddRosters a = AddRosters Rational [Property] deriving (Read, Show) 


myBaseConfig = gnomeConfig
--
-- main
--
 
main = do
    checkTopicConfig myTopics myTopicConfig
    dzen <- spawnPipe myStatusBar
    other <- spawnPipe myLeft
    other <- spawnPipe myRight
    xmonad $ withUrgencyHook NoUrgencyHook defaultConfig
	{ manageHook         = manageHook defaultConfig <+> myManageHook 
	, layoutHook         = mylayoutHook
	, startupHook        = setWMName "LG3D"
	, terminal           = myTerminal
	, modMask            = myModMask
	, borderWidth        = myBorderWidth
	, focusFollowsMouse  = True
	, normalBorderColor  = myBorder
	, focusedBorderColor = myFocusedBorder
	, workspaces         = myTopics 
	, logHook            = myLogHook >> (dynamicLogWithPP $ myDzenPP dzen)
	} `additionalKeysP` myKeys
 
-- End Main


-- | Modifier which converts given layout to IMs-layout (with dedicated
-- space for rosters and original layout for chat windows)
withIMs :: LayoutClass l a => Rational -> [Property] -> l a -> ModifiedLayout AddRosters l a
withIMs ratio props = ModifiedLayout $ AddRosters ratio props 

-- | IM layout modifier applied to the Grid layout
gridIMs :: Rational -> [Property] -> ModifiedLayout AddRosters Grid a
gridIMs ratio props = withIMs ratio props Grid

-- Simple configuration
myBorderWidth = 2
myBrowser = "firefox"
myTerminal = "gnome-terminal --window-with-profile=xmonad"
myShell = "zsh"
myIconDir = "/home/anand/.dzen/dzenIcons/"
myStatusBar = "dzen2 -x '0' -y '0' -h '20' -w '330' -ta 'l' -bg '" ++ myDBGColor ++ "' -fn '" ++ myFont ++ "'"
myLeft = "/home/anand/.dzen/left.zsh | dzen2 -xs 1 -x '330' -y '0' -h '20' -w '1110' -ta 'r' -bg '" ++ myDBGColor ++ "' -fg '" ++ myDFGColor ++ "' -fn '" ++ myFont ++ "'"
myRight = "/home/anand/.dzen/right.zsh | dzen2 -xs 2 -y '0' -h '20' -ta 'r' -bg '" ++ myDBGColor ++ "' -fg '" ++ myDFGColor ++ "' -fn '" ++ myFont ++ "'"
myFont = "DroidSans-Bold.ttf" 

-- workspaces
myWorkspaces = ["web", "editor", "terms"] ++ (miscs 5) ++ ["fullscreen", "im"]
    where miscs = map (("misc" ++) . show) . (flip take) [1..]
isFullscreen = (== "fullscreen")
-- layouts
basicLayout = Tall nmaster delta ratio where
    nmaster = 1
    delta   = 3/100
    ratio   = 1/2
tallLayout = named "tall" $ avoidStruts $ basicLayout
wideLayout = named "wide" $ avoidStruts $ Mirror basicLayout
singleLayout = named "single" $ avoidStruts $ noBorders Full
fullscreenLayout = named "fullscreen" $ noBorders Full
imLayout = avoidStruts $ reflectHoriz $ withIMs ratio rosters chatLayout where
    chatLayout      = Grid
    ratio           = 1%6
    rosters         = [skypeRoster, pidginRoster]
    pidginRoster    = And (ClassName "Pidgin") (Role "buddy_list")
    skypeRoster     = (ClassName "Skype") `And` (Not (Title "Options")) `And` (Not (Role "Chats")) `And` (Not (Role "CallWindowForm"))
--                                       
myLayoutHook = fullscreen $ im $ normal where
    normal     = tallLayout ||| wideLayout ||| singleLayout
    fullscreen = onWorkspace "fullscreen" fullscreenLayout
    im         = onWorkspace "im" imLayout
--                                                    
-- special treatment for specific windows:
-- put the Pidgin and Skype windows in the im workspace
myManageHook = imManageHooks <+> manageHook myBaseConfig
imManageHooks = composeAll [isIM --> moveToIM] where
    isIM     = foldr1 (<||>) [isPidgin, isSkype]
    isPidgin = className =? "Pidgin"
    isSkype  = className =? "Skype"
    moveToIM = doF $ S.shift "im"
--                                                                     
-- Mod4 is the Super / Windows key
myModMask = mod4Mask
altMask = mod1Mask
 
-- Layout Hook
mylayoutHook = smartBorders $ avoidStruts $ lessBorders (Combine Difference Screen OnlyFloat) (Mirror tiled ||| tiled ||| fullscreenLayout)
    where
	fullscreenLayout = smartBorders Full
	tiled = Tall nmaster delta ratio
	nmaster = 1
	delta = 3 / 100
	ratio = 11 / 20
 
-- Log Hook
myLogHook = fadeInactiveLogHook fadeAmount
    where fadeAmount = 0.90
 
-- XP Config
myXPConfig :: XPConfig
myXPConfig = defaultXPConfig { font = myFont
		         , height = 22
			     , bgColor = myDBGColor }
 
myDFGColor = "#b2b27f" -- Dzen
myDBGColor = "#2f3436"
myFFGColor = "#4c5e52" -- Focused
myFBGColor = "#ffbe2c"
myVFGColor = "#4c5e52" -- Visible
myVBGColor = "#2f3436"
myUFGColor = "#4c5e52" -- Urgent
myUBGColor = "#ffeca1"
myIFGColor = "#ffeca1" -- Icon
myIBGColor = myDBGColor
mySColor   = myDFGColor -- Seperator
myBorder   = "#4c5e52"
myFocusedBorder = "#4c5e52"
 
-- Pretty Printing
myDzenPP h = defaultPP
     {  ppCurrent         = dzenColor myFFGColor myFBGColor . wrap ("^fg(" ++ myIFGColor ++ ")^i(" ++ myIconDir ++ "/eye_l.xbm)" ++ "^fg(" ++ myFFGColor ++ ")") "" 
      , ppVisible         = dzenColor myVFGColor myVBGColor . wrap "" ("^fg(" ++ myIFGColor ++ ")^i(" ++ myIconDir ++ "/eye_r.xbm)")
      , ppHidden          = dzenColor myDFGColor myDBGColor . wrap ("^i(" ++ myIconDir ++ "/dzen_bitmaps/has_win.xbm)") ""
      , ppHiddenNoWindows = dzenColor myDFGColor myDBGColor . wrap ("^i(" ++ myIconDir ++ "/dzen_bitmaps/has_win_nv.xbm)") ""
      , ppUrgent          = dzenColor myUFGColor myUBGColor . wrap ("^i(" ++ myIconDir ++ "/info_03.xbm)") "" . dzenStrip
      , ppTitle           = dzenColor myDFGColor myDBGColor . shorten 0
      , ppLayout          = dzenColor myDFGColor myDBGColor .
                            (\x -> case x of
                            "Mirror Tall" -> "^fg(" ++ myIFGColor ++ ")^i(" ++ myIconDir ++ "/dzen_bitmaps/mtall.xbm)"
                            "Tall"	  -> "^fg(" ++ myIFGColor ++ ")^i(" ++ myIconDir ++ "/dzen_bitmaps/tall.xbm)"
                            "Full"	  -> "^fg(" ++ myIFGColor ++ ")^i(" ++ myIconDir ++ "/dzen_bitmaps/full.xbm)"
                            "Grid"	  -> "^fg(" ++ myIFGColor ++ ")^i(" ++ myIconDir ++ "/dzen_bitmaps/grid.xbm)"
                            "TwoPane"	  -> "^fg(" ++ myIFGColor ++ ")^i(" ++ myIconDir ++ "/dzen_bitmaps/two_pane.xbm)"
                            _ -> x
                            )
      , ppSep             = " "
      , ppOutput          = hPutStrLn h }



-- better Key bindings for dvorak
myKeys conf = M.fromList $
    [ ((myModMask              ,xK_Return), spawn $ Xmonad.terminal conf)
    , ((myModMask              , xK_r     ), gnomeRun)
    , ((myModMask              , xK_c     ), kill)
    , ((myModMask              , xK_space ), sendMessage NextLayout)
    , ((myModMask              , xK_n     ), refresh)
    , ((myModMask              , xK_m     ), windows S.swapMaster)
    , ((altMask                , xK_Tab   ), windows S.focusDown)
    , ((altMask .|. shiftMask  , xK_Tab   ), windows S.focusUp)
    , ((myModMask              , xK_Down  ), windows S.swapDown)
    , ((myModMask              , xK_Up    ), windows S.swapUp)
    , ((myModMask              , xK_Left  ), sendMessage Shrink)
    , ((myModMask              , xK_Right ), sendMessage Expand)
    , ((myModMask              , xK_t     ), withFocused $ windows . S.sink)
    , ((myModMask              , xK_w     ), sendMessage (IncMasterN 1))
    , ((myModMask              , xK_v     ), sendMessage (IncMasterN (-1)))
    , ((myModMask              , xK_q     ), broadcastMessage ReleaseResources >> restart "xmonad" True)
    , ((myModMask .|. shiftMask, xK_q     ), spawn "gnome-session-save --kill")
    , ((altMask .|. controlMask, xK_Left  ), prevWS)
    , ((altMask .|. controlMask, xK_Right ), nextWS)
    ] ++
    -- Alt+F1..F10 switches to workspace
    -- (Alt is in a nicer location for the thumb than the Windows key,
    -- and 1..9 keys are already in use by Firefox, irssi, ...)
    [ ((altMask, k), windows $ S.greedyView i)
        | (i, k) <- zip myWorkspaces workspaceKeys
    ] ++
    -- mod+F1..F10 moves window to workspace and switches to that workspace
    [ ((myModMask, k), (windows $ S.shift i) >> (windows $ S.greedyView i))
        | (i, k) <- zip myWorkspaces workspaceKeys
    ]
    where workspaceKeys = [xK_F1 .. xK_F10]
 
-- Key Bindings 
--myKeys = [ ("M-f",	spawn myBrowser)  	
         -- xmms2
--         , ("M-S-'",	spawn "nyxmms2 prev")
--         , ("M-S-.",	spawn "nyxmms2 next")
--         , ("M-S-p",	spawn "nyxmms2 toggle")
	 -- ALSA Volume
--         , ("M-C-e",	spawn "amixer set Master 2%-")
--         , ("M-C-u",	spawn "amixer set Master 2%+")
         -- CycleWS
--         , ("M-s",	nextWS)
--         , ("M-n",	prevWS)
	 -- Swap Workspaces
--	     , ("M-S-s",	swapTo Next)
--	     , ("M-S-n",	swapTo Prev)
--         , ((myAltMask, xK_space), viewEmptyWorkspace)
         -- Prompt
--         , ("M-C-p",	runOrRaisePrompt defaultXPConfig)
--         , ("M-C-.",	shellPrompt defaultXPConfig)
--         , ("M-C-j",	jumpPrompt)
	 -- Toggle Struts
--	     , ("M-S-s",	sendMessage ToggleStruts)
--	 -- Topics
--	     , ("M-a",	currentTopicAction myTopicConfig)
---	     , ("M-g",	promptedGoto)
--	     , ("M-c",	promptedGotoOtherScreen)
--	     , ("M-S-g",	promptedShift)
         -- Restart
--         , ("M-q",	spawn myRestart)
--	 ]
--        ++	
         -- Change Xinerama bindings
--         [ ("M-"++key, screenWorkspace sc >>= flip whenJust (windows . f))
--             | (key, sc) <- zip ["w", "v", "z"] [0..]
--             , (f, m) <- [(S.view, 0)]] 
 
spawnShell = currentTopicDir myTopicConfig >>= spawnShellIn
 
spawnShellIn :: Dir -> X ()
spawnShellIn dir = spawn $ myTerminal ++ " -title urxvt -e sh -c 'cd ''" ++ dir ++ "'' && " ++ myShell ++ "'"
 
goto :: Topic -> X ()
goto = switchTopic myTopicConfig
 
promptedGoto :: X ()
promptedGoto = workspacePrompt myXPConfig goto
 
promptedGotoOtherScreen :: X ()
promptedGotoOtherScreen =
	workspacePrompt myXPConfig $ \ws -> do
		nextScreen
		goto ws
 
promptedShift :: X ()
promptedShift = workspacePrompt myXPConfig $ windows . S.shift
 
jumpPrompt :: X ()
jumpPrompt = inputPrompt defaultXPConfig ("Jump") ?+ spawnJump
 
spawnJump ::  String -> X ()
spawnJump s = spawn ("nyxmms2 jump artist:" ++ s) 
 
-- Helper functions
--
-- Avoid changing master on new window creation
avoidMaster :: S.StackSet i l a s sd -> S.StackSet i l a s sd
avoidMaster = S.modify' $ \c -> case c of
	S.Stack t [] (r:rs) -> S.Stack t [r] rs
	otherwise			-> c
 
-- Kill zombie dzens before normal xmonad restart
myRestart :: String
myRestart = "for pid in `pgrep dzen2`; do kill -9 $pid; done && xmonad --recompile && xmonad --restart"
 
-- TopicSpace things
myTopics :: [Topic]
myTopics =
  [   "web"
    , "mail"
    , "term"
    , "music"
    , "im"
    , "irc"
    , "dev"
    , "mon"
    ]
 
myTopicConfig :: TopicConfig
myTopicConfig = TopicConfig
	{ topicDirs = M.fromList $
	[ ("music", "~/music")
	]
	, defaultTopicAction = const $ spawnShell
	, defaultTopic = "web"
	, maxTopicHistory = 10
	, topicActions = M.fromList $
		[ ("web",	spawn myBrowser)
		, ("mail",	spawn "urxvtc -e sup")
		, ("term",	spawnShell )
		, ("im",	spawn "pidgin")
		, ("music",	spawn "urxvtc -e nyxmms2")
		, ("irc",	spawn "urxvtc -e irssi")
		, ("dev",	spawnShell )
		, ("mon",	spawn "urxvtc -e htop")
		]
	}
