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