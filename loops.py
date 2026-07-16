#loops
#for,while,range,break,continue,pass

#for loop()
a=[10,20,30,40,50]
for i in a:
    print(i)

a=[10,20,30,40,50]
for i in a:
    print(a)

a=[10,20,30,40,50]
for i in a:
    print(i,end=",")

a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))

a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=(4,5,6,7,8,9)
for i in a:
    print(i)
print(type(a))
print(type(i))

a={4,5,6,7,8,9}
for i in a:
    print(i)
print(type(a))
print(type(i))

d={"year":2026,"month":"july","date":10}
for i in d:
    print(i)
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)

d={"year":2026,"month":"july","date":10}
for i in d:
    print(i)
for i in d.keys():
    print(i)
    print(type(d))
    print(type(i))
for i in d.values():
    print(i)
    print(type(d))
    print(type(i))
for i in d.items():
    print(i)
    print(type(d))
    print(type(i))

a="codegnan"
for i in a:
    print(i)

a=[3.4,5.6]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=["python","java","html","css"]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=[5+9j,2+10j]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=[True,False]
for i in a:
    print(i)

fruits=["apple","banana","mango"]
b=str(fruits)
print(b.upper())

fruits=["apple","banana","mango"]
for i in fruits:
    print(i.upper(),end=",")

fruits=["apple","banana","mango"]
b=[]
for i in fruits:
    b.append(i.upper())
print(b)

a=[10,20,30,40,50,"code"]
a.extend("code")
print(a)

#while loop()
a=10
while a>1:
    print(a)

a=10
while a>1:
    print(a)
    a=a-1
    
a=10
while a>=1:
    print(a)
    a=a-1

a=10
while a>1:
    a=a-1
    print(a)

a=20
while a>5:
    a=a-1
print(a)
    
a=30
while a>2:
    print(a)
    a+=1

a=30
while a>2:
    print(a)
    a-=1

a=5
while a<25:
    print(a)
    a+=1

while True:
    a=int(input("enter age:"))
    if a>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")

#range()
#start-stop-step
for i in range(10):
    print(i)

for i in range(5,15):
    print(i)
    
for i in range(30,45):
    print(i,end=",")

for i in range(2,20,2):
    print(i,end=",")

for i in range(5,50,5):
    print(i,end=",")

for i in range(0,30,3):
    print(i,end=",")

#grade code
while True:
    marks=int(input("Enter marks:"))
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif marks in range(71,81):
        print("Grade C")
    elif marks in range(50,71):
        print("Grade D")
    else:
        print("Fail")

#break
a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        break

a=30
while a>2:
    a=a-1
    if a==20:
        break
    print(a)

for i in range(40,65):
    print(i)
    if i==55:
        break

##a="python"
##if a=="h":
##    break
##print(a)#error

a="python"
for i in a:
    if i=="h":
        break
    print(i)

#continue
a=15
while a>3:
    print(a)
    a=a-1
    if a==11:
        continue

a=15
while a>3:
    a=a-1
    if a==11:
        continue
    print(a)

for i in range(18):
    if i==14:
        continue
    print(i)

a="python"
for i in a:
    if i=="t":
        continue
    print(i)

#pass
a=12
while a>4:
    print(a)
    a=a-1
    if a==10:
        pass

for i in range(25):
    if i==10:
        pass
    print(i)
