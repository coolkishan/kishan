{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any number: 10\n",
      "10 is not a prime number\n"
     ]
    }
   ],
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
