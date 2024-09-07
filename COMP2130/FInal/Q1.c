//Daunte Robertson 620150009

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(int argc, char* argv[])
{
	FILE *fpt;
	char buffer[25];
	int count=0;
	
	if(argc!=3)
	{
		printf("Error - Program only takes two arguments\n");
		exit(0);
	}
	fpt=fopen(argv[2],"r");
	if (fpt==NULL)
	{
		printf("Error - File could not be opened\n");
		exit(0);
	}
	while (fscanf(fpt, "%s", buffer) == 1)
	{
		//fscanf(fpt,"%s",text);
		if (strcmp(argv[1],buffer)==0)
			count++;
	}	
	fclose(fpt);
	printf("The number of times %s has been found in %s was %d time(s)\n",argv[1],argv[2],count);
}