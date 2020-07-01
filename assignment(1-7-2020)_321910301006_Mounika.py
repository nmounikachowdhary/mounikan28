#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


# In[2]:


n = 5
l = [{} for _ in range(n)]
print(l)


# In[3]:


# Python program to show working  
# of keys in Dictionary 
  
# Dictionary with three keys 
Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'} 
  
# Printing keys of dictionary 
print(Dictionary1.keys()) 
  
# Creating empty Dictionary 
empty_Dict1 = {} 
  
# Printing keys of Empty Dictionary 
print(empty_Dict1.keys()) 


# In[4]:


d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])


# In[5]:


my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))


# In[6]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


# In[ ]:




