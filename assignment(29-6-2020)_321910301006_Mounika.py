#!/usr/bin/env python
# coding: utf-8

# In[1]:


mystring = 'Hello, you need to print words which starts with s only in this sentense.'

for word in mystring.split():
    if word[0] == 's':
        print(word)


# In[2]:


mylist = list(range(0,11,2))
print(mylist)


# In[3]:


mylist = [x for x in range(1, 51) if x % 3 == 0]
print(mylist)


# In[4]:


mystring ='Create a list of the first letters of every word in this string'
mylist = [word[0] for word in mystring.split()]
print(mylist)


# In[6]:


# Python3 program to print  
#  even length words in a string  
  
def printWords(s): 
      
    # split the string  
    s = s.split(' ')  
      
    # iterate in words of string  
    for word in s:  
          
        # if length is even  
        if len(word)%2==0: 
            print(word)  
  
  
# Driver Code  
s ='Print every word in this sentence that has an even number of letters'

printWords(s) 


# In[ ]:




