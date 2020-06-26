#!/usr/bin/env python
# coding: utf-8

# In[1]:


inputStr = "pynativepynvepynative"
countDict = dict()
for char in inputStr:
  count = inputStr.count(char)
  countDict[char]=count
print(countDict)


# In[2]:


import re

inputStr = "English = 78 Science = 83 Math = 68 History = 65"
markList = [int(num) for num in re.findall(r'\b\d+\b', inputStr)]
totalMarks = 0
for mark in markList:
  totalMarks+=mark

percentage = totalMarks/len(markList)  
print("Total Marks is:", totalMarks, "Percentage is ", percentage)


# In[3]:


def findDigitsCharsSymbols(inputString):
  words = inputString.split()
  charCount = 0
  digitCount = 0
  symbolCount = 0
  for char in inputString:
    if char.islower() or char.isupper():
      charCount+=1
    elif char.isnumeric():
      digitCount+=1
    else:
      symbolCount+=1
      
  print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
      
inputString = "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols")
print(findDigitsCharsSymbols(inputString))


# In[4]:


inputStr = "PyNaTive"
words = inputStr.split()
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print("\n arranging characters giving precedence to lowercase letters:")
print(sortedString)


# In[5]:


def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex-1:]+ s2 +s1[middleIndex-1:]
  print("After appending new string in middle", middleThree)
  
appendMiddle("Chrisdem", "IamNewString")


# In[ ]:




