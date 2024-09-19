Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#variables
a=6
a
6
A=9
B=29
b
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b
NameError: name 'b' is not defined. Did you mean: 'B'?
name="nick"
print(name)
nick
print("name")
name
#here name is given in double quotes so it is displaying name
123ns=9
SyntaxError: invalid decimal literal
#variables cant be started with numbers
a9=k
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a9=k
NameError: name 'k' is not defined
a9='k'
bksnfdk
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    bksnfdk
NameError: name 'bksnfdk' is not defined
#variable defination is not possible only direct declaration
a=3,b=8
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
#inputing multiple variables llike above is not possible ,u can do using ;
a=3;b=8

b
8
a
3
#python is cvase sensitive
print(Name)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
#orange color is keyworf
if=9
SyntaxError: invalid syntax
#variables cant be keywords
_=4
$=7
SyntaxError: invalid syntax
#only _ is valid in variable declaration no other special char is used
#space is not used in variables
a nk=9
SyntaxError: invalid syntax
''''''''''''''''''''''   operators ''''''''''''''''''
#airthmetic operators






KeyboardInterrupt
1+2
3
4-1
3
5&3
1
5/1
5.0
5//1
5
5%1
0
5**1
5


#assignment operators
a=6
b=9
c=6
a+=b
a
15
print(a+=b)
SyntaxError: invalid syntax
a-=b
a
6
a*=b
a/=b
a
6.0
a
6.0
a*=b
a
54.0
a/=b
a
6.0
a//=b
a
0.0
a=8
b=2
a//=b
a
4
a=6.0
a//=b
a
3.0
a=6
b=3.0
a//=b
a
2.0
#########################check it out############################
#comparision operaot
2>4
False
3<6
True
3>=5
False
3<=6
True
3!=6
True
3==3
True
#logical opoerators
not 2
False
2>4 not 3
SyntaxError: invalid syntax
>>> nt is unary operator
SyntaxError: invalid syntax
>>> #n0t is unary operator
>>> 2>3 and 4>5
False
>>> 2 or 5
2
>>> #identify operators
>>> a=9
>>> if a is int:
... print("int)
SyntaxError: unterminated string literal (detected at line 2)
>>> if a is int:
... print("int")
SyntaxError: expected an indented block after 'if' statement on line 1
>>> if type(a) is int:
...     print("int")
... else:
...     print("not int")
... 
int
>>> if a is int:
...     print("int")
... else:
...     print("not int")
... 
...     
not int
>>> a is not int
True
>>> #membership operators
>>> a in 'vyshnavi'
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a in 'vyshnavi'
TypeError: 'in <string>' requires string as left operand, not int
>>> 'a' in 'vyshnavi'
True
