
module Main (
             main
            ) where

import Data.LinearProgram
import Control.Monad.LPMonad
import Data.LinearProgram.GLPK
import Control.Monad.State
import qualified Data.Map as Map

loadPattern = Map.fromList [ ("night",5),("morning",25),("evenings",100) ]

-- on-demand instances cost/hour
onDemandHourlyCost = 0.64

-- reserved instances cost

reservationFixedCosts = [("light", 552.0),("medium",1280.0),("heavy",1560.0)]
reservationVariableCosts = [("light",0.312),("medium",0.192),("heavy",0.128)]
reservationTypes = map (\(x,y) -> x) reservationFixedCosts

dailyCost :: Map.Map [Char] Double -> LinFunc [Char] Double
dailyCost loadPattern = let
    periods = Map.keys loadPattern
    
    --cost of reserving an instance
    reservationFixedCostsObj = [ ( cost/365.0, "reservation_" ++ kind)
                                | (kind, cost) <- reservationFixedCosts ] 
    -- cost of *running* the reserved instance. 
    reservationVariableCostsObj = [ (cost*8, "reserved_" ++ kind ++ "_" ++ period)
                                  | (kind, cost) <- reservationVariableCosts,
                                  period <- periods ]
    -- cost of running on-demand instances
    onDemandVariableCostsObj = [ (onDemandHourlyCost*8, "onDemand_" ++ p) |p <- periods ]

    in
    linCombination (reservationFixedCostsObj ++ reservationVariableCostsObj ++ onDemandVariableCostsObj)

-- Constraints.. 
--
-- on meeting the load at any instant the combination of all
-- services should satisfy load demand.

    capacityConstraints loadPattern = [ (linCombination (
                                            [ (1.0, "onDemand_" ++ period) ]
                                          ++[(1.0, "reserved_" ++ k ++ "_" ++ period) | k <- reservationTypes]
                                          ),
                                          load)
                                            | (period,load) <- (Map.assocs loadPattern)]


-- reservationConstraints

reservationConstraints loadPattern = [ linCombination [ (1.0, "reservation_" ++ k),
                                      (-1.0, "reserved_" ++ k ++ "_" ++ p) ],0.0  |
                                      p <- (Map.keys loadPattern),
                                      k <- reservationTypes ]


-- Positive integer variables constraint

allVariables loadPatten = ["onDemand_" ++ p | p <- periods] ++
                          ["reserved_" ++ k ++ "_" ++ p | p <- periods, k <- reservationTypes] ++
                          ["reservation_" ++ k | k <- reservationTypes]

            where periods = Map.keys loadPattern



lp :: Map.Map [Char] Double -> LP String Double
lp loadPattern = execLPM $ do 
                         -- Tell glpk we are minimizing no maximizing 
                          setDirection Min
                          -- pass the objective function/variable to minimize
                          setObjective (dailyCost loadPattern)

                          --First and second set of constraints
                          mapM (\(func, val) -> func `geqTo` val) (reservationConstraints loadPattern)
                          mapM (\(func, val) -> func `geqTo` val) (capacityConstraints loadPattern)
                          -- Positive values constraint
                          mapM (\var -> varGeq var 0.0) (allVariables loadPattern)
                          -- Integer values constraint. aws instances can't be
                          -- fractional
                          mapM (\var -> setVarKind var IntVar) (allVariables loadPattern)



--Finally, printing results

printLPSolution loadPattern = do
  x <- glpSolveVars mipDefaults (lp loadPattern)
  putStrLN (show (allVariables loadPattern))
  case x of (Success, Just (obj,vars)) -> do
                          putStrLn "Success!"
                          putStrLn ("Cost: " ++ (show obj))
                          putStrLN ("Variables: " ++ (show vars))
            (failure, result) -> putStrLn ("Failure: " ++ (show failure))





main :: IO ()
main = do 
  printLPSolution (Map.fromList [ ("night", 12.2), ("morning",25.1), ("evening",53.5) ])
                           
