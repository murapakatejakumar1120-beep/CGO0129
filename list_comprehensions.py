#list comprehension
a=["codegnan","python","course"]

'''print(a.upper())

b=str(a)
print(b.upper())

for i in a:
    print(i.upper(),end=" ")

b=[]
for i in a:
    b.append(i.upper())

print(b)'''

#syntax
#a=[expr for var in collections/range]

a=[i.upper() for i in a]
print(a)

a=["vja","hyd","vzg"]
b=[i.title() for i in a]
print(b)

a=[1,2,3,5,6,8,12,13]
b=[i*i for i in a]
b=[i**2 for i in a]
b=[pow(i,2) for i in a]
print(b)

#if-usage in list comprehension

a=[i for i in range(16) if i%2==0]
print(a)

a=[i for i in range(16) if i%2!=0]
print(a)

a=[ i for i in range(21)]
print(a)

fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]
a=[i for i in fruits if "a" in i]
print(a)

# no elif usage in list comprehension

#if-else usage in list comprehension

a=[i*i if i%2==0 else i*5 for i in range(21)]
print(a)

a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
c=[a[i]+b[i] for i in range(len(a))]
print(c)
