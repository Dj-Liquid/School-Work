#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

//Write a program that looks at all the command line arguments and reports if any of the
//arguments are the same (i.e., they match exactly). The program should print out the matching
//argument and the positions it occupies in the list of arguments.

void main(int argc, char* argv[])
{
	int i,j;
	for (i = 1; i <= argc; i++){
		for (j = i + 1; j <= argc; j++){
			if (!strcmp(argv[i], argv[j])){
				printf("Matching Arguments %s \n", argv[i]);
				printf("At position %d, %d\n", i, j);
				exit(0);
			}
		}
	}
} 