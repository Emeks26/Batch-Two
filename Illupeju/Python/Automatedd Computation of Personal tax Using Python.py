#Ojengbede Adegboyega A.
#gboyegaojengbede@gmail.com
#08062820520
from random import randint
#Define all major lists to be used in the program such as List for Inputted names
Stored_Names=[]
Generated_Numbers=[]
list1=[]
#Create a loop to ensure the program reruns for a specific number of times (3 is used for demo)
for x in range (3):
#Within this loop, prompt the user to input the relevant info for the computation
    Name=str(input("Please Enter Full Name (Surname First): "))
    Title=str(input("Please State Your Title(Mr/Mrs/Miss): "))
    Gross_income=int(input("Please enter your gross income (yearly):N"))
#Store name input in list for future reference
    Stored_Names.append(Name)
#Define all standard rates and variables required for computation
    Tax_A=0
    Minimum_Tax=0.01*Gross_income
    Relief_1A=(0.01*Gross_income)
    Relief_1B=200000
    Relief_2=(0.2*Gross_income)
    Relief_3=(0.08*Gross_income)
    Total_Relief_A=(Relief_1A+Relief_2+Relief_3)
    Total_Relief_B=(Relief_1B+Relief_2+Relief_3)
    Minimum_Level=0.01
    First_Level=0.07
    Second_Level=0.15
    Third_Level=0.21
    Fourth_Level=0.24
    Loop_Breaker=1
#Use conditional statements to sift through the input and calculate accordingly 
    if Relief_1A>=Relief_1B:
        Taxable_Income=Gross_income - Total_Relief_A
        for i in range(1,3):
            Taxable_Income=Taxable_Income - 300000
            Tax_A=Tax_A+(First_Level*300000)
            First_Level=First_Level+0.04
        for i in range (1,3):
            Taxable_Income=Taxable_Income - 500000
            Tax_A=Tax_A+(Second_Level*500000)
            Second_Level=Second_Level+0.04  
        Taxable_Income=(Taxable_Income - 1600000)
        Tax_A=Tax_A+(Third_Level*1600000)
        Tax_A=Tax_A+(Fourth_Level*Taxable_Income)
        
    else:
        Taxable_Income=Gross_income - Total_Relief_B
        if Taxable_Income < 0:
            Tax_A=(Gross_income * Minimum_Level)        
        else:
            if Taxable_Income <= 300000:
                Tax_A=Tax_A+(First_Level*Taxable_Income)
                if Tax_A < Minimum_Tax:
                    Tax_A=Minimum_Tax
                else:
                    Tax_A=Tax_A
            else:
                while Loop_Breaker < 3 and Taxable_Income > 300000:
                    Taxable_Income=Taxable_Income-300000
                    Tax_A=Tax_A+(First_Level*300000)
                    First_Level=First_Level+0.04
                    Loop_Breaker=Loop_Breaker+1
                    if Loop_Breaker == 2 and Taxable_Income <= 300000:
                        Tax_A=Tax_A+(First_Level*Taxable_Income)
                    else:
                       Taxable_Income=Taxable_Income
                Loop_Breaker=1
                while Loop_Breaker < 3 and Taxable_Income > 500000:
                    Taxable_Income=Taxable_Income-500000
                    Tax_A=Tax_A+(Second_Level*500000)
                    Second_Level=Second_Level+0.04
                    Loop_Breaker=Loop_Breaker+1
                    if Loop_Breaker == 2 and Taxable_Income <= 300000:
                        Tax_A=Tax_A+(Second_Level*Taxable_Income)
                    else:
                        Taxable_Income=Taxable_Income
                if Taxable_Income <= 1600000:
                    Tax_A=Tax_A+(Third_Level*Taxable_Income)
                else:
                    Taxable_Income=Taxable_Income-1600000
                    Tax_A=Tax_A+(Third_Level*1600000)
                Tax_A=Tax_A+(Fourth_Level*Taxable_Income)
#Print result as the computed Tax                
    print("Dear {0} {1}, Your Gross income of N{2} Accrues a Personal Income Tax of N{3} Yearly or N{4} Monthly".format(Title,Name,Gross_income,Tax_A,round((Tax_A/12),0)))
    i=1
#Prompt user to press Return key to continue
    a=input('Press "enter" to generate Unique Tax Verificaion Code')
#Using for loop, generate a 5 digits that will constitute unique code
    for i in range(5):
        a=randint(0,9)
        list1.append(a)
        i = i+1
#Combine the first and last letters in users name with the generated digits to give unique code
    list1.insert(0,Name[0])
    list1.insert(1,Name[-1])
    #print(list1)
    b=(str(list1[0])+str(list1[1])+str(list1[2]))
    c=(str(list1[3])+str(list1[4]))
    d=(str(list1[5])+str(list1[6]))
    e=("{0}{1}{2}".format(b,c,d))
#Using conditional statement, ensure that the same code cannot be generated twice
    if e in Generated_Numbers:
        pass
    else:
        Generated_Numbers.append(e)
#Print code
        print(e)
#Restart initial loop
x=x+1
#At the end of the loop, print  the compiled lists of names and codes
print("List of User names are:{0}".format(Generated_Numbers))
print ("List of User codes are:{0}".format(Stored_Names))
