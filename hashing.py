# -*- coding: utf-8 -*-
"""Hashing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_5mad9wxqgxIv96RvkjUz4fNUUB1qKts
"""

def mod(number, cellNumber):
    return number % cellNumber


# print(mod(400, 24))


def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

print(modASCII("ABC", 24))