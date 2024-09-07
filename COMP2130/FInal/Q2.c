//Daunte Robertson 620150009

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void create();
void display();
 
int yom;
char make[25],model[25];

struct node
{
        int stryom;
		char strmake[25];
		char strmodel[25];
        struct node *next;
};
struct node *start=NULL;

void makeVehicle()
{
	
	printf("Enter the year of manufacture of the vehicle: \n");
	scanf("%d",&yom);
	printf("Enter the make of the vehicle: \n");
	scanf("%s",make);
	printf("Enter the model of the vehicle: \n");
	scanf("%s",model);
}
	
	
	
void main()     
{
	create();
	display();
}

void create()
{
        struct node *temp,*ptr;
        temp=(struct node *)malloc(sizeof(struct node));
        if(temp==NULL)
        {
                printf("\nOut of Memory Space:\n");
                exit(0);
        }
		makeVehicle();
		temp->stryom=yom;
		strcpy(temp->strmake,make);
		strcpy(temp->strmodel,model);
        temp->next=NULL;
        if(start==NULL)
        {
                start=temp;
        }
        else
        {
                ptr=start;
                while(ptr->next!=NULL)
                {
                        ptr=ptr->next;
                }
                ptr->next=temp;
        }
}

void display()
{
	struct node *ptr;
	ptr=start;
	printf("The data has successfully entered the node\nYear of Manufacture: %d\nMake: %s\nModel: %s",ptr->stryom,ptr->strmake,ptr->strmodel);
}