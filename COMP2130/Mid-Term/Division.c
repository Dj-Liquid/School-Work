/*
Your program is a simple one. It must prompt a user to enter an integer numerator and then, prompt the user to enter an 
integer denominator. It must then call a function called division. The function declaration for division is provided below:
int division (int numerator, int denominator, int *dividend, int *remainder)

Note that it is the addresses of the memory locations that will be used to store the results of the division, dividend and 
remainder, are passed as arguments to the function. Include code that will inform the user that if the denominator is zero 
that division by zero is not defined. You are not required to consider any other possible errors. Examples of what the 
program's prompts and outputs should look like are provided below:

Execution with zero denominator...
Enter the numerator: 5
Enter the denominator: 0
Division by zero not defined
Execution with non-zero denominator...
Enter the numerator: 6
Enter the denominator: 5
6/5 = 1 with 1 remainder

Your program therefore should have only two functions, main and division, and the function division is called from within main.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>


int division (int numerator, int denominator, int *dividend, int *remainder)
{
	if(denominator==0)
		return 0;
	else
	{
		*dividend=numerator/denominator;
		*remainder=numerator%denominator;
	}
	return 1;
}

void main()
{
	int num,denum;
	int divi,rem;
	printf("Enter the numerator: ");
	scanf("%d",&num);
	printf("Enter the denominator: ");
	scanf("%d",&denum);
	if (division(num,denum,&divi,&rem)!=0)
	{
		printf("%d/%d = %d with %d remainder\n",num,denum,divi,rem);
	}
	else
	{
		printf("Division by zero not defined\n");
	}
}


