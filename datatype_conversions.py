Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data type conversions
#int()
int(8)
8
int(5.3)
5
int("nandhu")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("nandhu")
ValueError: invalid literal for int() with base 10: 'nandhu'
int(9_7j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(9_7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float()
float(4)
4.0
float(9.4)
9.4
float("nandhu")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("nandhu")
ValueError: could not convert string to float: 'nandhu'
float(9+8j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(9+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#str()
str(3)
'3'
>>> str(9.4)
'9.4'
>>> str("nandhu")
'nandhu'
>>> str(9+4j)
'(9+4j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex()
>>> complex(5)
(5+0j)
>>> complex(6+7j)
(6+7j)
>>> complex("nandhu")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("nandhu")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool()
>>> bool(2)
True
>>> bool(4+1j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool(2.9)
True
>>> #complex()
>>> complex(9.5)
(9.5+0j)
