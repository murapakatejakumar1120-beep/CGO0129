Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arithematic
a=3
b=6
print(a+b)
9
print(a-b)
-3
print(a*b)
18
print(a//b)
0
print(a/b)
0.5
print(a**b)
729
print(a%b)
3
#assignment
a=2
b=4
print(a+=b)
SyntaxError: invalid syntax
a=b
a+b
8
del a
del b
a=2
b=4
print(a+=b)
SyntaxError: invalid syntax
a+b
6
a+=b
a
6
b
4
a-=b
a
2
a*=b
a
8
a//=b
a
2
a/=b
a
0.5
a**=b
a
0.0625
a%=b
a
0.0625
a=3
b=6
b+=a
b
9
b-=a
b
6
b*=a
b
18
b//=a
b
6
b/=a
b
2.0
b
2.0



b**=a
b
8.0
b%=a
b
2.0
#comparison
a=5
b=9
a<b
True
a>b
False
b<a
False
b>a
True
a<=b
True
a>=b
False
a!=b
True
a==b
False
b=5
a!=b
False
a==b
True
#logical
a=3
b=8
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a>=b or a<=b
True
a!=b or a==b
True
not True
False
not False
True
#identify
a=5
type(a) is int
True
type(a) is not int
False
type(a) is str
False
type(a) is not str
True
a=4.6
type(a) is float
True
type(a) is not float
False
type(a) is complex
False
a=5+7j
type(a) is complex
True
type(a) is not complex
False
type(a) is bool
False
a=True
type(a) is True
False
type(a) is False
False
a=False
type(a)=True
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
type(a) is True
False
type(a) is False
False
#membership
a=1,2,3,4,5,6,7,8,9,10
1 in a
True
10 in a
True
20 in a
False
30 not in a
True
#bitwise
a=2
b=5
a&b
0
bin(2)
'0b10'
bin(5)
'0b101'
a=4
b=9
a&b
0
bin(4)
'0b100'
bin(9)
'0b1001'
a=3
b=5
a&b
1
bin(3)
'0b11'
bin(5)
'0b101'
>>> a|b
7
>>> a=4
>>> b=8
>>> a|b
12
>>> a=8
>>> ~a
-9
>>> a=77
>>> ~a
-78
>>> b=-45
>>> ~b
44
>>> b=6
>>> b=-6
>>> ~b
5
>>> a=3
>>> a<<2
12
>>> a=5<<3
>>> a=3
>>> a<<3
24
>>> a=5
>>> a<<3
40
>>> a=2
>>> a>>2
0
>>> a=6
>>> a>>3
0
>>> a=9
>>> a>>1
4
