-- Hello Readers, Apologies for the mess this code is.
-- It's one of my attempts at learning xmonad via biting off more than i can swallow.
-- i.e: Combination of copy,paste from a couple of template config files.
-- No missing functions/imports though. i was careful of that.

{-# LANGUAGE TypeSynonymInstances, MultiParamTypeClasses, FlexibleContexts #-}
-- http://haskell.org/haskellwiki/index.php?title=Xmonad/Config_archive/eschulte_xmonad.hs
-- Configuration for running xmonad as the window manager over XFCE
-- see http://xmonad.org/xmonad-docs/xmonad-contrib/XMonad-Doc-Extending.html


import XMonad

import XMonad.Hooks.ManageDocks       -- manage docks and panels
import qualified Data.Map as M        -- used to add key bindings


import XMonad.Util.EZConfig
import qualified XMonad.StackSet as S
import XMonad.Actions.CycleWS
import XMonad.Config.Gnome

import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.ManageDocks

--import XMonad.Layout.Combo
--import XMonad.Layout.Grid
--import XMonad.Layout.LayoutModifier
--import XMonad.Layout.Named
--import XMonad.Layout.NoBorders
--import XMonad.Layout.PerWorkspace
--import XMonad.Layout.Reflect
--import XMonad.Layout.TwoPane
-- import XMonad.Layout.WindowNavigation
-- import XMonad.Util.WindowProperties

import Control.Monad
import Data.Ratio

--Borrowed from the problematic config file
-- defaults on which we build
-- use e.g. defaultConfig or gnomeConfig
myBaseConfig = gnomeConfig

-- display
-- replace the bright red border with a more stylish colour
myBorderWidth = 2
myNormalBorderColor = "#202030"
myFocusedBorderColor = "#A0A0D0"

-- workspaces
myWorkspaces = ["web", "editor", "terms"] ++ (miscs 1) ++ ["fullscreen", "im"]
    where miscs = map (("misc" ++) . show) . (flip take) [1..]
isFullscreen = (== "fullscreen")

-- modified version of XMonad.Layout.IM --

-- | Data type for LayoutModifier which converts given layout to IM-layout
-- (with dedicated space for the roster and original layout for chat windows)
data AddRosters a = AddRosters Rational [Property] deriving (Read, Show)

instance LayoutModifier AddRosters Window where
  modifyLayout (AddRosters ratio props) = applyIMs ratio props
  modifierDescription _                = "IMs"

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
--    rosters         = (ClassName "Pidgin")
    rosters         = [skypeRoster, pidginRoster]
    pidginRoster    = And (ClassName "Pidgin") (Role "buddy_list")
    skypeRoster     = (ClassName "Skype") `And` (Not (Title "Options")) `And` (Not (Role "Chats")) `And` (Not (Role "CallWindowForm"))

-- Mod4 is the Super / Windows key
myModMask = mod4Mask
altMask = mod1Mask

-- better keybindings for dvorak
myKeys conf = M.fromList $
    [ ((myModMask              , xK_Return), spawn $ XMonad.terminal conf)
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

myManageHook =  composeAll
                -- per-window options, use `xprop' to learn window names and classes
                [ className =? "MPlayer"        --> doFloat
                , className =? "Gimp"           --> doFloat
                , title     =? "EPresent"       --> doFloat
                ]

--myKeys conf@(XConfig {XMonad.modMask = modm}) =
--    [ ((modm, xK_b     ), sendMessage ToggleStruts) ] -- Mod-b: toggle XFCE panel
--newKeys x  = M.union (keys defaultConfig x) (M.fromList (myKeys x))

main = xmonad $ myBaseConfig
       { modMask = mod4Mask   -- use the super key for xmonad commands
       , workspaces = myWorkspaces
       , manageHook = manageDocks <+> myManageHook
--       , keys = newKeys
       , layoutHook = noBorders $ avoidStruts $ layoutHook defaultConfig
       , keys = myKeys
       }


-- | Modifier which converts given layout to IMs-layout (with dedicated
-- space for rosters and original layout for chat windows)
withIMs :: LayoutClass l a => Rational -> [Property] -> l a -> ModifiedLayout AddRosters l a
withIMs ratio props = ModifiedLayout $ AddRosters ratio props

-- | IM layout modifier applied to the Grid layout
gridIMs :: Rational -> [Property] -> ModifiedLayout AddRosters Grid a
gridIMs ratio props = withIMs ratio props Grid

hasAnyProperty :: [Property] -> Window -> X Bool
hasAnyProperty [] _ = return False
hasAnyProperty (p:ps) w = do
    b <- hasProperty p w
    if b then return True else hasAnyProperty ps w

-- | Internal function for placing the rosters specified by
-- the properties and running original layout for all chat windows
applyIMs :: (LayoutClass l Window) =>
               Rational
            -> [Property]
            -> S.Workspace WorkspaceId (l Window) Window
            -> Rectangle
            -> X ([(Window, Rectangle)], Maybe (l Window))

applyIMs ratio props wksp rect = do
    let stack = S.stack wksp
    let ws = S.integrate' $ stack
    rosters <- filterM (hasAnyProperty props) ws
    let n = fromIntegral $ length rosters
    let (rostersRect, chatsRect) = splitHorizontallyBy (n * ratio) rect
    let rosterRects = splitHorizontally n rostersRect
    let filteredStack = stack >>= S.filter (`notElem` rosters)
    (a,b) <- runLayout (wksp {S.stack = filteredStack}) chatsRect
    return (zip rosters rosterRects ++ a, b)
