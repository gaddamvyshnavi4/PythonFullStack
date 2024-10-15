
#kwargs()

'''def check(**a):
    print(a)
    print(type(a))
check()
d={"names":["mounika","shanmukhi","bhavana"],
   "status":["P","A","P"]}
check(**d)'''

##def check1(**a):
##    print(a)
##    print(type(a))
##    for i in a.items():
##              print(i)
##    for i in a:
##        print(i,a[i])
##check1()
##e={"names":["mounika","shanny","bana"],
##   "idnos":[10,20,30]}
##check1(**e)
##

#both *  , ** usage

def final(*a,**b):
          for i in a:
                    print(i)
          for i,j in b.items():
                    print(i,j)

final()

a=(1,2,7,75)
final(*a)
b={'1':2,'3':4,'5':6}
#final(**b)
final(*a,b)
final(*a,**b)
