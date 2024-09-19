Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple()
#tuple is immutable
a=(1,5.6,2+9j,'ok',True)
print(a)
(1, 5.6, (2+9j), 'ok', True)
type(a)
<class 'tuple'>
a.index(1)
0
a.count(True)
2
a.count(1)
2
a.count(5.6)
1
#set{}
#set is unordered
a={5,8.9,"vyshnavi",2+9j,True}
print(a)
{True, 5, 8.9, 'vyshnavi', (2+9j)}
a={1,6,2,9}
a
{1, 2, 6, 9}
#remooves duplicate values
type(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(b)
NameError: name 'b' is not defined
type(a)
<class 'set'>
#semi mutable / mutable
a={True,1}
a
{True}
a={1,True}
a
{1}
#add()
a={1,2,7,4,9}
a
{1, 2, 4, 7, 9}
a
{1, 2, 4, 7, 9}
a.add(20)
a
{1, 2, 4, 20, 7, 9}
#issubset()
b={1,2,9}
a.issubset(a)
True
b.issubset(a)
True
a.issubset(b)
False
a.issuperset(a)
True
c=b
b.issuperset(c)
True
c.issuperset(b)
True
a.issuperset(b)
True
b.issuperset(a)
False
a.union(b)
{1, 2, 4, 7, 9, 20}
a={1,2}
b={3,4}
a.union(b)
{1, 2, 3, 4}
a
{1, 2}
b
{3, 4}
a.intersection(b)
set()
a={1,2}
{1,2}.intersection({1,5})
{1}
x={1,2}.intersection({1,5})
x
{1}
{1,2}.update({1,5})
a.update(b)
a
{1, 2, 3, 4}
x=a.update(b)
x
x
type(x)
<class 'NoneType'>
b
{3, 4}
(5,6,7}.difference({16,60})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
{5,6,7}.difference({16,60})
{5, 6, 7}
{6,16}.difference({16,60})
{6}
{1,2,3}.difference({4,5,6})
{1, 2, 3}
{1,2,3}.difference({1,4,5,6})
{2, 3}
{2,4,6,8,10}.symmetric_difference({3,4,5,6,7,8,9})
{2, 3, 5, 7, 9, 10}
#which is union - intersection
{1,2,3,4}.difference_update({4,5})
x={1,2,3,4}.difference_update({4,5})
x
a={1,2,3,4}
b={4,5}
a.difference_update(b)
a
{1, 2, 3}
#symmetric diff is same for both
a={5,6,7,8,9}
b={1,2,3,4,5,6}

a.symmetric_difference_update(b)
a
{1, 2, 3, 4, 7, 8, 9}
b.symmetric_difference_update(a)
#generally a.symmetric_difference(b) b.symmetric_difference(a)  values are same
#but symmetricupdate is different because a is updated in a.symmetric_difference_update(b)
a
{1, 2, 3, 4, 7, 8, 9}
>>> a.pop()
1
>>> #in set first element is poped
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.remove(5)
KeyError: 5
>>> a.remove(7)
>>> a
{2, 3, 4, 8, 9}
>>> #if value in remove doesn't contain in list it gets error
>>> a.discard(9)
>>> a
{2, 3, 4, 8}
>>> a.discard(1)
>>> a
{2, 3, 4, 8}
>>> #discard doesn't give error
>>> b=a.copy()
>>> b
{8, 2, 3, 4}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> a.add(3)
>>> a
{3}
>>> {1,2,3}.disjoint({5,6})
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    {1,2,3}.disjoint({5,6})
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> {1,2,3}.isdisjoint({5,6})
True
>>> {1,2,3}.isdisjoint({1,5,6})
False
>>> #disjoint does not contain common elements
