{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Kishan\n"
     ]
    }
   ],
   "source": [
    "print('Hello Kishan')"
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
      "Enter the number 2\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"Enter the number \"))\n",
    "if n>1:\n",
    "    for i in range(2,n):\n",
    "        if n%i==0:\n",
    "            print(\"Number\",n,\"is not prime\")\n",
    "        else:\n",
    "            print(\"Number\",n,\"is prime\")\n",
    "else:\n",
    "       print(\"Number\",n,\"is not prime\")"
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
