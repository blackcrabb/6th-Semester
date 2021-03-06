# -*- coding: utf-8 -*-
"""Control Structures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YNMXVbN1BLQliA5g-5nn2npoLNDLg5X2

Sum of digits of a number
"""

def sumofdigits(n):
    sum=0
    while(n!=0):
      sum=sum+(n%10)
      n=n//10
    print(sum)

def startingPoint():
    val = int(input("Enter a no."))
    sumofdigits(val)

if __name__=="__main__":
    startingPoint()

"""Print following Patterns

a
"""

def pattern(n):
    for i in range(0,n):
        for j in range(0,n-i):
          print(j+1,end=' ')
        print()

def startingPoint():
    val = int(input("Enter a no."))
    pattern(val)

if __name__=="__main__":
    startingPoint()

"""b"""

def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
          print(n-j,end=' ')
        print()

def startingPoint():
    val = int(input("Enter a no."))
    pattern(val)

if __name__=="__main__":
    startingPoint()

"""c"""

def pattern(n):
    for i in range(1, n + 1):
        for j in range(n - i, 0, -1):
            print(" ", end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        for j in range(2, i+1):
            print(j, end=" ")
        print()


def startingPoint():
    val = int(input("Enter a no."))
    pattern(val)


if __name__ == "__main__":
    startingPoint()