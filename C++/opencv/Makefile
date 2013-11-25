PROGRAMS_SRC=$(wildcard *.c)
TARGETS=$(patsubst %.c, %,$(PROGRAMS_SRC))
CPPFLAGS=I/usr/local/include/opencv2 -lml -lcvaux -lhighgui -lcv -lcxcore

all:
	$(foreach var,$(PROGRAMS_SRC),g++ $(var) -o $(patsubst %.c, %,$(var)) -$(CPPFLAGS); )


