#Hammed Adeboye
#adeboye.tosin432@gmail.com
#09025491823
print ("please note that 'Use of English' in UTME represent 'English Language' in O'level ") 

#enter utme subject 0, score and grade 
Subject0= 'Use of English '
print(' subject 0 in full:',Subject0)
Score0=int (input (" Enter your Score for "+Subject0+':'))
Grade0=str(input (" Enter your grade for "+  'English Language'+':')) 
print ('proceed to the next ') 
#Ask the candidate to enter utme subject 1,score and grade 
Subject1=str (input (" Enter your Subject1 in full:")) 
Score1=int (input (" Enter your Score for "+ Subject1	+':')) 
Grade1=str(input (" Enter your grade for "+Subject1+':')) 
print ('proceed to the next  ') 
#Ask the candidate to enter utme subject 2,score and grade
Subject2=str (input (" Enter your Subject2 in full:")) 
Score2=int (input (" Enter your Score for "+ Subject2	+':'))
Grade2=str(input (" Enter your grade for "+Subject2+':'))
print ('proceed to the next  ') 
#Ask the candidate to enter utme subject 3,score and grade 
Subject3=str (input (" Enter your Subject3 in full:")) 
Score3=int (input (" Enter your Score for "+ Subject3	+':'))
Grade3=str(input (" Enter your grade for "+Subject3+':'))
print ('proceed to the next  ') 
#Ask the Candidate to enter information for the fifth O' level subject 
Subject4=str (input (" Enter your last O'level Subject in full:")) 
Grade4=str(input (" Enter your grade for "+Subject4+':'))
#Add Post Utme point
Point0=int (input (" Enter your Post Utme point out of 50:")) 
#Add the UTME scores
Sum1=sum(Score0,Score1,Score2,Score3)
print (" Your UTME score is", Sum1)
#Assign points for UTME score range 
X=range(201,250)
Y=range (251,300)
Z=range (301,350)
U=range (351,400)
A=25
B=30
C=35
D=40
if Sum1 in X:
	print ("Your UTME point is "+A) 
elif Sum1 in Y:
	print ("Your UTME point is" +B) 
elif Sum1 in Z:
	print ("Your UTME point is"+C) 
else :
	print ("Your UTME point is"+D) 
# value for each grade 
A1=5
B2=4
B3=4
C4=3
C5=3
C6=2
D7=1
'''
#Assign variable for the total grade point 
Grade=({0}+ {1}+ {2}+ {3}.format(Grade0,Grade1,Grade2,Grade3,Grade4)
#Calculation
'''