# Leap year program
while True:
  year= input("enter year\n")
  y=int(year)

  if (y %4==0) and (y%100==0)  and (y%400==0) :
    print(f"{year} is leap year1")

  elif (y%4==0) and (y%100==0) and (y%400!=0):

        print(f"{year} is  not leap year2")

  elif (y%4==0) and (y%100!=0) and (y%400!=0):

          print(f"{year} is   leap year3") 
  else :

          print(f"{year} is  not leap year4")   
    
  

    
    
  

  

      
   
