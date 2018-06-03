#Olaoluwa Arijenuga 08144281071
Name=str(input("Enter Name:"))
Department=str(input("Enter Department"))
    
a=0
while a<10:
      
    subject=str(input("Enter Subject:"))
    score=int(input("Enter score:"))
    
    if score>=0 and score<30:
        print("F9")
        print("You Failed")

    elif score>29 and score<40:
        print("E8")
        print("You Failed")

    elif score>39 and score <45:
        print("D7")
        print("You Failed")

    elif score>44 and score<50:
        print ("C6")
        print("You Passed")
        
    elif score>49 and score<55:
        print("C5")
        print("You Passed")
        
    elif score>54 and score<60:
        print ("C4")
        print("You Passed")
        
    elif score>59 and score<64:
        print("B3")
        print("You Passed")
        
    elif score>64 and score<70:
        print("B2")
        print("You Passed")
        
    elif score>69 and score<101:
        print("A1")
        print("You Passed")
    else:
        print("invalid score"+", "+"try again")

        a+=1
    
