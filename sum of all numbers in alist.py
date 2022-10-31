#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20


# In[1]:


def sum_of_numbers(sample_list):    
    total = 0                       
    for number in sample_list:      
        total+= number
    return total
sample_list = [8, 2, 3, 0, 7]      
summ = sum_of_numbers(sample_list)
print(f" sum of number {sample_list} = {summ}")         

