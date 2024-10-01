#####List Comprehension
####Every list conprehension  can be re-written as a for loop but every for loop cannot be re written in list comprehension
##a=[i+1 if i%2==0 else 'off' for i in range(5)]
##a=['python','codegnan','course']
##l=[]
##for i in a:
##          l.append(i.upper())
##print(l)
##          
## 
##print([i.upper() for i in a])
##
##print(str(a).upper())
##print(type(str(a).upper()))
a=['python','java','js']

print([i.capitalize() for i in a])

a=[1,2,4,6,8,12,13]
print([i*i for i in a])
print([pow(i,2) for i in a])

print([i for i in range(21) if i%2==0]) 

a=['apple','banana','grapes','mango','kiwi','berry']
print([i for i in a if 'a' not in i])

print([i**2 if i%2==0 else i*5 for i in range(16)])

a=[1,2,3,4,5]
b=[5,4,3,2,1]
print([a[i]+b[i] for i in range(len(a))])
print([a+b for a,b in zip(a,b)])

for i,j in zip(a,b):
          print(i,j)


a={1:2,3:4}
print(set(a))
