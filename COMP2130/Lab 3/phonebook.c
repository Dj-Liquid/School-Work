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
	
	
	locate(name,books);
	
	
	
}