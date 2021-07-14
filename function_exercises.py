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


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[20]:


word = 'hector'

if word[0] not in 'aeiou':
        word = word.capitalize()
word


# In[23]:


def cap_word(word):
    if word[0] not in 'aeiou':
        word = word.capitalize()
    return word

word = "nope"
cap_word(word)


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[25]:


#first worked out the equation
bill = 10
tip_percent = 0.10

bill * tip_percent


# In[27]:


def calculate_tip(bill, tip_percent): #defined (def) the function (calculate_tip) and set the parameters inside the parens "bill" and "tip_percent"
    return bill * tip_percent #Function Body "return" sets the equation up for the answer

bill = 10 #sets the bill amount
tip_percent = 0.10 #sets the percentage

calculate_tip(bill, tip_percent) #runs the equation set by the Function Body


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[33]:


# first worked out the equation
price = 10
discount = .2

price - (price * discount)


# In[35]:


def apply_discount(price, discount): #defined (def) the function (apply_discount) and set the parameters inside the parens "price" and "discount"
    return price - (price * discount) #Function Body "return" sets the equation up for the answer

price = 10 #sets the price
discount = .2 #sets the discount

apply_discount(price, discount) #runs the equation set by the Function Body


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[51]:


str = "1,,1" #setting the string for the function
number = " " #place holder for the output

for char in str: #"for" loop in order to loop through each character. "char" variable set for each character "in" the "string"
    if char not in ",": #"if" condition to check each "char" that is NOT (not in) a comma
        number += char #takes the above place holder "number" and checks each character by character
float(number) #returns the output "place holder - number" with a decimal


# In[52]:


def handle_commas(str):
    number = " "
    for char in str:
        if char not in ",":
            number += char
    return float(number)


# In[53]:


str = "1,1,2,,,,3,,4"
handle_commas(str)


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[54]:


def get_letter_grade(number): #define "def" the function "get_letter_grade" and sets the "number" as the parameter. "number" is the grade number.
    if number <= '59':#"if" condition to check the grade number.
        print('F')
    elif number <= '69':
        print('D')
    elif number <= '79':
        print('E')
    elif number <= '89':
        print('B')
    else:
        print('A')


# In[57]:


number = "49" #sets the grade number
get_letter_grade(number)#returns the letter grade


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[69]:


def remove_vowels(str): #defines "def" the function "remove_vowels" and sets the parameter "str" -  
    letters = "" #place holder for the letters in the "str"
    for char in str: #"for" each character "char" in the "str" - sets the condition to search each character in the strg
        if char.lower() not in "aeiou": #"if" the character (.lower sets each letter in the string to lower case) is "not in" the listed vowels 'aeiou'
            letters += char #checks each letter in the string of characters
    return letters
            


# In[70]:


str = ("Aabecidofu") #the string in which the function is checking
remove_vowels(str) #returns the "str" without the vowels


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

# In[88]:


def normalize_name(str):
    normal = ""
    for char in str:
        if char.isalnum() == True:
            normal += char
    return normal
        
        
str = " n#@o !W@#$%^&*(<>?/a:;[}]{\|y 1*2,,3? "
normalize_name(str)


# In[ ]:




