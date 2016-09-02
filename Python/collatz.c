#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[])
{
	unsigned long current_number, start, end;
	int temp, highest_chain_number, highest_chain, current_chain; highest_chain = 0;
	if (argc == 3) {
		start = atoi(argv[1]);
		end = atoi(argv[2]) + 1;
	} else if (argc==2) {
		start = atoi(argv[1]);
		end = start + 1;
	} else {
		printf("Atleast one argument expected");
		exit(0);
	}

	for(current_number = start; current_number <= end; current_number++) {
		temp = current_number;
		current_chain = 1;
		while(current_number != 1) {
			if(current_number % 2 == 0) {
				if ((current_number!= 0) & ((current_number && (current_number -1))
							== 0)) {
					current_chain += log(current_number)/log(2);
					break;
				} else {
					current_number /= 2;
					++current_chain;
				}
			} else {
				current_number = 3*current_number + 1;
				++current_chain;
				}
		}
		if(current_chain > highest_chain) {
			highest_chain = current_chain;
			highest_chain_number = temp;
			}
		current_number = temp;
	}
	printf("%d %d %d\n", start, end, highest_chain);
}
