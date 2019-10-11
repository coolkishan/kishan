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
      "Enter the upper limit 1\n",
      "Enter the lower limit 10\n"
     ]
    }
   ],
   "source": [
    "def prime_v1(i):\n",
    "    if i==0 or i==1:\n",
    "       return False\n",
    "    for d in range(2,i):\n",
    "        if i % d == 0:\n",
    "            return False\n",
    "    else:\n",
    "        return \n",
    "x=[]\n",
    "a=int(input(\"Enter the upper limit \"))\n",
    "b=int(input(\"Enter the lower limit \"))\n",
    "for j in range(a,b):\n",
    "    tex=prime_v1(j)\n",
    "    if tex == True:\n",
    "        print(j,\"TRUE\")\n",
    "        #x.append(j)\n",
    "    else:\n",
    "        continue\n",
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
