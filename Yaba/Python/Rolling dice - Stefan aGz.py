#Agoziem Daniel 07064703005
import random 
import time
 
def castDie():
 
   value = int(input('Press Enter to cast the die!'))
   r = list(range(1, 7))
   comp_random = int(random.choice(r))
   if value == comp_random :
      return True
   print('Result: ',comp_random)
 
 
while True:
   time.sleep(1)
   castDie()
   if(castDie()):
      break
