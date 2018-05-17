#Obi Chukwudumebi
#dumebiobi08@gmail.com
#07010765543
"""
FIRE,LOGS,WATER!!!!
for player,
    FIRE=f
    LOGS=l
    WATER=w
for computer,
    FIRE=1
    LOGS=2
    WATER=3
PLAYER VS COMPUTER: lets see who wins!
rules of the game:
1) fire burns logs
2) water puts out the fire
3) logs makes a bridge over the water
"""

from random import randint
player=str(input("fire(f),logs(l) or water(w)"))
print(player)
computer=randint(1,3)
if(computer==1):
    computer_choice='f'
elif(computer==2):
    computer_choice='l'
else:
    computer_choice='w'
print(computer_choice)
print("Therefore we have,{0} vs {1}".format(player,computer_choice))
if(player=='l')and(computer_choice=='w'):
    print("PLAYER WINS")
elif(player=='w')and(computer_choice=='l'):
    print("COMPUTER WINS")
elif(player=='f')and(computer_choice=='w'):
    print("COMPUTER WINS")
elif(player=='w')and(computer_choice=='f'):
    print("PLAYER WINS")
elif(player=='f')and(computer_choice=='l'):
    print("PLAYER WINS")
elif(player=='l')and(computer_choice=='f'):
    print("COMPUTER WINS")
elif(player==computer_choice):
    print("DRAW")
