Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+" "+b)
python course
fname="nandhu"
lname="chocky"
print(a+b)
pythoncourse
print(fname+" "+lname)
nandhu chocky
print(fname.title()+" "+lname.title())
Nandhu Chocky
print(fname+" "+lname).title()
nandhu chocky
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(fname+" "+lname).title()
AttributeError: 'NoneType' object has no attribute 'title'
print((fname+" "+lname).title())
Nandhu Chocky
#formatng
a=2
b=4
print(a+b)
6
print("the sum is",a+b)
the sum is 6
city="vja"
print("the city is",city)
the city is vja
#format method()
a="motu"
b="pathlu"
print("hello",a+b)
hello motupathlu
>>> print("hello {}{}".format(a,b))
hello motupathlu
>>> print("hello {} {}".format(a,b))
hello motu pathlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello pathlu
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a} {b}")
hello sita ram
>>> print(f"hello {a} hello {b}")
hello sita hello ram
>>> 
======== RESTART: C:/Users/surib/OneDrive/Desktop/codegnan/python/mul.py =======
a:2
b:4
2*4=()
>>> 
======== RESTART: C:/Users/surib/OneDrive/Desktop/codegnan/python/mul.py =======
a:2
b:5
2*5=10
>>> a=2
>>> b=9
>>> print(a*b)
18
>>> c=a*b
>>> print("the product is {}".format(c))
the product is 18
>>> print("the product is {c}")
the product is {c}
>>> print("the product is {}".format(a*b))
the product is 18
>>> print("the product is {a*b}")
the product is {a*b}
>>> print(f"the product is {a*b}")
the product is 18
