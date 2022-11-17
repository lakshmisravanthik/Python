

def add():
    a=20
    print ("a value in local is : ", a+3)
    
    def mult():
        nonlocal a
        print("a value is :",a*2)
        print("a value is :",a*100) 

    mult()
    print("a value is :",a)

       





add()

