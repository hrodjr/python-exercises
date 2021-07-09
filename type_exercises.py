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