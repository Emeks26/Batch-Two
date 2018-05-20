#Osunjimi Ola
#olabranch@gmail.com
#07087035959

"""
A Program that manages a Multi-level parking Archade.
It displays counts of vehicle types parked along with empty lots

Presented by: OSUNJIMI, B

OBJECTIVES:
   To help manage and track  occupancy of vehicles
   To direct to open space(s) available
   To display billing system for vehicle categories

ALGORITHM FOR A MULTI-LEVEL PARKING LOT OCCUPANCY TRACKER:
Salutation
Name the parking lot
Display number of level(s) of parking lot
Display number of total spaces
Display lot occupied and spaces open for immediate occupation

CHALLENGES:
How to incorporate a Billing System
Vehicles categorization to capture heavy duty ones and possibly leave out Ground Floor or Basement  for such parking 

Parking Archade Name
"""
name=str(input("Please enter the name of the Infrasture: "))
print()
print("Welcome to",name,"Parking Archade")
print()
import math
Levels=int(input("Enter number of level on the infrastucture: "))
print()
Spaces=int(input("Enter number of space availabe on each level: "))
print()
Lots=Levels*Spaces
print("We have total",Lots,"Spaces on this facility")
print()
#Occupied lot space per level Estimation
Parked=int(input("Enter number of vehicles parked: "))
Open=Lots-Parked
print()
#print(Open)
if (Open>(Levels-1)*Spaces):
    print("We have",Open,"spaces, you are advised to use the Ground Floor")
    
elif (Open>(Levels-2)*Spaces):
    print("We have",Open,"spaces, you are advised to use the First Floor")

elif (Open>(Levels-3)*Spaces):
    print("We have",Open,"spaces, you are advised to use the Second Floor")

elif (Open>(Levels-3)*Spaces):
    print("We have",Open,"spaces, you are advised to use the Third Floor")

elif (Open>(Levels-4)*Spaces):
    print("We have",Open,"spaces, you are advised to use the Forth Floor")

elif (Open>(Levels-5)*Spaces):
    print("We have",Open,"spaces, you are advised to use the Fifth Floor")

elif (Open>(Levels-6)*Spaces):
    print("We have",Open,"spaces, you are advised to use the Sixth Floor")

elif (Open>(Levels-7)*Spaces):
    print("We have",Open,"spaces, you are advised to use the Seventh Floor")

elif (Open>(Levels-8)*Spaces):
    print("We have",Open,"spaces, you are advised to use the Eigth Floor")

elif (Open>(Levels-9)*Spaces):
    print("We have",Open,"spaces, you are advised to use the nineth Floor")
                             
else:
    print("We have",Open,"openning,use the Last Floor")
