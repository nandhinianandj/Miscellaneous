all: $(patsubst %.hs, %, $(wildcard *.hs))

%: %.hs
	    ghc $^
		    grep -xq "$@" .gitignore || echo $@ >> .gitignore
