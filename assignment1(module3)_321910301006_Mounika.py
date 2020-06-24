#!/usr/bin/env python
# coding: utf-8

# In[1]:


#genrate first N nos of fibonocci numbers 
nterms = int(input("how many terms"))
n1, n2 =0, 1
count = 0
if nterms <= 0:
    print("enter a positive integer")
elif nterms == 1:
    print("fibonocci sequence",nterms,":")
    print(n1)
else:
    print("fibonocci sequence:")
    while count < nterms :
        print(n1)
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count += 1


# In[3]:


# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 544
num2 = 244

print("The H.C.F. is", compute_hcf(num1, num2))


# In[5]:


b_num = list(input("binary no:"))
value = 0
for i in range(len(b_num)):
    digit = b_num.pop()
    if digit =='1':
        value = value + pow(2, i)
print("decimal value",value)


# In[7]:


num = int(input("enter a no"))
print("multiplication table of",num)
for i in range(1, 11):
    print(num,"x",i,"=",num * i)


# In[ ]:




