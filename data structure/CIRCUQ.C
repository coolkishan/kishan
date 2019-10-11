//CIRCULAR QUEUE FOR CODE BLOCKS
#include<process.h>
#include<stdio.h>
#include<conio.h>
#define Qsize 3
int front=0,rear=-1,count=0,item,q[3];
void insertQ()
{
  printf("Enter the item to be inserted\n");
  scanf("%d",&item);
  rear=(rear+1)%Qsize;
  q[rear]=item;
  count++;

}

int deleteQ()
{
    int item;
    if(count==0)return -1;
    item=q[front];
    front=(front+1)%Qsize;
    count--;
    return item;
}

void displayQ()
{
    int i,f;
    printf("Contents of the Queue are:\n");
    for(i=1,f=front;i<=count;i++)
    {
        printf("%d\t",q[f]);
        f=(f+1)%Qsize;
    }
    printf("\n");
}



int main()
{
    int choice;
    for(;;)
    {
        printf("1:INSERT\t2:DELETE\t3:DISPLAY\t4:EXIT\n");
        printf("Enter your choice\n");
        scanf("%d",&choice);
        switch(choice)
                {
                    case 1: if(count==Qsize)
                            {
                                printf("Queue Overflow\n");
                                break;
                            }
                    insertQ();
                   break;
            case 2:item=deleteQ();
                    if(item==-1)
                    {
                        printf("Queue is empty\n");
                        break;
                    }
                    printf("Item deleted = %d\n",item);
                    break;
            case 3: if(count==0)
                    {
                        printf("Queue is empty\n");
                        break;
                    }
                    displayQ();
                    break;
            default:return 0;
        }
    }
}


