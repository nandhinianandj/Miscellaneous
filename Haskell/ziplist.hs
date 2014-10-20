-- data ZipList a = ZipList [a]
-- data ZipList a = ZipList { getZipList :: [a] }

newtype ZipList a = ZipList { getZipList :: [a] }
data Profession = Fighter | Archer | Accountant
data Race = Human | Elf | Orc | Goblin
data PlayerCharacter = PlayerCharacter Race Profession

newtype CharList = CharList { getCharList :: [Char] } deriving (Eq, Show)
