#!/usr/bin/env python
# coding: utf-8

# # control_structures_exercises

# 1. Conditional Basics
# 
#     a. prompt the user for a day of the week, print out whether the day is Monday or not
# 
#     b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# 
#     c. create variables and make up values for
# 
#         - the number of hours worked in one week
#         - the hourly rate
#         - how much the week's paycheck will be
#         
#     d. write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[8]:


user_input = input("What day of the week is it?")
if user_input == 'Monday':
    print(f'Today is {user_input}!')
else:
    print(f'Not Today!')


# In[ ]:


user_input = input(f"What day of the week is it?")
if user_input == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
    print(f'{user_input} is a weekday.')
elif user_input == 'Saturday' or 'Sunday':
    print(f'{user_input} it is the Weekend!')


# In[ ]:




