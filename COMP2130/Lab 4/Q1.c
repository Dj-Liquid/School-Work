//Q(1.) Write the contents for out.txt as produced by the following code. Give specific byte
//values. How many total bytes will the file contain at the end of execution?
#include <stdio.h>
void main()
{
	FILE *fpt;
	int x;
	fpt=fopen("out.txt","w");
	for (x=0; x<15; x+=2)
	fprintf(fpt,"%2d ",x);
	fclose(fpt);
}
	Including the ' ' printed, the total number of bytes the file
	contains is 1+4+1+1+4+1+1+4+1+1+4+1+1+4+1+1+4+1+4+1+4+1
	= 46 bytes
	
