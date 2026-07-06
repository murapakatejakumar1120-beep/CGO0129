Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"nandhu","year":2026,"month":6}
a
{'name': 'nandhu', 'year': 2026, 'month': 6}
type(a)
<class 'dict'>
b={"name","nandhu"}
b
{'nandhu', 'name'}
type(b)
<class 'set'>
a={"year":2026,"month":"july","date":4}
a.update({"time":7})
a
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7}
a.update({"name":"pooja"},{"city":"vja"})
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.update({"name":"pooja"},{"city":"vja"})
TypeError: update expected at most 1 argument, got 2
a.update({"name":"pooja","city":"vja"})
a
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7, 'name': 'pooja', 'city': 'vja'}
#setdefault()
a={"course":"python"}
a.setdefault("duration",4)
4
a
{'course': 'python', 'duration': 4}
a={"color":"black","food":"biryani","icecream":"nuts"}
a
{'color': 'black', 'food': 'biryani', 'icecream': 'nuts'}
a["color"]
'black'
a["black"]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a["black"]
KeyError: 'black'
a.get("food")
'biryani'
a
{'color': 'black', 'food': 'biryani', 'icecream': 'nuts'}
a.get("biryani")
a
{'color': 'black', 'food': 'biryani', 'icecream': 'nuts'}
a={"month":7,"day":"sat","time":7}
a
{'month': 7, 'day': 'sat', 'time': 7}
a.keys
<built-in method keys of dict object at 0x00000231BB19D840>
a.keys()
dict_keys(['month', 'day', 'time'])
a.values()
dict_values([7, 'sat', 7])
a.items()
dict_items([('month', 7), ('day', 'sat'), ('time', 7)])
a={"city":"vja","country":"india","state":"ap"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("city")
'vja'
a
{'country': 'india', 'state': 'ap'}
a.popitem()
('state', 'ap')
a
{'country': 'india'}
>>> a={"name":"nandhu","mail":"nandhu@gmail.com"}
>>> len(a)
2
>>> a.copy()
{'name': 'nandhu', 'mail': 'nandhu@gmail.com'}
>>> a
{'name': 'nandhu', 'mail': 'nandhu@gmail.com'}
>>> a.clear()
>>> a
{}
>>> a={"name":"nandhu","year":"2026","name":"nandhu"}
>>> a
{'name': 'nandhu', 'year': '2026'}
>>> a={"name":"nandhu","year":"2026","name":"chocky"}
>>> a
{'name': 'chocky', 'year': '2026'}
>>> a={"idnos":[10,20,30],"names":["a","b","c"],"marks":[60,70,80]}
>>> a
{'idnos': [10, 20, 30], 'names': ['a', 'b', 'c'], 'marks': [60, 70, 80]}
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['a', 'b', 'c'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['a', 'b', 'c']), ('marks', [60, 70, 80])])
>>> a={"year":2026,"month":7}
>>> a.count("year")
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.count("year")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("month")
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.index("month")
AttributeError: 'dict' object has no attribute 'index'
