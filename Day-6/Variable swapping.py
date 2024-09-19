#swapping of 2 variables
'''
a=5
b=6
print("before swap:",a,b)
a,b=b,a
print("after swapping",a,b)

#using extra variable
print("before swap:",a,b)
temp=a
a=b
b=temp
print("after swapping",a,b)

#using airthmetic variables
print("before swap:",a,b)
a=a+b
b=a-b
a=a-b
print("after swapping",a,b)
print("after swapping a=%d b=%d" %(a,b))
print("after swapping a=%2d b=%3d" %(a,b))
print("after swapping a=%02d b=%03d" %(a,b))


'''
#float swapping
'''
a=5.7
b=6.9
print("before swap:",a,b)
a,b=b,a

print("after swapping",a,b)
print("after swapping a=%f b=%f" %(a,b))
print("after swapping a=%0.2f b=%0.1f" %(a,b))

print("after swapping a=%06.2f b=%0.1f" %(a,b))
'''


#string swapping
'''
a='ok'
b='hi'
print("before swap:",a,b)
a,b=b,a

print("after swapping",a,b)
print("after swapping a=%s b=%s" %(a,b))
'''
#swapping with run time input
'''

a=float(input())
b=float(input())
print("before swap:",a,b)
a,b=b,a

print("after swapping",a,b)
print("after swapping a=%f b=%f" %(a,b))
print("after swapping a=%0.2f b=%0.1f" %(a,b))

print("after swapping a=%06.2f b=%0.1f" %(a,b))

a=int(input())
b=int(input())
print("before swap:",a,b)
a,b=b,a

print("after swapping",a,b)
print("after swapping a=%f b=%f" %(a,b))
print("after swapping a=%0.2f b=%0.1f" %(a,b))

print("after swapping a=%06.2f b=%0.1f" %(a,b))

a=str(input())
b=str(input())
print("before swap:",a,b)
a,b=b,a

print("after swapping",a,b)
print("after swapping a=%f b=%f" %(a,b))
print("after swapping a=%0.2f b=%0.1f" %(a,b))

print("after swapping a=%06.2f b=%0.1f" %(a,b))

'''
f_name=input()
l_name=input()
c=f_name+" "+l_name

print(f"{c.title()}")
print("{}".format((f_name+" "+l_name).title()))
print(f"{f_name,l_name}")
print("{} {}".format(f_name,l_name).title())
#u get error when u use "" all the time u have to so that the compiler doesn't get conflicted between "," like shown below
print(f' {(f_name+" "+l_name).title()}')
print(f"My name is {f_name} {l_name}".title())
