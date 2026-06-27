Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=10
>>> type(a)
<class 'int'>
>>> b=9.9
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="python"
>>> type(d)
<class 'str'>
>>> e='''idle'''
>>> type(e)
<class 'str'>
>>> f=9+5j
>>> type(f)
<class 'complex'>
>>> g=9j+9
>>> type(g)
<class 'complex'>
>>> h=2j
>>> type(h)
<class 'complex'>
>>> a=6+9i
SyntaxError: invalid decimal literal
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> c=true
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    c=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> d="true"
>>> type(d)
<class 'str'>
