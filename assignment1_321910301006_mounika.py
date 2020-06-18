#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Program - Calculate Circumference of Circle

print("Enter 'x' for exit.");
rad = input("Enter radius of circle: ");
if rad == 'x':
    exit();
else:
    radius = float(rad);
    circumference = 2*3.14*radius;
    print("\nCircumference of Circle =",circumference);


# In[2]:


print("Enter 'x' for exit.");
side = input("Enter side length of square: ");
if side == 'x':
    exit();
else:
    slength = int(side);
    perimeter = 4*slength;
    print("\nPerimeter of Square:", perimeter);


# In[3]:


# Python Program to Swap Two Numbers
 
a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

print("Before Swapping two Number: a = {0} and b = {1}".format(a, b))

temp = a
a = b
b = temp

print("After Swapping two Number: a = {0} and b = {1}".format(a, b))


# In[5]:


a = 21
b = 10
c = 0
c = a + b
print ("line 1 - Value of c is ", c)

c = a - b
print ("Line 2 - Value of c is ", c) 

c = a * b
print ("Line 3 - Value of c is ", c)

c = a / b
print ("Line 4 - Value of c is ", c)

c = a % b
print( "Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b 
print ("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b 
print ("Line 7 - Value of c is ", c)


# In[6]:


principle=float(input("enter the principle amount:"))
time=int(input("enter the time(years)"))
rate=float(input("enter the rate:"))
simple_interest=(principle*time*rate)/100
print("the simple interest is:",simple_interest)


# In[7]:


pi=3.14
r=float(input('enter the radius of the circle:'))
area=pi*r*r
print("area of the circle:%.2f"%area)


# In[8]:


a=float(input('enter first side:'))
b=float(input('enter second side:'))
c=float(input('enter third side:'))
#calculate the semiperimeter
s=(a+b+c)/2
#calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('area of triangle is %0.2f'%area)


# In[9]:


celsius=int(input("Enter the temperature in celcius:"))
f=(celsius*1.8)+32
print("Temperature in farenheit is:",f)


# In[10]:


width = float(input('Please Enter the Width of a Rectangle: '))
height = float(input('Please Enter the Height of a Rectangle: '))

# calculate the area
Area = width * height

# calculate the Perimeter
Perimeter = 2 * (width + height)

print("\n Area of a Rectangle is: %.2f" %Area)
print(" Perimeter of Rectangle is: %.2f" %Perimeter)


# In[ ]:




