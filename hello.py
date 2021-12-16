{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0617d58b",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 1         # assign variable x the value 1\n",
    "y = x + 5     # assign variable y the value of x plus 5\n",
    "z = y         # assign variable z the value of y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb429c18",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 1       # integer\n",
    "x = 1.0     # decimal (floating point)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7eb1b69d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "x = 1\n",
    "print(type(x)) # outputs: <class 'int'>\n",
    "\n",
    "x = 1.0\n",
    "print(type(x)) # outputs: <class 'float'>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3a31ebfe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "x = True\n",
    "print(type(x)) # outputs: <class 'bool'>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cdfee57e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is a string\n",
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "x = 'This is a string'\n",
    "print(x) # outputs: This is a string\n",
    "print(type(x)) # outputs: <class 'str'>\n",
    "y = \"This is also a string\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bb21a5a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World!\n"
     ]
    }
   ],
   "source": [
    "x = 'Hello' + ' ' + 'World!'\n",
    "print(x) # outputs: Hello World!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a49796d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World!\n"
     ]
    }
   ],
   "source": [
    "print('Hello World!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ff9d1c7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "PI = 3.14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d0d35253",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.14"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "PI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "23688589",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name:Susannah\n",
      "Susannah\n"
     ]
    }
   ],
   "source": [
    "name = input('Enter your name:')\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "66b8f1c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your name?\n",
      "Susannah\n",
      "Susannah\n"
     ]
    }
   ],
   "source": [
    "print('What is your name?')\n",
    "name = input()\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "34ceb20d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 5\n",
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "x = input('Enter a number: ')\n",
    "print(type(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "0f418a63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number is 5\n"
     ]
    }
   ],
   "source": [
    "x = 5\n",
    "print('The number is ' + str(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b92276d3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

