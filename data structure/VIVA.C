#include<stdio.h>
#include<conio.h>
void main()
{
int i,j;
clrscr();
for(i=1;i<=3;i++)
{
 for(j=1;j<=3;j++)
   {
   if(i%2==1&&j%2==0)
   printf(" ");
   else
   printf("%d",i);
   }
   printf("\n");
}
getch();
}