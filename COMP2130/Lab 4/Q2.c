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