#!/usr/bin/env python
# coding: utf-8

# # 2. list which contain the sum of of the number of tuples:

# In[2]:


list1=[(1,2),(3,4),(5,6),(4,5)] 
  
print("The original tuple is : " + str(list1))  
   
res = list(map(sum, list1)) 

print("The summation of tuple elements are : " + str(res))  


# # 3. list contain list and tuple .make the elements of inner lists and tuples to outer list:

# In[31]:



list1 = [(1, 2, 3),[1,2],["a","hit","less"]]

tup1 = list1[0]
print(tup1)

def convert(list): 
   return tuple(list)


list3 = list1[1] + list1[2]
print(list3)
tup2 = convert(list3)
print (tup2)

tup3= tup1 + tup2
print (tup3)


# # 1. make dictionaryin which keys become values and values become keys:

# In[7]:



port1 = {21:"FTP", 22:"SSH", 23:"TELNET", 80:"HTTP"} 

port2 = dict([(value, key) for key, value in port1.items()]) 

print ("Original dictionary is : ") 
print(port1) 

print() 

print ("Dictionary after swapping is : ") 
print("keys:values") 
for i in port2: 
   print(i, " : ", port2[i]) 

