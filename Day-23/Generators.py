'''#generators:- A generator is also a function which can be used as an iterater (loop), by procuding group of values, where we use yield keyword.
#Yield vs Return:- Return will terminate the function whereas yield can pass the function and go on with every successive iteration.

a,b=map(int,input().split())
def gen(a,b):
    while a<b:
        yield a
        a+=1
        yield a
print(*gen(a,b))


a,b=map(int,input().split())
def gen(a,b):
    while a<b:
        a+=1
        return a
print(gen(a,b))

#yield vs return
def mygen():
    return "python","sql"
print(mygen()) # this will return the answer in tuple if need to unpack it add * in print function

def mygen():
    yield 'a'
    yield 'b'
print(*mygen())
'''  # if we don't add * in genrators it will return as classs generator without the value.

# if we want to display each output in yield in successive iteration

def mygen():
    yield 'a'
    yield 'b'
    yield 'c'
print(*mygen())
d=mygen()
#next() ->which gives successive iteration
print(next(d))
print(next(d))
print(next(d))

