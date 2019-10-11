{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number:\n",
      "45\n",
      "Sum of digits = 9\n"
     ]
    }
   ],
   "source": [
    "def sum(n):\n",
    "    s = 0\n",
    "    while (n != 0):\n",
    "        rem = n % 10\n",
    "        s = s + rem\n",
    "        n = n // 10\n",
    "    return s\n",
    "n = int(input(\"Enter the number:\\n\"))\n",
    "sum1 = sum(n)\n",
    "print(\"Sum of digits =\",sum1)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "8//4\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.0"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "8/4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number item in the list = 5\n",
      "Enter the list\n",
      "\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "List =  [5, 6, 7, 8, 9]\n",
      "Enter the key 3\n",
      "Failure,Search is not successful\n",
      "\n"
     ]
    }
   ],
   "source": [
    "def search(list,l,key):\n",
    "    for i in range(0,l):\n",
    "        if key == list[i]:\n",
    "            return i\n",
    "    else:\n",
    "        return -1\n",
    "list = []\n",
    "n = int(input(\"Enter the number item in the list = \"))\n",
    "print(\"Enter the list\\n\")\n",
    "for i in range(0,n):\n",
    "    x = int(input())\n",
    "    list.append(x)\n",
    "    \n",
    "l = len(list)\n",
    "print(\"List = \",list)\n",
    "key = int(input(\"Enter the key \"))\n",
    "result = search(list,l,key)\n",
    "if result == -1:\n",
    "    print(\"Failure,Search is not successful\\n\")\n",
    "else:\n",
    "    print(\"Success,Key is found at =\",result+1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your sentence \n",
      "My name is Khan.\n",
      "No. of word in sentence =  4\n"
     ]
    }
   ],
   "source": [
    "def getword(string,l):\n",
    "    c = 0 \n",
    "    for i in range(0,l): \n",
    "        if string[i] == \" \":\n",
    "            c = c + 1\n",
    "        else:\n",
    "            continue\n",
    "    return c\n",
    "string = str(input(\"Enter your sentence \\n\"))\n",
    "l = len(string)\n",
    "#result = getword(string,l)\n",
    "print(\"No. of word in sentence = \",getword(string,l)+1)\n"
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
      "Enter the words\n",
      "my,name,is,khan\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-252d5afb91c2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mstring\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Enter the words\\n\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[0ml\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstring\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m \u001b[0mnew_string\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mchange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstring\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Replaced words = \"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mnew_string\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-1-252d5afb91c2>\u001b[0m in \u001b[0;36mchange\u001b[1;34m(string, l)\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mstring\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\",\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m             \u001b[0mstring\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"-\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mstring\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mstring\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Enter the words\\n\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "def change(string,l):\n",
    "    for i in range(0,l):\n",
    "        if string[i] == \",\":\n",
    "            string[i] = \"-\"\n",
    "    return string\n",
    "list = [ram,shyam,gita,babita]\n",
    "#string = str(input(\"Enter the words\\n\"))\n",
    "l = len(list)\n",
    "new_string = change(string,l)\n",
    "print(\"Replaced words = \",new_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'a' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-bd182cf7b6c3>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mlist\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mg\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msort\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'a' is not defined"
     ]
    }
   ],
   "source": [
    "list = [a,s,g,d]\n",
    "list.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "List =  None\n"
     ]
    }
   ],
   "source": [
    "list = ['a','s','g','d']\n",
    "print(\"List = \",list.sort())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
