l=[1,2,3]
#print(max(l),min(l),sum(l),type(l),range(5),len(l),input('enter a value:'))
for i in range(65,91):
          print(chr(i),end=" ")
#['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
dir()
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'''

dir('__builtins__')
print(dir())
print(dir('__builtins__'))

#fromkeys()
a='vyshnavi'
print(a)
print(list(a))
print(tuple(a))
print(set(a))
b=dict.fromkeys(a)
print(b)
b=dict.fromkeys(a,'ok')
print(b)
b['v']='vyshavi'
print(b)


#takes any type of data eval()


#eval()

'''
while True:
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)'''

'''
while True:
    a=float(input("a value:"))
    b=float(input("b value:"))
    print(a+b)'''

'''
while True:
    a=input("data1:")
    b=input("data2:")
    print(a+b)'''

'''
while True:
    a=complex(input("a value:"))
    b=complex(input("b value:"))
    print(a+b)'''

while True:
    a=eval(input("a value:"))
    b=eval(input("b value:"))
    print(a+b)
