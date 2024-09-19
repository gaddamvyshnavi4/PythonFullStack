Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dictionary{}
a={"name":"pooja","place":"guntur"}
type(a)
<class 'dict'>
#accessing item
a["name"]
'pooja'
a.keys()
dict_keys(['name', 'place'])
keys=a.keys()
keys
dict_keys(['name', 'place'])
#values()
a.values()
dict_values(['pooja', 'guntur'])
a.items()
dict_items([('name', 'pooja'), ('place', 'guntur')])
#accessing items
a={"year":2003}
a={"year":2003,}
#to add elements
a.update({"month":"september"})
a
{'year': 2003, 'month': 'september'}
a.update({1:2},{3:4})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.update({1:2},{3:4})
TypeError: update expected at most 1 argument, got 2
a.update({1:2,3:4})
a
{'year': 2003, 'month': 'september', 1: 2, 3: 4}
a.setdefault(9,8)
8
a
{'year': 2003, 'month': 'september', 1: 2, 3: 4, 9: 8}
#it returns value
a.setdefault(7)
a
{'year': 2003, 'month': 'september', 1: 2, 3: 4, 9: 8, 7: None}
a.setdefault()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.setdefault()
TypeError: setdefault expected at least 1 argument, got 0
a.copy()
{'year': 2003, 'month': 'september', 1: 2, 3: 4, 9: 8, 7: None}
a.pop()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.pop(2)
KeyError: 2
a.pop(1)
2
a.setdefault(7:9)
SyntaxError: invalid syntax
a.popitem()
(7, None)
a.popitem(1:2)
SyntaxError: invalid syntax
a.popitem({1:2))
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a.popitem({1:2})
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.popitem({1:2})
TypeError: dict.popitem() takes no arguments (1 given)
a.get('year')
2003
a
{'year': 2003, 'month': 'september', 3: 4, 9: 8}
a.clear()
a
{}
b={'numbers':[7,8,9,1]}
#duplicates are accepted in set , dict
#no count fun for both
a.update({"year":2024})
a
{'year': 2024}
a.update({"year":2003})
a
{'year': 2003}
a.count()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
a=[1,2,3,4]
type(a)
<class 'list'>
b=set(a)
type(b)
<class 'set'>
b=tuple(a)
type(b)
<class 'tuple'>
b=dict(a)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    b=dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
a=(1,2)
b=list(a)
type
<class 'type'>
type(b)
<class 'list'>
b=set(a)
type(b)
<class 'set'>
a={1:2}
b=list(a)
b
[1]
b=set(a)
b
{1}
b=tuple(a)
b
(1,)
#list
a=[1,2,4,2.5,2j,True,'hey']
type(a)
<class 'list'>
c=9
type(c)
<class 'int'>
c=[2]
type(c)
<class 'list'>
a.append('hi')
a
[1, 2, 4, 2.5, 2j, True, 'hey', 'hi']
a.append('hi',9)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.append('hi',9)
TypeError: list.append() takes exactly one argument (2 given)
a.extend('hi',9)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.extend('hi',9)
TypeError: list.extend() takes exactly one argument (2 given)
a.append(('hi',9))
a
[1, 2, 4, 2.5, 2j, True, 'hey', 'hi', ('hi', 9)]
a.extend(('hi',9))
a
[1, 2, 4, 2.5, 2j, True, 'hey', 'hi', ('hi', 9), 'hi', 9]
a.insert(1,"python")
a
[1, 'python', 2, 4, 2.5, 2j, True, 'hey', 'hi', ('hi', 9), 'hi', 9]
a.insert(6,"python")
a
[1, 'python', 2, 4, 2.5, 2j, 'python', True, 'hey', 'hi', ('hi', 9), 'hi', 9]
a.copy()
[1, 'python', 2, 4, 2.5, 2j, 'python', True, 'hey', 'hi', ('hi', 9), 'hi', 9]
b=a.copy()
b
[1, 'python', 2, 4, 2.5, 2j, 'python', True, 'hey', 'hi', ('hi', 9), 'hi', 9]
a.remove('python')
a
[1, 2, 4, 2.5, 2j, 'python', True, 'hey', 'hi', ('hi', 9), 'hi', 9]
#remove deletes first apperaed python
a.pop()
9
#deletes last element
a.pop(1)
2
#it takes index
a.pop("python")
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.pop("python")
TypeError: 'str' object cannot be interpreted as an integer
#given value
a.sort()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'complex' and 'float'
list=[1,2,45,]
list.sort()
list
[1, 2, 45]
a.reverse()
a
['hi', ('hi', 9), 'hi', 'hey', True, 'python', 2j, 4, 2.5, 1]
a.sort(revefrse=True)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.sort(revefrse=True)
TypeError: 'revefrse' is an invalid keyword argument for sort()
a.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a.sort(reverse=True)
TypeError: '<' not supported between instances of 'complex' and 'int'
list.sort(reverse=True)
#sorts descending order
list=[1,2,45,5]
list.sort()
list
[1, 2, 5, 45]
list.sort(reverse=True)
list
[45, 5, 2, 1]
a.index(20)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.index(20)
ValueError: 20 is not in list
#takes values and gives index
a.index(1)
4
a
['hi', ('hi', 9), 'hi', 'hey', True, 'python', 2j, 4, 2.5, 1]
#True is considered as 1
>>> a=[1,2,2,1]
>>> a.count(1)
2
>>> a.count(9)
0
>>> len(a)
4
>>> a.clear()
>>> a
[]
>>> a=[9,1,5,8,9,6]
>>> #o/p [1,5,9,6,8,9]
>>> a=a[:3].sort()+a[3:].sort()
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a=a[:3].sort()+a[3:].sort()
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
>>> a1=a[:3]
>>> a2=a[3:]
>>> a1.sort();a2.sort()
>>> a=a1+a2
>>> a
[1, 5, 9, 6, 8, 9]
>>> a[:3]
[1, 5, 9]
>>> a[:3].sort
<built-in method sort of list object at 0x0000021637553DC0>
>>> a[:3].sort()
>>> a=[a[:3].sort()]+[a[3:].sort()]
>>> a
[None, None]
>>> c=a[:3].sort()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    c=a[:3].sort()
TypeError: '<' not supported between instances of 'NoneType' and 'NoneType'
>>> a=[9,1,5,8,9,6]
>>> c=a[:3].sort()
>>> c
