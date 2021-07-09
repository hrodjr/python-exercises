#!/usr/bin/env python
# coding: utf-8

# # Break and Continue section examples

# In[1]:


for n in range (100_000):
    print (n)
    if n > 10:
        break


# In[5]:


for n in range (10):
    if n % 2 == 0:
        continue
    print (f'Here is an odd number: {n}')


# In[6]:


dataset = [{'name': 'age', 'type': 'int', 'data': [20, 25, 43, 11, 15, 53, 36]},
           {'name': 'is_vegetarian', 'type': 'boolean', 'data': [False, True, False, False, True, False, False]},
           {'name': 'shoe size', 'type': 'int', 'data': [8, 11, 7, 10, 7, 9, 10]},
           {'name': 'ISP', 'type': 'categorical', 'data': ['AT&T', 'Spectrum', 'Spectrum', 'Spectrum', 'AT&T', 'Spectrum', 'AT&T']},
           {'name': 'BMI', 'type': 'float', 'data': [29.9, 20.4, 23.3, 21.7, 22.2, 22.8, 27.0]}]

# print the means for the numeric data
for feature in dataset:
    if feature['type'] == 'categorical' or feature['type'] == 'boolean':
        print(f"{feature['name']} is not numeric, skipping")
        continue
    avg = sum(feature['data']) / len(feature['data'])
    print(f"{feature['name']} average: {avg:.2f}") # the :.2f formats the decimal to 2 places.


# In[ ]:




