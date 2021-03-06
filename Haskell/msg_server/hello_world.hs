module Main where
import System.ZMQ4.Monadic
import Control.Monad (formM_)
import Data.ByteString.Char8 (pack, unpack)

main :: IO ()
main = 
    runZMQ $ do
      liftIO $ putStrLn "connecting to hello world server"
      reqSocket <- socket Req
      connect reqSocket "tcp://localhost:5555"
      forM_ [1..10] $ \i -> do
        liftIO $ putStrLn $ unwords ["Sending request", show i]
        send reqSocket [] (pack "Hello")
        reply <- receive reqSocket
        liftIO $ putStrLn $ unwords ["Received Reply", unpack reply]
