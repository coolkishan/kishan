/*#include<stdio.h>
#include<conio.h>
#define Qsize 5
int ch,item,r,f,q[10];
void insert_rear()
	{
	if(r==Qsize-1)
		{
		printf("Queue full\n");
		return;
		}
	}

void delete_front()
{
	if(j>r)
		{
		printf("Queue is Underflow\n");
		return;
		}
	printf("Element deleted is %d\n",q[f]);
	f++;
}



void display()
{
	int i;
	if(j>r)
		{
		printf("Queue is empty\n");
		return;
		}
	printf("Contents of the queue\n");
	for(i=f;i<=r;i++)
		{
		printf("%d\n",q[i]);
		}
}


void main()
{
f=0;
r=-1;
clrscr();
for(;;)
	{
	printf("Enter 1:INSERT  2:DELETE  3:DISPLAY 4:EXIT\n");
	scanf("%d",&choice);
	switch(choice)
		{
		case 1: printf("Enter the item\n");
			scanf("%d",&item);
			insert_rear(item,q,r);
			break;

		case 2: delete_front(q,&f,&r);
			break;

		case 3: display(q,f,r);
			break;
		default:exit(0);
		}
	}
} */


//queues
#include<stdio.h>
#include<conio.h>
#include<process.h>
#define qsize 3
int q[3],item,front=0,rear=-1;
void insertq()
{
	if(rear==qsize-1)
	{
		printf("Q is Full\n");
		return;
	}
	rear=rear+1;
	q[rear]=item;
}
int deleteq()
{
	int item_del;
	if(front>rear)
	{
		//printf("Q Empty\n");
		return -1;
	}
	item_del=q[front];
	front=front+1;
	return item_del;
}
void display()
{
	int i;
	if(front>rear)
	{
		printf("Q Empty\n");
		return;
	}
	printf("Queue Contents\n");
	for(i=front;i<=rear;i++)
	{
		printf("%d\n",q[i]);
	}
}
void main()
{
	int choice,item_del;
	clrscr();
	for(;;)
	{
		printf("Enter your choice\n 1.insert\t 2.delete\t 3.display\n");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:printf("Enter your item\n");
				scanf("%d",&item);
				insertq();
				break;
			case 2:item_del=deleteq();
				if(item_del==-1)
				{
				printf("Queue is Empty\n");
				break;
				}
				printf("your Deleted item is\n");
				printf("%d\n",item_del);
				break;
			case 3:display();
				break;
			default:exit(0);
				getch();
		}
	}
}






