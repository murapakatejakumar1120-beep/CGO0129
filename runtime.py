a=2
b=4
print(a+b)

a=6
b=8
print(a+b)

print(10+10)

#run_time input()
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(a+b)

a=float(input("enter a value:"))
b=float(input("enter b value:"))
print(a+b)

a=str(input("data1:"))
b=str(input("data2:"))
print(a+b,"\n")

a=input("data1:")
b=input("data2:")
print(a+b)

fname=input("first name:")
lname=input("last name:")
print((fname+" "+lname).title())

a=complex(input("enter a value:"))
b=complex(input("enter b value:"))
print(a+b)

a=bool(input("enter a value:"))
b=bool(input("enter b value:"))
print(a+b)

a=bool(input("enter a value:"))
b=bool(input("enter b value:"))
c=bool(input("enter c value:"))
print(a+b+c)

a=int(input("enter a value:"))
b=int(input("enter b value:"))
option=int(input("choose option 1.add 2.sub 3.mul"))
print(a+b)
print(a-b)
print(a*b)

a=int(input("enter a value:"))
b=int(input("enter b value:"))
option=int(input('''choose option
                 1.add
                 2.sub
                 3.mul'''))
print(a+b)
print(a-b)
print(a*b)

a=int(input("enter a value:"))
b=int(input("enter b value:"))
option=int(input("choose option 1.add 2.sub 3.mul"))
print(a+b)
print(a-b)
print(a*b)

a=int(input())
b=int(input())
print(a+b)

a=input()
print(a)

#swapping of two variables
a=10
b=20
a,b=b,a
print("a:",a)
print("b:",b)

a=10
b=20
temp=a
a=b
b=temp
print("a:",a)
print("b:",b)

a=10
b=20
a=a+b
b=a-b
a=a-b
print("a:",a)
print("b:",b)

a=10
b=20
a=a+b
b=a-b
a=a-b
print("after sawpping a=%d,b=%d" %(a,b))

a=float(input("a:"))
b=float(input("b:"))
a=a+b
b=a-b
a=a-b
print("after sawpping a=%f,b=%f" %(a,b))

a=float(input("a:"))
b=float(input("b:"))
a=a+b
b=a-b
a=a-b
print("after sawpping a=%.2f,b=%.2f" %(a,b))

a=input("data1:")
b=input("data2:")
temp=a
a=b
b=temp
print("after sawpping a=%s,b=%s" %(a,b))

a=input("data1:")
b=input("data12")
a,b=b,a
print("after sawpping a=%s,b=%s" %(a,b))
