>>> type('99.9')
<class 'str'>
>>> type('"False")
  File "<stdin>", line 1
    type('"False")
                 ^
SyntaxError: EOL while scanning string literal
>>> type("false")
<class 'str'>
>>> type(False)
<class 'bool'>
>>> type(99.9)
<class 'float'>
>>> type('0')
<class 'str'>
>>> type(0)
<class 'int'>
>>> type(True)
<class 'bool'>
>>> type('True')
<class 'str'>
>>> type([{}])
<class 'list'>
>>> type{'a':[]}
  File "<stdin>", line 1
    type{'a':[]}
        ^
SyntaxError: invalid syntax
>>> type({'a':[]})
<class 'dict'>
>>> 

# A term or phrase typed into a search box? string
# If a user is logged in? string
# A discount amount to apply to a user's shopping cart? float
# Whether or not a coupon code is valid? bool
# An email address typed into a registration form? string
# The price of a product? float
# A Matrix? int
# The email addresses collected from a registration form? string
# Information about applicants to Codeup's data science program? dict


# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.


In [1]: print ('1' + 2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-922b4761d6c9> in <module>
----> 1 print ('1' + 2)

TypeError: can only concatenate str (not "int") to str

In [2]: print (6 % 4)
2

In [3]: type (6 % 4)
Out[3]: int

In [4]: type(type(6 % 4))
Out[4]: type

In [5]: print('3 + 4 is ' + 3 + 4)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-a2ba62681605> in <module>
----> 1 print('3 + 4 is ' + 3 + 4)

TypeError: can only concatenate str (not "int") to str

In [6]: '3 + 4 is ' + 3 + 4
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-d779031f2239> in <module>
----> 1 '3 + 4 is ' + 3 + 4

TypeError: can only concatenate str (not "int") to str

In [7]: 0 < 0
Out[7]: False

In [8]: 'False' == False
Out[8]: False

In [9]: True == 'True'
Out[9]: False

In [10]: 5 >= -5
Out[10]: True

In [11]: print (5 >= -5)
True

In [12]: True or "42"
Out[12]: True

In [13]: 6 % 5
Out[13]: 1

In [14]: 5 < 4 and 1 == 1
Out[14]: False

In [15]: 'codeup' == 'codeup' and 'codeup' == 'Codeup'
Out[15]: False

In [16]: 4 >= 0 and 1 !== '1'
  File "<ipython-input-16-28fe0c9082c3>", line 1
    4 >= 0 and 1 !== '1'
                   ^
SyntaxError: invalid syntax


In [17]: 6 % 3 == 0
Out[17]: True

In [18]: 5 % 2 != 0
Out[18]: True

In [19]: [1] + 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-19-54324b7054ad> in <module>
----> 1 [1] + 2

TypeError: can only concatenate list (not "int") to list

In [20]: [1] + [2]
Out[20]: [1, 2]

In [21]: [1] * 2
Out[21]: [1, 1]

In [22]: [1] * [2]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-22-887f6473eaff> in <module>
----> 1 [1] * [2]

TypeError: can't multiply sequence by non-int of type 'list'

In [23]: [] + [] == []
Out[23]: True

In [24]: {} + {}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-24-03eea6c7a00d> in <module>
----> 1 {} + {}

TypeError: unsupported operand type(s) for +: 'dict' and 'dict'