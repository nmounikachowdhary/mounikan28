#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Program to find Area Of Circle using Circumference

import math

circumference = float(input(' Please Enter the Circumference of a circle: '))
area = (circumference * circumference)/(4 * math.pi)

print(" Area Of a Circle = %.2f" %area)


# In[2]:


from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)


# In[5]:


import math 
  
pi = 3.14159
  
# Function to find 
# area of segment 
def area_of_segment(radius, angle): 
    # Calculating area of sector 
    area_of_sector = pi *(radius * radius)  * (angle / 360) 
    # Calculating area of triangle 
    area_of_triangle = 1 / 2 * (radius * radius) *math.sin((angle * pi) / 180)
    return area_of_sector - area_of_triangle;  
# Driver Code 
radius = 10.0
angle = 90.0
print("Area of minor segment =", 
       area_of_segment(radius, angle)) 
print("Area of major segment =", 
      area_of_segment(radius, (360 - angle))) 


# In[6]:


import math
math.sin(60)


# In[7]:


math.cos(180)


# In[8]:


math.tan(90)


# In[9]:


5^8


# In[10]:


math.log2(1024)


# In[11]:


math.log10(1024)


# In[12]:


math.ceil(23.56)


# In[13]:


math.floor(23.56)


# In[15]:


from random import shuffle
list=[100,1,2,3,30,40,"hai","helo"]
shuffle(list)
print(list)


# In[21]:


from random import shuffle
list=[100,1,2,3,30,40,"hai","helo"]
shuffle(list)
print(list)


# In[ ]:




