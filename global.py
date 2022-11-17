def foo():
    x=20

    def bar():
        global x
        x=25
        x="rama"
        print("x value in bar is:",x)
        

    print("before calling bar x value is:",x)
    print("now calling bar")
    bar()   

    print("after calling bar x value is :",x) 



foo()    

print ("x in main is:",x)