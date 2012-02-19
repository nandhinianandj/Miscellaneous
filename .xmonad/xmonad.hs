-- Hello Readers, Apologies for the mess this code is.
{-# LANGUAGE TypeSynonymInstances, MultiParamTypeClasses, FlexibleContexts #-}
-- http://haskell.org/haskellwiki/index.php?title=Xmonad/Config_archive/eschulte_xmonad.hs
-- Configuration for running xmonad as the window manager over XFCE
-- see http://xmonad.org/xmonad-docs/xmonad-contrib/XMonad-Doc-Extending.html


import XMonad

import qualified Data.Map as M        -- used to add key bindings


import XMonad.Util.EZConfig
import XMonad.Util.Run(spawnPipe)

import qualified XMonad.StackSet as S
import XMonad.Actions.CycleWS
import XMonad.Config.Gnome

import XMonad.Hooks.DynamicLog
import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.ManageDocks

import Control.Monad
import Data.Ratio

import System.IO

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

-- layouts
basicLayout = Tall nmaster delta ratio where
    nmaster = 1
    delta   = 3/100
    ratio   = 1/2

-- Mod4 is the Super / Windows key
myModMask = mod4Mask
altMask = mod1Mask

-- better keybindings for dvorak
myKeys conf = M.fromList $
    [ ((myModMask              , xK_r), spawn $ XMonad.terminal conf)
    , ((myModMask              , xK_Return ), gnomeRun)
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
    , ((myModMask .|. shiftMask, xK_q     ), spawn "gnome-session-quit")
    , ((altMask .|. controlMask, xK_Left  ), prevWS)
    , ((altMask .|. controlMask, xK_Right ), nextWS)
    ] ++
   -- Print screen, lock 
    [ ((mod4Mask .|. shiftMask, xK_l), spawn "xscreensaver-command -lock")
        , ((controlMask, xK_Print), spawn "sleep 0.2; scrot -s")
        , ((0, xK_Print), spawn "scrot")
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

main = do
    xmproc <- spawnPipe "xmobar"
    xmonad $ myBaseConfig
       { modMask = mod4Mask   -- use the super key for xmonad commands
       , workspaces = myWorkspaces
       , manageHook = manageDocks <+> myManageHook
       , layoutHook = avoidStruts $ layoutHook defaultConfig
       , logHook = dynamicLogWithPP xmobarPP
                    { ppOutput = hPutStrLn xmproc
                      , ppTitle = xmobarColor "green" "" . shorten 50
                    }
       , keys = myKeys
       }



