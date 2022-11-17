def addition():

    return   lambda a,b:a+b

ex=addition()   

print(ex(1,2))


def mul(n):
    return  lambda a,b,c: (a+b+c) * n

ans=mul(3)  

print(ans(10,20,30))

def f1():
    
     return lambda a,b: print(f"first name is {a},and last name is {b} then full name is {a}{b}")
ans1=f1()

print(ans1("rama","sita"))

##lamda using set

list=[1,2,3,4,5,6,7,8,9,10]

newlist=list(filter(lambda x:x*2) ,list)

print(newlist)




        