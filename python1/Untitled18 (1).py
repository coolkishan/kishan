{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_prime(n):\n",
    "    if n == 0 or n == 1:\n",
    "        return False\n",
    "    for i in range(2,n):\n",
    "        if n % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "n = int(input(\"Enter the no.\\n\"))\n",
    "tex = is_prime(n)\n",
    "if tex == True:\n",
    "    print(n,\"is prime\")\n",
    "else:\n",
    "    print(n,\"is not prime\")"
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
