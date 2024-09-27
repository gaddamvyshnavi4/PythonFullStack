#multiple if statements
'''
a=4
b=5
if a>b:
          print('greater')
if a<b:
          print('lesser')
if a==b:
          print('equal')

if a>b:
          print('greater')
elif a<b:
          print('lesser')
elif a==b:
          print('equal')



          
if a>b:
          print('greater')
if b<a:
          print('lesser')
if a!=b:
          print(' not equal')


a,b=b,a      
if a>b:
          print('greater')
elif b<a:
          print('lesser')
elif a!=b:
          print(' not equal')
#nested if


if a>b:
          print('grater')
          if a!=b:
                    print('not equal')



if a<b:
          print('grater')
          if a!=b:
                    print('not equal')



if a>b:
          print('greater')
          if a!=b:
                    print('not equal')
else:
          print("invalis")



#voting
age=int(input())
if age>=20:
          print('eligible for voting')
else:
          print('not eligible for voting')

#even or odd
number=int(input())
if number%2==0:
          print('even')
else:
          print('odd')



#guest code
name=input()
if name=="vyshnavi":
          print('welcome',name)
else:
          print('welcome guest')

'''

#leap year
year=int(input())
if year%4==0 or year%400==0 and year%100==0:
          print('leap year')
          
else:
          print('not leap year')
 
