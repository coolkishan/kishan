//Stack and its operation
//while using codeblocks avoid using exit(0)
#include<stdio.h>
#include<conio.h>
//#include<process.h>
#define STACK_SIZE 3
int top,s[10],item;
void push()
{
    top = top +1;
    s[top]=item;
}

int pop()
{
    int item_deleted;
    item_deleted=s[top--];
    return item_deleted;
}

void display()
{
    int i;
    for(i=0;i<=top;i++)
    {
        printf("%d ",s[i]);
    }
    printf("\n");

}
 int main()
 {
     int choice,top=-1;
     //clrscr;
     for(;;)
     {
         printf("1:PUSH\t2:POP\t3:DISPLAY\t4:EXIT\n");
         printf("Enter your choice\n");
         scanf("%d",&choice);
         switch(choice)
         {
             case 1:if(top == STACK_SIZE - 1)
                    {
                        printf("Stack is overflow\n");
                        return 0;
                    }
                    printf("Enter the item\n");
                    scanf("%d",&item);
                    push();
                    break;
             case 2:if(top == -1)
                        {
                            printf("Stack is empty\n");
                            break;
                        }
                    else
                            item = pop();
                            printf("Item deleted = %d\n",item);
                    break;
             case 3:if(top == -1)
                    {
                        printf("Stack is empty\n");
                        break;
                    }
                    display();
                    break;
            default:return 0;

         }

     }

 }
