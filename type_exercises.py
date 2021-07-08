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

