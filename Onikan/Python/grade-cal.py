#input your score
x=int(input("what is your score"))
#check your grade
#and/or are used for comparism
#70-100:A
#69-60:B
#59-50:C
#49-45:D
#44-40:E
#39-0:F
if(x>=70 and x<=100):
   print("you scored an A")
elif(x>=60 and x<=69):
    print("you scored a B")
elif(x>=50 and x<=59):
    print("you scored a C")
elif(x>=45 and x<=49):
    print("you scored a D")
elif(x>=40 and x<=44):
    print("you scored an E")
elif (x>=0 and x<=39):
    print("you scored an F")
else:
    print("please go and read")




