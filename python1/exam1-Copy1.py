{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "number = int(input(\"Enter any number: \"))\n",
    "if number > 1:\n",
    "    for i in range(2,number):\n",
    "        if(number%i)==0:\n",
    "            print(number,\"is not a prime number\")\n",
    "            break\n",
    "    else:\n",
    "            print(number,\"is a prime number\")\n",
    "else:\n",
    "    print(number,\"is not a prime number\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "number =int(input(\"Enter any number: \"))\n",
    "if number > 1:\n",
    "    for i in range(2,number):\n",
    "        if(number%i)==0:\n",
    "            print(number,\"is not a prime number\")\n",
    "            break\n",
    "    else:\n",
    "            print(number,\"is a prime number\")\n",
    "else:\n",
    "    print(number,\"is not a prime number\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "n=int(input(\"Enter value\"))\n",
    "k=0\n",
    "for i in range(2,(n+2)/2,1):\n",
    "    if (a%i==0):\n",
    "        k=k+1 break\n",
    "if(k==0):\n",
    "    print(\"No. is prime\")\n",
    "else:\n",
    "    print(\"No. is not prime\")\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "m = int(input(\"Enter first positive number:\"))\n",
    "n = int(input(\"Enter second positive number\"))\n",
    "if m==0 and n==0:\n",
    "    print(\"Invalid Input\")\n",
    "if m==0:\n",
    "    print(f\"GCD is {n}\")\n",
    "if n==0:\n",
    "    print(f\"GCD is {m}\")\n",
    "while m!=n:\n",
    "    if m>n:\n",
    "        m=m-n\n",
    "    if n>m:\n",
    "        n=n-m\n",
    "    print(f\"GCD of two number is {m}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 4\n",
    "b = 5\n",
    "print(\"Before swapping\")\n",
    "print(\"a =\",a)\n",
    "print(\"b =\",b)\n",
    "a,b=b,a\n",
    "print(\"After Swapping\")\n",
    "print(\"a=\",a)\n",
    "print(\"b=\",b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number5\n",
      "The fibonacci series upto 5 are \n",
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "x1 = 0\n",
    "x2 = 1\n",
    "n =int(input(\"Enter a number\"))\n",
    "print(\"The fibonacci series upto\",n,\"are \")\n",
    "print(x1)\n",
    "print(x2)\n",
    "for i in range(n-2):\n",
    "    x3=x1+x2\n",
    "    x1=x2\n",
    "    x2=x3\n",
    "    print(x3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter 1 no:5\n",
      "Enter 2 no:4\n",
      "sum is =  9\n",
      "diff is =  1\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def sum(x,y):\n",
    "    sum=x+y\n",
    "    print(\"sum is = \",sum)\n",
    "    return sum\n",
    "def diff(x,y):\n",
    "    diff = x-y\n",
    "    print(\"diff is = \",diff)\n",
    "    return diff\n",
    "x = int(input(\"Enter 1 no:\"))\n",
    "y = int(input(\"Enter 2 no:\"))\n",
    "sum(x,y)\n",
    "diff(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter values n= 5\n",
      "Enter elements to list\n",
      "Enter k value:12\n",
      "Enter k value:13\n",
      "Enter k value:14\n",
      "Enter k value:15\n",
      "Enter k value:16\n",
      "Sum of  [12, 13, 14, 15, 16] is  70\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter values n= \"))\n",
    "sum = 0\n",
    "list = []\n",
    "print(\"Enter elements to list\")\n",
    "for i in range(0,n,1):\n",
    "    k = int(input(\"Enter k value:\"))\n",
    "    list.append(k)\n",
    "    sum=sum+k\n",
    "print(\"Sum of \",list,\"is \", sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "number = int(input(\"Enter any number: \"))\n",
    "if number > 1:\n",
    "    for i in range(2,number):\n",
    "        if(number%i)==0:\n",
    "            print(number,\"is not a prime number\")\n",
    "            break\n",
    "    else:\n",
    "            print(number,\"is a prime number\")\n",
    "else:\n",
    "    print(number,\"is not a prime number\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
