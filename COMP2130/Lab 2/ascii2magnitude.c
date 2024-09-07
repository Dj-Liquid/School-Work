#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

void main ()
{
	char input[3];
	int aski[3];	
	printf("Input a positive three digit number: \n");
	scanf("%s",input);
	for (int i=0;i<3;i++)
		aski[i]=input[i];
	printf("The ASCII values are: n[0] is %d",aski[0]);
	printf(", n[1] is %d",aski[1]);
	printf(", n[2] is %d\n",aski[2]);
	printf("The magnitude only number is %d",atoi(input));
}
