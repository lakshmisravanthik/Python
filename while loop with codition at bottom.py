# Loop with Condition at bottom 
# Roll a dice until user choose to exit

# import random module
import random 
count=0

while True:
    input("Press Enter to Roll the Dice :")

    num=random.randint(1,8)

    print ("got number is ",num)

    count=count+1 

    option=input("Roll the dice again select y/n :\n")

    
    if option =='n':
     
     print("stop dice  to roll")
     print(" Dice is rolled  ",count ,"times") 
     break


  

