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
		break;
	}
}