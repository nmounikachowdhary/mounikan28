#!/usr/bin/env python
# coding: utf-8

# In[1]:


#two inputs check wheather they r equal r not
a=input("enter a first number: ")
b=input("enter a second number: ")
if a == b:
    print("both are equal")
else :
    print("not equal")


# In[3]:


#take 3 inputs from user and check :
#all are equal
#any of two are equal
# use and or
print ("first number")
first = input()
print ("second number")
second = input()
print ("third number")
third = input()
all = first == second and second == third and third == first
print ("All are equal:",all)
any = first == second or second == third or third == first
print ("Any of two are equal:",any)


# In[14]:


#Take two number and check whether the sum is greater than 5, less than 5 or equal to 5.
a=2
b=3
sum = a+b
print ("Sum is greater than 5:",sum>5)
print ("Sum is equal to 5:",sum==5)
print ("Sum is lesser than 5:",sum<5)


# In[21]:


#Suppose passing marks of a subject is 35. Take input of marks from
#user and check whether it is greater than passing marks or not.
pm=35
n=int(input('enter a no'))
if n>35:
    print ('Marks is greater than passing marks')
else :
    print ('invalid')


# 

# In[13]:


#write a python function to find the max of 3 no
num1 = 10
num2 = 14
num3 = 12
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


# In[ ]:




