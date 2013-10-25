FLAGS=-Wall -g
CC=gcc
CFLAGS=--std=c99 -g -pedantic -Wall -lm
PROGRAMS_SRC=$(wildcard bin/*.c)
PROGRAMS=$(patsubst %.c,%,$(PROGRAMS_SRC))
OBJECTS=$(patsubst %.c,%.o,$(PROGRAMS_SRC))
TARGETS=$(patsubst %.c,%,$(PROGRAMS_SRC))

all: 
	echo $(OBJECTS)
	echo $(TARGETS)
	$(TARGET) $(SO_TARGET) tests $(PROGRAMS)


clean:
	  rm -rf $(OBJECTS) $(TESTS) $(PROGRAMS)

$(PROGRAMS): CFLAGS += $(TARGET)
test: 
	test_game
	./test_game

