import System.Environment
import qualified Data.ByteString as S

main = do
    (fileName1:fileName2:_) <- getArgs
    copyFile fileName1 fileName2

copyFile :: FilePath -> FilePath -> IO ()
copyFile source dest = do
    contents <- S.readFile source
    S.writeFile dest contents


