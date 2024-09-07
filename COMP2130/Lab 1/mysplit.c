#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#define MAXINPUT 10

void main(int argc,char *arbv[])
{

	char name[50],first[25],last[25];
	int length,i,pos;
	int j=0;
	printf("What is your name? ");
	scanf("%s",name);
	length = strlen (name);
	for (i=0;i<length; i++)
    {
        if (isupper(name[i]))
			pos=i;	  
    }
	for (i = 0; i < length + 1; i++) 
	{
		if (i < pos)
			first[i]= name[i];
		else
		{
			last[j] = name[i];
			j++;
		}
		
    }

	printf("Your first name is %s",first);
	printf(" and your last name is %s\n",last);
	
	
	
}
