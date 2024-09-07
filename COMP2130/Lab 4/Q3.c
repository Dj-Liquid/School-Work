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