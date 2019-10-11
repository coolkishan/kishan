{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "t = list()\n",
    "for i in range(1,1):\n",
    "    t.append(i)\n",
    "print(t)\n",
    "print(max(t))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# =======  python program to find list of the prime no. from the given boundary and also print the largest one  ===========\n",
    "\n",
    "import time\n",
    "def is_prime_v1(n):\n",
    "        if n == 1 or n == 0:\n",
    "            return False\n",
    "        for d in range(2,n):\n",
    "            if n % d ==0:\n",
    "                return False\n",
    "        return True\n",
    "#======= Time Function  ========\n",
    "t0 = time.time()\n",
    "a = int(input(\"Enter upper boundary\\n\"))\n",
    "b = int(input(\"Enter lower boundary\\n\"))\n",
    "t = list()\n",
    "for n in range(a,b+1):\n",
    "    tex = is_prime_v1(n)\n",
    "    if tex == True:\n",
    "       #print(max(t))\n",
    "        t.append(n)\n",
    "    else:\n",
    "        continue\n",
    "t1 = time.time()\n",
    "print(\"\\nList of prime: \",t)\n",
    "print(\"\\nLargest of prime list: \",max(t))\n",
    "print(\"\\nTime required: \",t1 - t0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "import time\n",
    "def is_prime_v2(n):\n",
    "        if n == 1 or n == 0:\n",
    "            return False\n",
    "        max_divisor = math.floor(math.sqrt(n))\n",
    "        for d in range(2,max_divisor+1):\n",
    "            if n % d ==0:\n",
    "                return False\n",
    "        return True\n",
    "#======= Time Function  ========\n",
    "t0 = time.time()\n",
    "a = int(input(\"Enter upper boundary\\n\"))\n",
    "b = int(input(\"Enter lower boundary\\n\"))\n",
    "t = list()\n",
    "for n in range(a,b+1):\n",
    "    tex = is_prime_v2(n)\n",
    "    if tex == True:\n",
    "       #print(max(t))\n",
    "        t.append(n)\n",
    "    else:\n",
    "        continue\n",
    "t1 = time.time()\n",
    "print(\"\\nList of prime: \",t)\n",
    "print(\"\\nLargest of prime list: \",max(t))\n",
    "print(\"\\nTime required: \",t1 - t0)"
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
