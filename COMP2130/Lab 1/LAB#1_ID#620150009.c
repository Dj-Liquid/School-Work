//Question 1

#include <stdio.h>
#include <math.h>

main(int argc,char *arbv[])
{
	int n,i;
	int d2,count;  //lab.cpp:8:9: error: expected unqualified-id before 'double'  
	double d1;	   //8 |         double d1;
				   // there was no semi-colon at the end of line 7
	
	while (1)
	{
		printf("Enter a number (0 to quit): ");
		scanf("%d",&n);
		if (n==0)
			break;
		count=0;
		for (i=0; i<n; i++)
		{
			d1=(double)n/(double)i;
			d2=n/i;
			if (fabs(d1-(double)d2) < 0.00001)
			count++;
		}
		if (count == 2)
			printf("%d is prime\n",n);
		else
			printf("%d is not prime\n",n);
	}
}


//Question 2
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define MAXINPUT 100

main(int argc,char *arbv[],char** argv)
{
	int n1,n2,n3,length,i,counter;
	char input[MAXINPUT] = "";
	while (1)
	{	

		printf("Enter a number: ");
		scanf ("%s", input);
		length = strlen (input);
		for (i=0;i<length; i++)
        if (!isdigit(input[i]))
        {
            printf ("Entered input is not a number\n");
            exit(1);
        }
		n1=atoi(input);
		printf("Enter another number: ");
		scanf ("%s", input);
		length = strlen (input);
		for (i=0;i<length; i++)
        if (!isdigit(input[i]))
        {
            printf ("Entered input is not a number\n");
            exit(1);
        }
		n2=atoi(input);
		if(n1==0|n2==0)
			printf ("Entered number cannot be 0\n");
		
		if(n1>n2)
		{
			n3=n1/n2;
			printf("The result of the division is %d\n",n3);
			if(argc==1)
				printf("\nNo Extra Command Line Argument Passed Other Than Program Name");
			if(argc>=2)
			{
				printf("\nNumber Of Arguments Passed: %d",argc);
				printf("\n----Following Are The Command Line Arguments Passed----");
				for(counter=0;counter<argc;counter++)
					printf("\nargv[%d]: %s",counter,argv[counter]);
			}
			break;
		}
		else
		printf("The first number must be larger than the second\n");
	}
}

//Question 3
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


//Question 4
//The output would be 9


//Question 5
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#define MAXINPUT 10

main(int argc,char *arbv[])
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





    
    
    