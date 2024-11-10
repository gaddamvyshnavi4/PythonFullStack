a=[]
print(type(a))
a=()
print(type(a))
a={}
print(type(a))
a=set()
print(type(a))
#zip->combine multiple collections into one collection

a=[1,2,3]
b=[4,5,6]
c=zip(a,b)
print(list(c))
#prints empty
print(dict(c))
print(set(c))
print(tuple(c))


print(dict(zip(a,b)))
print(set(zip(a,b)))
print(tuple(zip(a,b)))

a=['1','2','3','4','5']
   


#enumerate() ->we can give counter to the colection
for i,j in enumerate(a):
          print(i,j)
          
          
b=dict(enumerate(a,11))
print(b)


#anonymous functions are nameless functions we use a keyword called as lambda to create anonymous functions



a=lambda x:2*x+5
print(a(5))


sum=lambda x,y:x+y
print(sum(4,5))


s=lambda x:x.upper()
print(s('codegnan'))


name=lambda f,l:(f+" "+l).title()
print(name('vyshnavi','gaddam'))
