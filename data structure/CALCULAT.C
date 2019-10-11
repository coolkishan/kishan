#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
void main()
{
int a,b,res;
char choice;
clrscr();
printf("Enter '+' for addition ,\n '-' for subtraction ,\n '*' for  multiplication ,\n '/' for division\n");
scanf("%c",&choice);
printf("Enter the oprand a and b\n");
scanf("%d %d",&a,&b);
switch(choice)
{
case '+':res=a+b;break;
case '-':res=a-b;break;
case '*':res=a*b;break;
case '/':
	if(b==0)
	{
	printf("Divided by zero error\n");
	getch();
	exit (0);
	}
	else
	{
	res=a/b;
	}
	break;

default:printf("Invalid Choice\n");
	break;
}
printf("The result=%d",res);
getch();
}
