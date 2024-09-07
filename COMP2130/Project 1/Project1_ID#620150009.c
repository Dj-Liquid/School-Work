//Daunte Robertson ID 620150009

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
	char kbinput[25];
	FILE *fptr;
	
	fptr=fopen("keylogfile.txt","w");
	printf("\nC:\\Users\\user\\Documents\\Test Code\\2130\\Project 1>");
	gets(kbinput);
	while(1)
	{
		if(strlen(kbinput)==1 && kbinput[0]==126)
		{
			fclose(fptr);
			exit(0);
		}
		system(kbinput);
		fprintf(fptr,"%s\n",kbinput);
		printf("\nC:\\Users\\user\\Documents\\Test Code\\2130\\Project 1>");
		gets(kbinput);
	}
}