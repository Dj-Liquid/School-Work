//Daunte Robertson
//Question 1 

//Write the contents for out.txt as produced by the following code. Give specific byte
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
	
	
//Question 2	

//Q(2.) Consider the variable declaration below. Write code that opens a file for output and uses
//a single line of code to write out all of the declared variable(s).
#include <stdio.h>
struct inventory 
{
char name[30];
int count;
float price;
};// log[75];

void main()
{
	FILE *fpt;
	struct inventory item;
	printf("Name of the item: \n");
	scanf("%s",item.name);
	printf("Number of items in stock: \n");
	scanf("%d",&item.count);
	printf("Price of the item: \n");
	scanf("%f",&item.price);
	fpt=fopen("inventory.txt","w");
	fprintf(fpt,"Item name:%s         Amount of item:%d         Cost of item:$%.2f \n",item.name,item.count,item.price);
	fclose(fpt);
}	


//Question 3

//Q(3.) Write a program that reads a text file and reports the total count of words of each length.
//A word is defined as any contiguous set of alphanumeric characters, including symbols. For
//example, in the current sentence there are 10 words. The filename should be given at the
//command line as an argument. The file should be read one word at a time. A count should be
//kept for how many words have a given length. For example, the word “frog” is 4 bytes in
//length; the word “turtle” is 6 bytes in length. The program should report the total word counts
//of all lengths between 3 and 15 bytes. Words with lengths outside that range should not be counted.
#include <stdio.h>
#include <string.h>

void main()
{
	FILE *fpt;
	char text[50],file[20];
	char buffer[100];
	int length=0;
	int three=0;
	int four=0;
	int five=0;
	int six=0;
	int seven=0;
	int eight=0;
	int nine=0;
	int ten=0;
	int eleven=0;
	int twelve=0;
	int thirteen=0;
	int fourteen=0;
	int fifteen=0;
	printf("Enter the name of the file: ");
	scanf("%s",&file);
	fpt=fopen(file,"r");
	while (fscanf(fpt, "%s", buffer) == 1)
	{
		//fscanf(fpt,"%s",text);
		length=strlen(buffer);
		if (length==3)
			three++;
		else if (length==4)
			four++;
		else if (length==5)
			five++;
		else if (length==6)
			six++;
		else if (length==7)
			seven++;
		else if (length==8)
			eight++;
		else if (length==9)
			nine++;
		else if (length==10)
			ten++;
		else if (length==11)
			eleven++;
		else if (length==12)
			twelve++;
		else if (length==13)
			thirteen++;
		else if (length==14)
			fourteen++;
		else if (length==15)
			fifteen++;
	}	
	fclose(fpt);
	if (three>0)
		printf("The number of 3 byte long words is %d\n",three);
	if (four>0)
		printf("The number of 4 byte long words is %d\n",four);
	if (five>0)
		printf("The number of 5 byte long words is %d\n",five);
	if (six>0)
		printf("The number of 6 byte long words is %d\n",six);
	if (seven>0)
		printf("The number of 7 byte long words is %d\n",seven);
	if (eight>0)
		printf("The number of 8 byte long words is %d\n",eight);
	if (nine>0)
		printf("The number of 9 byte long words is %d\n",nine);
	if (ten>0)
		printf("The number of 10 byte long words is %d\n",ten);
	if (eleven>0)
		printf("The number of 11 byte long words is %d\n",eleven);
	if (twelve>0)
		printf("The number of 12 byte long words is %d\n",twelve);
	if (thirteen>0)
		printf("The number of 13 byte long words is %d\n",thirteen);
	if (fourteen>0)
		printf("The number of 14 byte long words is %d\n",fourteen);
	if (fifteen>0)
		printf("The number of 15 byte long words is %d\n",fifteen);

	
}

//Question 4

//Q(4.) Write a program that will display text on any terminal. The program should prompt the
//user for the name of the device file for the terminal on which to display output, as well the
//output to display. It should then perform the necessary I/O operations. This process should
//repeat until the user decides to exit the program
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

void main()
{
	FILE *fpt;
	char file[20],text[100],cont[5];
	while(true)
	{
		printf("Enter the name of the device file: ");
		scanf("%s",&file);
		printf("Enter the text to be displayed: ");
		scanf("%s",text);
		fpt=fopen(file,"w");
		fprintf(fpt,text);
		fclose(fpt);
		printf("Press n to exit the program or press anything else to continue\n");
		scanf("%s",cont);
		if(strcmp(cont,"n")==0 | strcmp(cont,"N")==0)
			exit(0);
	};
}