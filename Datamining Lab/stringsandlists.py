# -*- coding: utf-8 -*-
"""StringsandLists.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mzk9iOadRW4lR2q9vrhaYplUkEq5m6CZ

WAP that takes a sentence as an input and convert the text in sentence to pig latin.
"""

def piglatin(val):
    for i in val.split(" "):
        if i[0] in ["a", "e", "i", "o", "u"]:
            print(i + "hay", end=" ")
        else:
            print(i[1 : len(i)] + i[0] + "ay", end=" ")

def startingPoint():
    val = input("Enter a string:")
    piglatin(val)

if __name__=="__main__":
    startingPoint()

"""WAP that takes a list as an input and returns another list without duplicate values.

"""

def duplicatelist(lst):
    res = [] 
    for i in lst: 
        if i not in res: 
            res.append(i)
    return res

def startingPoint():
    lst = [] 
    n = int(input("Enter number of elements : "))  
    for i in range(0, n): 
        ele = int(input()) 
        lst.append(ele) 
    print(duplicatelist(lst))

if __name__=="__main__":
    startingPoint()

"""WAP that takes a list as an input and returns the reversed list"""

def reversealist(lst):
    lst.reverse()
    return lst

def startingPoint():
    lst = [] 
    n = int(input("Enter number of elements : "))  
    for i in range(0, n): 
        ele = int(input()) 
        lst.append(ele) 
    print(reversealist(lst))

if __name__=="__main__":
    startingPoint()