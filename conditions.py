#conditions
#if - condition by using comparison operators
#<,>,<=,>=,==,!=
a=12
b=14
if a<b:
     print("true")

a=12
b=14
if a>b:
     print("true")

a=121
b=141
if a<=b:
     print("true")

a=220
b=420
if b>=a:
     print("true")


a=78
b=198
if a!=b:
     print("not equal")

a=75
b=170
if a==b:
     print("equal")

a=88
b=88
if a==b:
     print("equal")

a=int(input("a:"))
b=int(input("b:"))
if a<b:
    print("less")

a=int(input("a:"))
if a<100:
    print("less")

a="python"
if a=="java":
    print("true")

a="python"
if a!="java":
    print("true")

a=input("data")
if a=="java":
    print("true")

#if - condition by using logical operators
#and,or,not
a=44
b=94
if a<b and b>a:
    print("less")

a=47
b=97
if a<=b and b>=a:
    print("less")

a=49
b=99
if a!=b and a==b:
    print("true")

a=73
b=113
if a<b or b>a:
    print("less")

a=65
b=85
if a<=b or b>=a:
    print("less")
a=41
b=91
if a!=b or a==b:
    print("true")

a=132
b=152
if not a<b:
    print("less")

a=136
b=156
if not a>b:
    print("less")

a=138
b=158
if not a>b and b>a:
    print("less")

a=139
b=159
if not a>b or b>a:
    print("less")

a=int(input())
b=int(input())
if a<b and b>a:
    print("less")

#if - condition by using identify operators
#is,is not

a=5
if type(a) is int:
    print("it is int")

a=5
if type(a) is not int:
    print("false")

a=int(input("a:"))
if type(a) is int:
    print("it is int")

a=15.0
if type(a) is float:
    print("it is float")

a=15.0
if type(a) is not float:
    print("false")

a=float(input("a:"))
if type(a) is float:
    print("it is float")


a="pyhton"
if type(a) is str:
    print("it is str")

a="python"
if type(a) is not str:
    print("false")

a=str(input("a:"))
if type(a) is str:
    print("it is str")

#if - condition by using membership operators
a=1,2,3,4,5,6,7,8,9,10
if 10 in a:
    print("true")


a=1,2,3,4,5,6,7,8,9,10
if 20 in a:
    print("true")

a=1,2,3,4,5,6,7,8,9,10
if 20 not in a:
    print("true")

a=int(input("enter value:"))
if 30 in a:
    print("true")#error

a=1,2,3,4,5,6,7,8,9,10
b=int(input("a:"))
if 10 in a:
    print("true")




#if-else conditions by using comparison operators
a=13
b=16
if a<b:
     print("true")
else:
     print("false")

a=32
b=62
if a>b:
     print("true")
else:
     print("false")

a=93
b=123
if a!=b:
     print("not equal")
else:
     print("equal")

#if-else condition by using logical operators
a=45
b=410
if a<b and b>a:
     print("less")
else:
     print("true")

a=55
b=105
if a<b or b>a:
     print("less")
else:
     print("true")

a=56
b=106
if  not a<b and b>a:
     print("less")
else:
     print("true")

#if-else condition by using identify operators
a=47
if type(a) is int:
    print("it is int")
else:
     print("false")

a="python"
if type(a) is not int:
    print("false")
else:
     print("true")

#if-else conditon by using membership operators
a=1,2,3,4,5,6,7,8,9,10
if 10 in a:
    print("true")
else:
     print("false")

a=1,2,3,4,5,6,7,8,9,10
if 20 not in a:
    print("true")
else:
     print("false")

     

#if-elif-else conditions by using comparison operators
a=88
b=108
if a<b:
     print("less")
elif b>a:
     print("greater")
else:
     print("equal")

a=89
b=109
if a==b:
     print("less")
elif b>a:
     print("greater")
else:
     print("equal")

a=81
b=101
if a<b:
     print("less")
elif b>a:
     print("greater")
else:
     print("equal")

a=28
b=210
if a>b:
     print("less")
elif b<a:
     print("greater")
elif a!=b:
     print("not equal")
else:
     print("equal")

#if-elif-else conditions by using logical operators
a=35
b=310
if a<b and b>a:
     print("and")
elif a<b or b>a:
     print("or")
elif  not a<b and b>a:
     print("not")
else:
     print("true")

#if-elif-else condition by using identify operators
a=44
if type(a) is int:
    print("it is int")
elif type(a) is str:
     print("it is str")
elif type(a) is float:
     print("it is float")
else:
     print("false")

a=45.0
if type(a) is int:
    print("it is int")
elif type(a) is str:
     print("it is str")
elif type(a) is float:
     print("it is float")
else:
     print("false")

#if-elif-else conditon by using membership operators
a=1,2,3,4,5,6,7,8,9,10
if 10 in a:
    print("10")
elif 5 in a:
     print("5")
elif 1 in a:
     print("1")
else:
     print("false")

a=1,2,3,4,5,6,7,8,9,10
if 20 in a:
    print("20")
elif 15 in a:
     print("15")
elif 1 in a:
     print("1")
else:
     print("false")

     

#multiple-if conditions by using comparison operators
a=206
b=406
if a<b:
     print("less")
if b>a:
     print("greater")
if a!=b:
     print("not equal")

a=720
b=740
if a==b:
     print("less")
if b>a:
     print("greater")
if a!=b:
     print("not equal")

a=820
b=840
if a>b:
     print("less")
if b<a:
     print("greater")
if a==b:
     print("not equal")
else:
     print("false")

#multiple-if conditions by using logical operators
a=35
b=310
if a<b and b>a:
     print("and")
if a<b or b>a:
     print("or")
if  not a<b and b>a:
     print("not")

#multiple-if condition by using identify operators
a=44
if type(a) is int:
    print("it is int")
if type(a) is str:
     print("it is str")
if type(a) is float:
     print("it is float")

#multiple-if conditon by using membership operators
a=1,2,3,4,5,6,7,8,9,10
if 10 in a:
    print("10")
if 5 in a:
     print("5")
if 1 in a:
     print("1")
if 11 in a:
     print("11")

#nested-if
a=41
b=61
if a<b:
     print("less")
     if b>a:
          print("greater")

a=42
b=63
if a>b:
     print("less")
     if b>a:
          print("greater")

a=37
b=312
if a<b:
     print("less")
     if b==a:
          print("equal")

a=124
b=134
if a<b:
     print("less")
     if b==a:
          print("equal")
     else:
          print("true")

a=154
b=174
if a>b:
     print("less")
     if b>a:
          print("greater")
else:
          print("true")

a=96
b=116
if a<b:
     print("less")
     if b>a:
          print("greater")
     else:
          print("true")
else:
     print("false")

a=9
b=11
if a<b:
     print("less")
     if b==a:
          print("greater")
     elif a!=b:
          print("not equal")

a=8
b=12
if a<b:
     print("less")
     if b==a:
          print("greater")
     elif a>=b:
          print("not equal")
     else:
          print("equal")
