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
	
}