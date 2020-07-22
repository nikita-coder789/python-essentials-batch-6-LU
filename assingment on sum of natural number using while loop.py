#!/usr/bin/env python
# coding: utf-8

# # sum of natural number with for loop 

# In[1]:


sum1=0 
for each in range(1,11):
    print ("\nnumber is",each,end="-> ")    
    sum1 = sum1+ each
    print(sum1,end=",")
print ("\nsum1 of number is",sum1)


# # sum of natural number with WHILE LOOP

# In[2]:


value= int(input("enter a number: "))

if (value<=0):
    print("enter a positive number: ")
else:
    sum2=0
    while(value>0):
        sum2= sum2 + value
        value= value - 1
print("the sum is",sum2)

