#include<stdio.h>
#include<conio.h>
void main()
{
int n,cr,pr,m;
char utype;
float bill;
clrscr();
printf("\n***********ELECTRICITY----BILL**************\n");
printf("Enter 'D'for Domestic User\n      'N' for Non Domestic User\n");
scanf("%c",&utype);
printf("Enter the metre no. :\n");
scanf("%d",&m);
printf("Enter the curent reading:\n");
scanf("%d",&cr);
printf("Enter the previous reading:\n");
scanf("%d",&pr);
n=cr-pr;
if(utype=='d'|| utype=='D')
 {
if(n>0 && n<=200)
bill=n*0.5;
else if(n>200 && n<=400)
bill= 100 + n*0.65;
else if(n>400 && n<=600)
bill=230+ n*0.8;
else if(n>600)
bill=390+n*1;
else
printf("INVALID UNITS\n");
 }

else if(utype=='N'|| utype=='n')
 {
if(n>0 && n<=100)
bill=n*0.5;
else if(n>100 && n<=200)
bill= 50 + n*0.60;
else if(n>200 && n<=300)
bill=100+ n*0.70;
else if(n>300)
bill=200+n*1;
else
printf("INVALID UNITS\n");
 }

else
 {
printf("INVALID USER TYPE\n");
getch();
exit(0);
 }

if(bill>0)
{
printf("The metre no. =%d\n",m);
printf("The no. of unit consumed =%d\n",n);
printf("The amount of bill=%f\n",bill);
}
getch();
}


