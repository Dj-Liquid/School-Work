#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#define MAXINPUT 10

main(int argc,char *arbv[])
{
	char input[MAXINPUT] = "";
	int i,length,sum;
	printf("Enter a 1-10 digit number: ");
	scanf ("%s", input);
	length = strlen (input);
	sum=0;
	for (i=0;i<length; i++)
	{
		if (!isdigit(input[i]))
		{
			printf ("Entered input contains a non-number\n");
			exit(1);
		}
		else
		sum+=input[i];
	}
	printf("The sum of the digits in the number is %d",sum);
}