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