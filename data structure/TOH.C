#include<stdio.h>
#include<conio.h>
void tower(int n,char src,char temp,char des)
{
if(n==1)
{
printf("Move disc = %d from %c to %c\n",n,src,des);
return ;
}
tower(n-1,src,des,temp);
printf("Move disc = %d from %c to %c\n",n,src,des);
tower(n-1,temp,src,des);
}
void main()
{
int n;
//char 'S','T','D';
clrscr();
printf("Enter the no. disc:\n");
scanf("%d",&n);
printf("Steps to solve tower of Hanoi:\n");
tower(n,'S','T','D');
getch();
}




