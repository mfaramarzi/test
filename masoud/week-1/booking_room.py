{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9f678322",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "5\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "57\n"
     ]
    }
   ],
   "source": [
    "#I have be given a list of already booked rooms\n",
    "#the hotel has r rooms\n",
    "\n",
    "#########################\n",
    "#sdo code\n",
    "\n",
    "#getting two input numbers\n",
    "#getting a list of n numbers\n",
    "#if n == r\n",
    "#print too late\n",
    "#else if r > n\n",
    "# print (a random number between 1 and r (included) excluding the list of n numbers inputed)\n",
    "#####################\n",
    "\n",
    "r = int(input()) #getting a value for r\n",
    "\n",
    "n = int(input()) #getting a value for n\n",
    "\n",
    "lst = [] #creating an empty list\n",
    "\n",
    "\n",
    "#iterating till the range\n",
    "for i in range (n):\n",
    "\tele = int(input())\n",
    "\n",
    "\tlst.append(ele) #adding the element\n",
    "\n",
    "from random import choice\n",
    "\n",
    "if (r == n):\n",
    "\tprint(\"too late\")\n",
    "\n",
    "elif (r > n):\n",
    "\tprint (choice([i for i in range(1 , r+1) if i not in lst]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e0c084b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "csc591",
   "language": "python",
   "name": "csc591"
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
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
