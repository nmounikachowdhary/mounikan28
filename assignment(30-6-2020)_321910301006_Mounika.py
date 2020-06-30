#!/usr/bin/env python
# coding: utf-8

# In[6]:


def file_read(fname):
    txt = open(fname)
    print(txt.read())
file_read('text.txt')


# In[7]:


def file_read(fname):
    from itertools import islice
    with open(fname, "w")as myfile:
        myfile.write("python\n")
        myfile.write("hello")
    txt=open(fname)
    print(txt.read())
file_read('abc.txt')        


# In[8]:


def file_read(fname):
    with open(fname) as f:
        content_list = f.readlines()
        print( content_list)
file_read(\'test.txt\')


# In[9]:


def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))


# In[10]:


file_path = r"C:\Users\userName\Documents\image.txt"

#2
lines_count = 0

#3
with open(file_path,'r') as f:
  #4
  for l in f:
    #5
    lines_count = lines_count +1

#6
print("Total number of lines : ",lines_count)


# In[ ]:




