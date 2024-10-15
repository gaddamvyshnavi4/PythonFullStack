#global and local variables
'''

A variable inside and outside the function is called global and local variables

A variable define above the function and is accessible to the entire global space is called a global variable

A variable inside the function is called local variable



'''
#first case of global variable
'''
a=5
def check():
          print('inside the function',a)
check()
print('outside the function',a)

'''
#second case of global variable
'''
def check():
          a=6
          print('inside the function',a**2)
check()
print('outside the function',a)
'''
#third case of both global and local variables
'''
a,b=2,4
def check():
          a=4
          print('inside the function',a)
          a=8
          print('inside the function',a+6)
          b=8+a
          print('value of b'.b)
check()
print('outside the function a is',a)
print('outside the function b is',b)
'''
#usage of global keyword
'''
when user wants to access the global variable inside the function deirectly and
carry forward the updated value even outside the function  the we need to use global keyword  
'''
#fourth case of global and local variable
'''
a=5
def check():
          #global a,b
          global a
          print('inside value is',a)
          a=7
          print('updated value is ',a)
          global b
          b=12
          b+=a
          print('value of b is',b)
check()
print('outside function a is ',a)
print('outside function b is',b)
'''

#generators
'''
no tuple comprehension in above cases if we remove those braces and keep paranthesis then the outcome is generator

'''
'''
a=[i**3 for i in range(9)]
print(a)
'''

a=(i**6 for i in range(4))

'''print(a)
print(type(a))
print(*a)'''

#can also access with data types
print(list(a))
a=(i**6 for i in range(4))
print(tuple(a))
a=(i**6 for i in range(4))
print(set(a))
a=(i**6 for i in range(4))
print(dict(a))#error
