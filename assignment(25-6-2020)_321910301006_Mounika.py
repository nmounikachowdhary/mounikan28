#!/usr/bin/env python
# coding: utf-8

# In[9]:


#count no of vowls in agiven string
string='hello world myname is mounika hai'
vowels=0
for i in string:
    if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A'or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
print("no of vowels are:")
print(vowels)


# In[23]:


#remove duplicates from a string
from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
     
print(remove_duplicate("python excercise practice solution"))
print(remove_duplicate("w3resource"))


# In[21]:


#even length words 
def printWords(s): 
      
    # split the string  
    s = s.split(' ')  
      
    # iterate in words of string  
    for word in s:  
          
        # if length is even  
        if len(word)%2==0: 
            print(word)  
  
  
# Driver Code  
s = "i am muskan" 
printWords(s)


# In[20]:


# initializing the string
string = "I am a python programmer"
# splitting the string on space
words = string.split()
# reversing the words using reversed() function
words = list(reversed(words))
# joining the words and printing
print(" ".join(words))


# In[19]:


# Python program to check 
# if a string is binary or not 
  
# function for checking the 
# string is accepted or not 
def check(string) : 
  
    # set function convert string 
    # into set of characters . 
    p = set(string) 
  
    # declare set of '0', '1' . 
    s = {'0', '1'} 
  
    # check set p is same as set s 
    # or set p contains only '0' 
    # or set p contains only '1' 
    # or not, if any one condition 
    # is true then string is accepted 
    # otherwise not . 
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes") 
    else : 
        print("No") 
  
  
          
# driver code 
if __name__ == "__main__" : 
  
    string = "101010000111"
  
    # function calling 
    check(string) 


# In[ ]:




