Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print(3+8)
11
a=99
print(a)
99
b=44
print(b)
44
x=90
print(X)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
90
x=66
print(z)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
print(x)
66
9=99
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
print(9)
9
p9=88
print(p9)
88
@=99
SyntaxError: invalid syntax
_=77
print(_)
77
if=88
SyntaxError: invalid syntax
for=99
SyntaxError: invalid syntax
a=9,b=8
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=9;b=8
print(a,b)
9 8
print(a+b)
17
a,b=9,8
print(a,b)
9 8
a=1,2,3,4
print(a)
(1, 2, 3, 4)
a,b,c=8
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a,b,c=8
TypeError: cannot unpack non-iterable int object
a=b=c-66
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a=b=c-66
NameError: name 'c' is not defined
print(a,b,c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(a,b,c)
NameError: name 'c' is not defined
a=b=c=88
print(a,b,c)
88 88 88
print(c)
88
a,b,c=(1,2,3)
print(a,b,c)
1 2 3
a,b,c=1,2,3,4,5,6,7,8,9
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a,b,c=1,2,3,4,5,6,7,8,9
ValueError: too many values to unpack (expected 3)
first name="pooja"
SyntaxError: invalid syntax
first_name="pooja"
print(firstname)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(firstname)
NameError: name 'firstname' is not defined. Did you mean: 'first_name'?
print(first_name)
pooja
firstname="pooja"
pirnt(firstname)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    pirnt(firstname)
NameError: name 'pirnt' is not defined. Did you mean: 'print'?
print(firstname)
pooja
fname="nandhu"
lname="chocky"
print(fname+lname)
nandhuchocky
print(fname+lname)
nandhuchocky
print(fname,lname)
nandhu chocky
print(fname,""lname)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(fname,"",lname)
nandhu  chocky
>>> print(fname+_+lname)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(fname+_+lname)
TypeError: can only concatenate str (not "int") to str
>>> print(fname+"_"+lname)
nandhu_chocky
>>> name="nandhu"
>>> print(name)
nandhu
>>> print("name")
name
>>> city="vja"
>>> print(city)
vja
>>> print(name,city)
nandhu vja
>>> print(name,\n city)
SyntaxError: unexpected character after line continuation character
>>> a=99
>>> print(a)
99
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> name="nandhu"
>>> print(name)
nandhu
>>> NAME="nandhu"
>>> print(NAME)
nandhu
>>> Name="nandhu"
>>> print(Name)
nandhu
