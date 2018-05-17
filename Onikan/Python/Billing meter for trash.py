#This project is by Bakare Hamaamah;hamaamahbakare@gmail.com
#Its trash pickup day
#Billing meter for trash dropped per household in residence B
#Residence B consists of 5 blocks
#tax rate for each block is as follows below
#block 1=51 naira
#block 2=48 naira
#block 3=35 naira
#block 4=22 naira
#block 5=17 naira
print("please weigh your trash\n")
block=int(input("choose your block number:\n1.Block 1\n2.Block 2 \n3.Block 3 \n4.Block 4 \n5.Block 5 \n"))
if(block==1):
   weight=float(input("please enter the weight of trash"))
   tax=int(input("input the standard trash tax of this block"))
   bill= weight * tax
   print("your total bill is",bill,"naira")

elif(block==2):
   weight=float(input("please enter the weight of trash"))
   tax=int(input("input the standard trash tax of this block"))
   bill= weight * tax
   print("your total bill is",bill,"naira")
   
elif(block==3):
   weight=float(input("please enter the weight of trash"))
   tax=int(input("input the standard trash tax of this block"))
   bill= weight * tax
   print("your total bill is",bill,"naira")

elif(block==4):
   weight=float(input("please enter the weight of trash"))
   tax=int(input("input the standard trash tax of this block"))
   bill= weight * tax
   print("your total bill is",bill,"naira")

elif(block==5):
   weight=float(input("please enter the weight of trash"))
   tax=int(input("input the standard trash tax of this block"))
   bill= weight * tax
   print("your total bill is",bill,"naira")

else:
    print("you are not on this block")
