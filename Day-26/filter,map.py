#filter

a=[10,15,20,25,30,40,50,60,70,80,90,100]
b=list(filter(lambda c: c%2==0,a))
print(b)

a=[[],(),set(),{},None,' ','string',1,2.7,5+0j,True,False]
b=list(filter(None,a))
print(b)

a=[[],(),set(),{},None,' ','string',1,2.7,5+0j,True,False]
b=list(filter(lambda a:type(a)==list,a))
print(b)

#map -> each object from a collection and form a new collection

a=[1,2,3,4,5,6]
b=[6,3,8,2,9,9]
b=list(map(max,a,b))
print(b)


#uneven list

a=[1,2,3,4,5,6,7]
b=[6,3,8,2,9,9]
b=list(map(max,a,b))
print(b)


a = [1, 2, 3, 4, 5, 6]
b = [6, 3, 8, 2, 9, 9]
b = list(map(lambda x, y: x + y, a, b))

a=[1,2,3,4,5,6]
b=[6,3,8,2,9,9]
b=list(map(min,a,b))
print(b)
'''

a=[1,2,3,4,5,6]
b=[6,3,8,2,9,9]
b=list(map(sum,a,b))#error
print(b)
'''


a=input('data1')
b=input('data2')
print(a+b)



a,b=[x for x in input('enter the data').split(',')]
print(a+b)

a,b=input('enter names with ,').split(',')
print(a+b)

a=int(input('a value'))
b=int(input('b value'))
print(a+b)



a,b=int(input('enter the values')).split(',')
print(a+b)#error

        
a,b=map(int,input('enter the values').split(' '))
print(a,b)
print(a+b)

