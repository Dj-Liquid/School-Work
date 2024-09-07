#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

void main(int argc,char *arbv[])
{
	char input;
	char a;
	char b;
	
	printf("Enter a positive integer: ");
	scanf("%d",&input);
	a=input >> 1;
	b=input << 1;
	
	printf("%d \n",input);
	printf("%d \n",a);
	printf("%d \n",b);
	
	// shifting to the left is the same as multiplying the number by 2^n, n being the number of shifts.
	// shifting to the right is the same as dividing the number by 2^n, n being the number of shifts.
}