#This is MY SHOP APPLICATION designed with python 

print("WELCOME TO MY SHOP \n")

print("please select the following options \n1.Apple \n2.Banana \n3.Mango \n4.Coconut")
      
option=int(input("Enter an option \n"))

if option == 1:
      print("we have 8 apples at the rate of N100 per unit")
      n=int(input("how many apples do you care for \n"))
      if n <=8:
            print ('The cost of', n , 'apples is' , n*100 , 'Naira')
      if n >= 9 :
            print("number of available apples exceeded")

elif option== 2:
      print("we have 10 bunches of banana at the rate of N300 per bunch")
      n =int(input("how many bunches do you care for \n"))
      if n <=10:
            print ('The cost of', n , "bunches is" , n*300 , "Naira")
      elif n >= 11 :
            print("number of available bunches exceeded")
      
elif option== 3:
      print("we have 6 mangoes at the rate of N50 per unit")
      n =int(input("how many mangoes do you care for \n"))
      if n <=6:
            print ('The cost of',n,'mangoes is'  ,n*50,'Naira')
      elif n >= 7 :
            print("number of available mangoes exceeded")
            
elif option== 4:
      print("we have 12 Coconuts at the rate of N150 per unit")
      n=int(input("how many Coconuts do you care for \n"))
      if n<=12:
            print ('The cost of',n,'Coconuts is'  ,n*150,'Naira')
      elif n >= 13 :
            print("number of available Coconuts exceeded")

else:
      print("Enter a valid option")

      




            
