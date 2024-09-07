#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

//Consider the following variable declarations. Assume each variable stores the values in
//a matrix. Write code that multiplies the matrix a by the matrix b and stores the result in the
//matrix c.
//float a[2][3],b[3][2],c[2][2]; row a * col a

void main ()
{
	float a[2][3],b[3][2],c[2][2];
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<3;j++)
		{
		printf("2x3 Array[%d][%d]= ", i, j);
		scanf("%f",&a[i][j]);	
		}
	}
	for(int k=0;k<3;k++)
	{
		for(int l=0;l<2;l++)
		{
		printf("3x2 Array[%d][%d]= ", k, l);
		scanf("%f",&b[k][l]);	
		}
	}
	for(int m=0;m<2;m++)
	{
		for(int n=0;n<2;n++)
		{
			c[m][n]=a[m][0]*b[0][n] + a[m][1]*b[1][n] + a[m][2]*b[2][n];
		}
	}
	for(int o=0;o<2;o++)
	{
		for(int p=0;p<2;p++)
		{
			printf("%f\t",c[o][p]);
		}
		printf("\n");
	}
}