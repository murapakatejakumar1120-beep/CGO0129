Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #sets{}
>>> a={2,4.7,"python",9+3j,True,False}
>>> a
{False, True, 2, (9+3j), 4.7, 'python'}
>>> type(a)
<class 'set'>
>>> b={1,2,3,4,3,2,1,5,6,7,8,9}
>>> b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> a={2,3,4,5,6,7,8,9}
>>> b={6,7,8,9}
>>> a.issubset(b)
False
>>> b.issubset(b)
True
>>> a={4,5,6,7,8,9}
>>> b=6,7,8,9}
SyntaxError: unmatched '}'
>>> b={6,7,8,9}
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
>>> #union()
>>> a={1,2,3,4,5,6}
>>> b={5,6,7,8,9,10}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> #intersection()
>>> a={3,4,5,6,7,8,9}
>>> b={7,8,9,10,11,12}
>>> a.intersection(b)
{8, 9, 7}
>>> #difference()
>>> a={10,11,12,13,14,15,16}
>>> b={6,7,8,12,13,14,15,16,17}
a.difference(b)
{10, 11}
b.difference(a)
{8, 17, 6, 7}
#symmetric_difference()
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference(b)
{2, 3, 4, 10, 11}
b.symmetric_difference(a)
{2, 3, 4, 10, 11}
#update()
a={1,2,3,4,5}
b={4,5,6,7,8}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}
a={1,3,5,7,8,9,10}
b={2,4,6,7,10,11,12}
a.intersection_update(b)
a
{10, 7}
b.intersection_update(a)
b
{10, 7}
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9,10}
a.difference_update(b)
a
{2, 3, 4}
b.difference_update(a)
b
{1, 5, 6, 7, 8, 9, 10}
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference_update(b)
a
{2, 3, 4, 10, 11}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
a={3,4,5,6,7,8}
a.add(10)
a
{3, 4, 5, 6, 7, 8, 10}
a.copy()
{3, 4, 5, 6, 7, 8, 10}
b=a.copy()
b
{3, 4, 5, 6, 7, 8, 10}
a.clear()
a
set()
c=set()
c.add(40)
c
{40}
a={5,6,7,8,9}
a.pop()
5
a.pop(8)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.pop(8)
TypeError: set.pop() takes no arguments (1 given)
a.remove(7)
a
{6, 8, 9}

a={2,3,4,5,6}
a.discard(4)
a
{2, 3, 5, 6}
b={4,5,6,7}
c={8,9,10,11}
b.isdisjoint(a)
False
b.isdisjoint(c)
True
a={4,5,6,7,8}
len(a)
5
a.count(7)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.count(7)
AttributeError: 'set' object has no attribute 'count'
a.index(2)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
