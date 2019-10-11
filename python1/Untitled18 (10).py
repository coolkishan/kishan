{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number 564765476467\n",
      "Number 564765476467 is not prime\n"
     ]
    }
   ],
   "source": [
    "#prime or not\n",
    "n=int(input(\"Enter the number \"))\n",
    "if n>1:\n",
    "    for i in range(2,n):\n",
    "        if (n%i)==0:\n",
    "            print(\"Number\",n,\"is not prime\")\n",
    "            break\n",
    "    else:\n",
    "        print(\"Number\",n,\"is prime\")\n",
    "else:\n",
    "       print(\"Number\",n,\"is not prime\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list=[]\n",
    "a=int(input(\"Enter the lower point \"))\n",
    "b=int(input(\"Enter the upper point\"))\n",
    "for i in range(a,b):\n",
    "    def prime():\n",
    "        n=i\n",
    "        if n>1:\n",
    "            for i in range(2,n):\n",
    "                if (n%i)==0:\n",
    "                    return -1\n",
    "                    break\n",
    "            else:\n",
    "                return 1\n",
    "        else:\n",
    "            return -1\n",
    "    firta=prime()    \n",
    "    if firta==1:\n",
    "        list=list.append[i]\n",
    "    else:\n",
    "        continue\n",
    "maxi=max.list\n",
    "print(maxi)"
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
