#!/usr/bin/env python
# coding: utf-8

# # Function Exercises
# 
# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[48]:


def is_two(n):
    return n == 2 or n == "2"
n = 3
is_two(n)


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[56]:


def is_vowel(str):
    return str.lower() in "aeiou"
str = "A"
is_vowel(str)


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[65]:


def is_consonant(str):
    return str.lower() not in "aeiou"
str = "a"
is_consonant(str)


# In[ ]:




