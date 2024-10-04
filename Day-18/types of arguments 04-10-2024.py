#keyword arguments
'''def check1(id,name,emailid):
    id=34
    name="mounika"
    emailid="mouni@gmail.com"
    print(id,name,emailid)
check1(id="id",name="name",emailid="emailid")'''

'''def check2(id,name,emailid):
    print(id,name,emailid)
check2(id=45,name="shanmukhi",emailid="shan@gmail.com")
check2(34,"bhavana","bana@gmail.com")
check2("koushi@gmail.com","koushik",75)
check2(name="anusha",id=55,emailid="an@gmail.com")'''

#example
def employe(name,salary,designation):
    '''name="mounika"
    salary=30000
    designation="java developer"
    print(name,salary,designation)
employe(name="name",salary="salary",designation="designation")
    print(name,salary,designation)
employe(name="roja",salary=34000,designation="research and development")
employe("python developer","anu",29000)
employe(name="kosuhik",designation="senoir mech",salary=34000)'''


#default arguments
'''def grocery(item,price):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery("bread",25)'''

'''def grocery(item="toor daal",price=55):
    print("item is %s"%item)
    print("price is %d"%price)
grocery()'''

'''def grocery(item,price=45):
    print("item is %s"%item)
    print("price is %d"%price)
grocery("makhana"''')

'''def grocery(item="oil",price):'''#####raises error as the first argument must be non-default argument or both must be non default
    '''print("item is %s"%item)
    print("price is %d"%price)
grocery(price)'''
