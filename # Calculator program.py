#  Calculator program

def add(x,y):
   
   return x+y

def sub(x,y):

    return x-y   

def mul(x,y):

    return x*y

def div(x,y) :

    return(x/y)


print("Select the Operation :")

print ("1.Addition")
print ("2.Subtraction")
print ("3.Multiplication")
print ("4. Division")

while True:

  print("Take input from the User ")
  choice=input("Enter any Number 1/2/3/4")

  num1=float(input("Enter First number"))
  num2=float(input("Enter second number"))

  if choice in ('1','2','3','4'):

    if choice=='1':

         print(num1 ,"+",num2 ,"=",add(num1,num2))
        
    elif choice=='2':
         print(num1 ,"-",num2 ,"=",sub(num1,num2))
         
    elif choice=='3':
         print(num1 ,"*",num2 ,"=",mul(num1,num2))

    elif choice=='4':
        print(num1 ,"/",num2 ,"=",div(num1,num2))

    next_calculation=input("Lets do next calculTION YES/NO")

    if next_calculation=="NO":

        break
  else:

     print ("INVALID INPUT")
       
        

         
          











     


    