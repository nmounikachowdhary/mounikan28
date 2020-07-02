#!/usr/bin/env python
# coding: utf-8

# In[3]:


#creat atuple with different types
tuplex = ("tuple", False,3.2,1)
print(tuplex)


# In[4]:


#convert a tuple to a string
tup = ('e', 'x', 'e', 'r', 'c' ,'i', 's',) 
str = ''.join(tup)
print(str)


# In[6]:


tuplex=(2,3,4,5,6,7)
_slice=tuplex[3:5]
print(_slice)
_slice=tuplex[:6]
print(_slice)
_slice=tuplex[5:]
print(_slice)
_slice=tuplex[:]
print(_slice)
_slice=tuplex[-8:-4]
print(_slice)
tuplex=tuple("hello world")
print(tuplex)
_slice=tuplex[2:9:2]
print(_slice)
_slice=tuplex[::4]
print(_slice)
_slice=tuplex[9:2:-4]
print(_slice)


# In[7]:


tuplex = tuple("hello")
print(tuplex)
print(len(tuplex))


# In[8]:


tuplex = ((2,"w"),(3,"r"))
print(dict((y, x) for x,y in tuplex))


# In[9]:


x=("helloworld")
y=reversed(x)
print(tuple(y))
x=(5,10,15,20)
y=reversed(x)
print(tuple(y))


# In[11]:


l=[("x",1),("x",2),("x",3),("y",1),("y",2),("z",1)]
d={}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)


# In[12]:


listx=[5,10,7,4,15,3]
print(listx)
tuplex=tuple(listx)
print(tuplex)


# In[ ]:




