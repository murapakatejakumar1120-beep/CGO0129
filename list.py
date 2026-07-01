Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #list[]
>>> a=[3,5.6,"python",9+7j,True,False]
>>> print(a)
[3, 5.6, 'python', (9+7j), True, False]
>>> type(a)
<class 'list'>
>>> a=["python","java","c"]
>>> a.append("c++")
>>> a
['python', 'java', 'c', 'c++']
>>> a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["ml","ai"])
>>> a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
>>> #extend()
>>> a=["java","html","css"]
>>> a.extend(["js","bs"])
>>> a
['java', 'html', 'css', 'js', 'bs']
>>> #insert
>>> b=["apple","banana","grapes"]
>>> b.insert(1,"mango")
>>> b
['apple', 'mango', 'banana', 'grapes']
>>> #sort()
>>> a=["kiwi","mango","apple","dragon","berry"]
>>> a.sort()
>>> a
['apple', 'berry', 'dragon', 'kiwi', 'mango']
>>> b=[4,2,5,7,0,5,2,5]
>>> b.sort()
>>> b
[0, 2, 2, 4, 5, 5, 5, 7]
#reverse()
a=["c","java","html","css"]
a.reverse()
a
['css', 'html', 'java', 'c']
b=[1,2,3,4,5,6,7,8,9,0]
b.reverse()
b
[0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a=["black","white","red","blue","pink"]
#pop
a.pop()
'pink'
a
['black', 'white', 'red', 'blue']
a.pop(2)
'red'
a
['black', 'white', 'blue']
a.pop("white")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.pop("white")
TypeError: 'str' object cannot be interpreted as an integer
#remove()
a.remove("white")
a
['black', 'blue']
a=[1,2,3,4,5,6]
#pop()
a=["black","white","red","blue","pink"]
a=["pooja","priya","sweety","cutiee"]
a.copy()
['pooja', 'priya', 'sweety', 'cutiee']
b=a.copy()
b
['pooja', 'priya', 'sweety', 'cutiee']
a.clear()
a
[]
b
['pooja', 'priya', 'sweety', 'cutiee']
b=[]
b.append("hi")
b
['hi']
a=["hi","hello:,"how"]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["hi","hello","how"]
   
len(a)
   
3
