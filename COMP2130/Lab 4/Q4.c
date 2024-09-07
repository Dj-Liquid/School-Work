//Q(4.) Write a program that will display text on any terminal. The program should prompt the
//user for the name of the device file for the terminal on which to display output, as well the
//output to display. It should then perform the necessary I/O operations. This process should
//repeat until the user decides to exit the program
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

void main()
{
	FILE *fpt;
	char file[20],text[100],cont[5];
	while(true)
	{
		printf("Enter the name of the device file: ");
		scanf("%s",&file);
		printf("Enter the text to be displayed: ");
		scanf("%s",text);
		fpt=fopen(file,"w");
		fprintf(fpt,text);
		fclose(fpt);
		printf("Press n to exit the program or press anything else to continue\n");
		scanf("%s",cont);
		if(strcmp(cont,"n")==0 | strcmp(cont,"N")==0)
			exit(0);
	};
}