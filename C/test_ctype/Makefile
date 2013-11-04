all:hello.dll hello hello_dll

clean:
	rm *.dll hello.so hello_so hello

hello: hello.h hello.c hello_main.c
	gcc hello.c hello_main.c -o hello # --save-temps

hello.dll:hello.h hello.c
	gcc -shared hello.c -o hello.dll -fPIC #--save-temps -fPIC

hello_dll: hello.h hello.c
	gcc hello_main.c -L. hello.dll -o hello_main


