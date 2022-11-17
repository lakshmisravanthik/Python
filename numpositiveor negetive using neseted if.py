# print is positive, negetive or zero using nested if


num=input("Ënter value\n")
          
x=int(num)

if(x>=0):
   if(x>0):
       print(x,"is positive number")
   else:
          print(x,"is zero number") 
else:
     print(x,"is negetive number")