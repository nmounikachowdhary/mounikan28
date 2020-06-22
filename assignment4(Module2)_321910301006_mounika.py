#!/usr/bin/env python
# coding: utf-8

# In[3]:


#max of 3 nos
num1 = 108
num2 = 145
num3 = 128
if (num1 >= num2) and (num1 >= num3):
   maximum= num1
elif (num2 >= num1) and (num2 >= num3):
   maximum = num2
else:
   maximum = num3
print("The largest number is", maximum)


# In[5]:


#reverse string
def StringReverse(str1):
    str2 = str1[::-1]
    return str2
string = input("Please enter your own String : ")
string2 = StringReverse(string)
print("\nThe Original String = ", string)
print("The Reversed String = ", string2)


# In[6]:


# taking input from user
number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")


# In[9]:


chr(ord('A'))


# In[8]:


printtype(type(int))


# In[14]:


num = int(input("Enter the value of n: "))
hold = num
sum = 0

if num <= 0:
    print("Enter a whole positive number!") 
else:
    while num > 0:
        sum = sum + num
        num = num - 1;
    # displaying output
    print("Sum of first", hold, "natural numbers is: ", sum)


# In[17]:


# function to check string is  
# palindrome or not  
def isPalindrome(str): 
  
    # Run loop from 0 to len/2  
    for i in range(0, int(len(str)/2)):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
  
# main function 
s = "malayalam"
ans = isPalindrome(s) 
  
if (ans): 
    print("Yes") 
else: 
    print("No")


# In[ ]:




