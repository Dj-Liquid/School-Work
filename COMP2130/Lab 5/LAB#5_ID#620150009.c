//Daunte Robertson
//Question 1

/*Consider the code given below. Write a custom print function “cprintf()” that implements a buffer.
The function takes a single string as input and returns nothing. All bytes in the string are buffered until
the percent symbol (%) is encountered. Upon encountering that symbol, all contents of the buffer
should be flushed (printed to the stdout stream) and the buffer should be reset to empty. The percent
symbol should not be printed; it is only a trigger. The buffer only needs to be large enough for this
example, do not worry about overflow. The newline character should be printed but should not cause a
flush. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>

/* custom function cprintf() goes here */
void cprintf(char etext[])
{
	FILE *fpt;
	char otext[30],ntext[100],ctext[30],ntext2[100],stext[30];
	int count=0;
	
	strcpy(ntext,"");
	fpt=fopen("cprintf.txt","r");
	fscanf(fpt, "%s", ntext);
	while (fscanf(fpt, "%s", otext) == 1)
	{
		strcat(ntext," ");
		strcat(ntext,otext);
	}
	strcat(ntext," ");
	fclose(fpt);
	fpt=fopen("cprintf.txt","w");
	strcat(ntext,etext);
	fprintf(fpt,"%s",ntext);
	fclose(fpt);
	fpt=fopen("cprintf.txt","r");
	strcpy(ntext2,"");
	while (fscanf(fpt, "%s", ctext) == 1)
	{
		if(strstr(ctext,"%")==NULL)
		{	
			strcat(ntext2,ctext);
			strcat(ntext2," ");
		}
		else
		{
			for(int i=0;i<strlen(ctext);i++)
			{
				if((int)ctext[i]==37)
				{
					strncpy(stext, ctext,i);
					if(strlen(ctext)>1)
					{
						strcpy(stext,ctext);
						strtok(stext,"%");
					}
					strcat(ntext2,stext);
					printf("%s \n",&ntext2);
					strcpy(ntext2,"");
					strncpy(ctext, &ctext[i+1], strlen(ctext)-i+1);
					strcpy(stext,ctext);
					count=1;
					break;
				}
			}
		}
	}
	fclose(fpt);
	if (count==1)
	{
		fpt=fopen("cprintf.txt","w");
		strcat(stext," ");
		strcat(stext,ntext2);
		fprintf(fpt,"%s",stext);
		strcpy(stext,"");
		fclose(fpt);
	}
}

void main()
{
	
cprintf("Test\n"); 
Sleep(500);                      //the value 500 seemed to be about 1 second in my console
cprintf("Re%test\n");
Sleep(500);
cprintf("All done\n%");
}
// The text should appear in the order they were entered

//Question 2
/*The way I coded it could be a solution to the issue of the program ending with bytes still in the buffer,
by using a file as the buffer, even after the program is closed, for however long it is closed for, once it is restarted
it will start where it left off printing the leftover bytes first. */ 

