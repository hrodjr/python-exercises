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

# 1.a. Propmt the user for a day of the week, print out whether the day is Monday or not.

# In[ ]:


user_input = input("What day of the week is it?")
if user_input == 'Monday':
    print(f'Today is {user_input}!')
else:
    print(f'Not Today!')


# 1.b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[10]:


user_input = input(f"What day of the week is it?")
if user_input == 'Monday':
    print(f'{user_input} is a Weekday!')
elif user_input == 'Tuesday':
    print(f'{user_input} is a Weekday!')
elif user_input == 'Wednesday':
    print(f'{user_input} is a Weekday!')
elif user_input == 'Thursday':
    print(f'{user_input} is a Weekday!')
elif user_input == 'Friday':
    print(f'{user_input} is a Weekday!')
elif user_input == 'Saturday':
    print(f"{user_input} - It's the Weekend!")
elif user_input == 'Sunday':
    print(f"{user_input} - It's the Weekend!")
else:
    print(f"You don't know your days of the week!")
    


# ### Question
# - Would something like this work?

# In[19]:


user_input = input("What day of the week is it?")
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday", "Sunday"]
weekend = ["Saturday", "Sunday"]
while user_input == ???
    for the_day_of_week in weekday:
        if the_day_of_week in weekend:
            print(f"If it's {the_day_of_week} it must be the Weekend!")
        else:
            print(f"{the_day_of_week} is a Weekday")


# 1.c. create variables and make up values for
# 
#  - the number of hours worked in one week
#  - the hourly rate
#  - how much the week's paycheck will be

# In[33]:


hours = 45
rate = 10
overtime_rate = 10 * 1.5


# 1.d. write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[34]:


if hours <= 40:
    print(hours * rate)
elif hours > 40:
    print((hours * rate) + (overtime_rate * (hours - 40)))


# # Loop Basics
# 
# ## 2.a. While
# 
# - Create an integer variable i with a value of 5.
# - Create a while loop that runs so long as i is less than or equal to 15
# - Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15

# In[37]:


i = 5
while i <= 15:
    print (i)
    i += 1


# 2.a. (continued)
# - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
#  
#  I also tried:
#  for n in range (100):
#  -  if n % != 0:
#  - continue
#  - print(n)

# ### range() inside the () is start, stop, and step. In this instance the step is counting down by -5
# 2.a. 
# -Alter your loop to count backwards by 5's from 100 to -10.
# AND
# -Write a loop that uses print to create the output shown below.

# In[116]:


for n in range(100, -15, -5):
    print(n)


# In[109]:


for n in range(100, 0, -1):
    if n % 5 != 0:
        continue
    print(n)


# ### Questions:
# - How do i get it to do what it says to do because I am obvioulsy not doing it correctly.
# - Why doesn't my code stop at a number under 10? Why does it stop at 100?
# 2.a. Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
#  2
#  4
#  16
#  256
#  65536

# In[93]:


x = 2
while x <= 10:
    print(x * x)
    x += 2


# ## 2.b For LOOPS

# 2.b.i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# 
# For example, if the user enters 7, your program should output:
# 
# 
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

# In[118]:


user_input = int(input("Enter a number: "))
for mul in range(1, 11):
    print(f"{user_input} X {mul} = ", (user_input * mul))


# ### Question
# - How?
# 
# 2.b.ii. Create a for loop that uses print to create the output shown below.1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# In[153]:


x = "1"
for y in range (1,10):
    print(x * y)
    


# ### Question
# - Not sure how to combine while and if with user input.
# 
# 2.c.i. Break and Continue
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# 
# Your output should look like this:
# 
# 
# Number to skip is: 27
# 
# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

# In[ ]:


# Doesn't work. Not sure how to work the if statement with input.
user_input = input("Enter an odd number between 1 and 50: ")
while user_input.isdigit() == False:
    print(f"Enter an odd number.")
    user_input = input("Enter an odd number between 1 and 50: ")
    for num in range(1,10):
        if num % 2 == 0:
            continue
            print(f"Here is an odd number: {user_input}")


# In[ ]:





# In[ ]:




