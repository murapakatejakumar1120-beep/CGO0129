Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#cout()
#count()
a="twinkle twinkle little star"
count("twinke")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count("twinke")
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count(" ")
3
b=("twinkletwinkle")
b.count("twinkle")
2
b.count("twinkletwinkle")
1
#find a string
a="python"
a[2]
't'
a.find("t")
2
a.find("n")
5
b="hello"
b.find("l")
2
#escape sequences
#\n->new line
#\t->tab space
a="name\n mobileno\t mailid\n college\t branch"
print(a)
name
 mobileno	 mailid
 college	 branch
a="name:teja\n mobileno:9638527419\t mailid:teja@gmail.com\n college:urce\t branch:ai-ds"
print(a)
name:teja
 mobileno:9638527419	 mailid:teja@gmail.com
 college:urce	 branch:ai-ds
#replace()
 
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="i love java"
b.replace("java","python")
'i love python'
a
'wait until you succeed'
b
'i love java'
#upper
a="hello"
a.upper()
'HELLO'
#lower()
b="HI"
b.lower()
'hi'
c="python"
c.upper("p")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c[0].upper()
'P'
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.capitalize()
'I am in class'
e.title()
'I Am In Class'
a="python"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b="python course"
b.isalpha()
False
c="pythoncourse"
c.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
e="1234"
e.isdigit()
True
f="pooja"
f.isalnum()
True
g="pooja1234"
g.isalnum()
True
f="pooja@1234"
f.isalnum()
False
#startswith and endswith
a="java"
a.startswith("j")
True
a.endswith("a)
           
SyntaxError: unterminated string literal (detected at line 1)
a.endswith("a")
           
True
#strip()
           
#lstrip(),rstrip()
           
a="      pooja"
           
>>> a.strip()
...            
'pooja'
>>> a.lstrip()
...            
'pooja'
>>> a.rstrip()
...            
'      pooja'
>>> #split()
...            
>>> a="python java c c++"
...            
>>> a.split()
...            
['python', 'java', 'c', 'c++']
>>> b="i am in class room"
...            
>>> b.split()
...            
['i', 'am', 'in', 'class', 'room']
>>> #join
...            
>>> b="vja","hyd","vzg"
...            
>>> "".join(b)
...            
'vjahydvzg'
>>> " ".join(b)
...            
'vja hyd vzg'
>>> "k".join(b)
...            
'vjakhydkvzg'
>>> c="python"
...            
>>> "k".join(c)
...            
'pkyktkhkokn'
