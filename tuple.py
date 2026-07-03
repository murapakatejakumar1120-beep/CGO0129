Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(4,5.6,"nandhu",8+9j,True,False)
>>> print(a)
(4, 5.6, 'nandhu', (8+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> a.index(8+9j)
3
>>> a.count(True)
1
