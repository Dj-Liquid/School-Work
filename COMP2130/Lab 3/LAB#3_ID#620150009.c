//Daunte Robertson
//Question 1
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


//Question 2
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

//Write a complete program that prompts the user for an input string, sorts its characters,
//and prints out the sorted output. Assume the string contains no spaces and is at most 30
//characters long. Sort the characters according to byte values, regardless of the symbols
//those values represent, from smallest to largest. The output should be one contiguous string,
//printed on one line. Example: “Input: apple” should print “aelpp”.


void main ()
{
	char word[30],final[30];
	int aski[30],length,temp;
	printf("Enter the word you would like sorted: \n");
	scanf("%s",word);
	length = strlen (word);
	for (int i=0;i<length;i++)
		aski[i]=word[i];
	for (int x = 0; x < length; x++) 
	{     
        for (int y = x+1; y < length; y++) 
		{     
           if(aski[x] > aski[y]) 
		   {    
               temp = aski[x];    
               aski[x] = aski[y];    
               aski[y] = temp; 
		   }
		}
	}
	for (int i=0;i<length;i++)
		word[i]=aski[i];
	printf("The word is now: %s", word);
	
}


//Question 3
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

//Write a program that looks at all the command line arguments and reports if any of the
//arguments are the same (i.e., they match exactly). The program should print out the matching
//argument and the positions it occupies in the list of arguments.

void main(int argc, char* argv[])
{
	int i,j;
	for (i = 1; i <= argc; i++){
		for (j = i + 1; j <= argc; j++){
			if (!strcmp(argv[i], argv[j])){
				printf("Matching Arguments %s \n", argv[i]);
				printf("At position %d, %d\n", i, j);
				exit(0);
			}
		}
	}
}


//Question 4
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

//A phone book typically lists the name, address, and telephone number of everyone
//living in an area. Write code defining a structure template that could be used to store this
//data. Assume that a name and address will be no more than 30 characters each, and that a
//telephone number has exactly seven digits. Write code that will enter records in your
//structure. Write a function that will accept a pointer to a phone book structure and present all
//the records. Write a function that accepts a name and locate the record matching that name.

struct phonebook
{
	char name[30],address[30];
	int number;
};

void records(struct phonebook *pbp)
{
	printf("Name: %s \n",pbp->name);
	printf("Address: %s \n",pbp->address);
	printf("Telephone Number: %d \n",pbp->number);
}

void locate(char name[30],struct phonebook *books[100])
{
	for(int i=0;i<100;i++)
	{
		if (name==books[i]->name)
			printf("The record for %s is \n",name);
			records(books[i]);
			break;
	}
}

void main ()
{
	struct phonebook pbook,*pbp,*books[100];
	int num;
	char name[30];
	
	printf("\nEnter your name: ");
	scanf("%s",&pbook.name);
	printf("\nEnter your address: ");
	scanf("%s",&pbook.address);
	printf("\nEnter your telephone number: ");
	scanf("%d",&num);
	pbook.number=num;
	pbp=&pbook;
	records(pbp);
	
	
	locate(name,books);  //We were'nt told to write code to store phonebook records
						 // so i just wrote the code for the function and function call
						 // with the assumption that that code exists.
	
	
}


//Question 5
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

//Use the following code to describe a rectangle. Assume the rectangle sides are parallel
//to the x and y axes (no rotation), and that the corners of the rectangle are located properly
//according to their compass designations in the structure.

struct point 
{
	int x,y;
};
struct rect 
{
	struct point ne,se,sw,nw;
};

//Write a function called RectArea() that returns an integer value equal to the
//area of the given rectangle. The rectangle should be passed in as an argument.

int RectArea(struct rect shape)
{
	int x1,x2,y1,y2,length,width,area;
	x1= shape.ne.x;
	x2= shape.nw.x;
	y1= shape.ne.y;
	y2= shape.se.y;
	length = x1-x2;
	width  = y1-y2; 
	area = length*width;
	return area;
}


void main ()
{
	struct rect shape;
	struct point tr,br,bl,tl;
	int x1,x2,y1,y2,area;
	printf("Enter the x coordinate for the north east point: \n");
	scanf("%d",&x1);
	printf("Enter the y coordinate for the north east point: \n");
	scanf("%d",&y1);
	printf("Enter the x coordinate for the south west point: \n");
	scanf("%d",&x2);
	printf("Enter the y coordinate for the south west point: \n");
	scanf("%d",&y2);
	tr.x=x1;
	tr.y=y1;
	br.x=x1;
	br.y=y2;
	bl.x=x2;
	bl.y=y2;
	tl.x=x2;
	tl.y=y1;
	shape.ne=tr;
	shape.se=br;
	shape.sw=bl;
	shape.nw=tl;
	area=RectArea(shape);
	printf("The area of the rectangle is %d",area);
	
}