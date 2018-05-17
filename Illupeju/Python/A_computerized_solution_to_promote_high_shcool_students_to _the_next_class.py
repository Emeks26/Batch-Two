# Adelanke Ologbenla
# lanky404@yahoo.computerized
# 08083297281


"""
Project Title: A computerized solution to promote high shcool students to the next level/class
Alogrithm: Collect the student information e.g full name
	   Collect the score of the student
	   Assign grades for scores
	   Award results to student
i.e.
Enter Student name
Enter Student score
score
Distinction>80
Very Good<80>59
Pass<60>40
Fail<40
"""

student=input("Enter name of Student")
score=int(input("Enter student score"))
if (score>=80):
    print("Distinction")
elif(score<80) and (score>=59):
    print("Very Good")
elif(score<60) and (score>=40):
    print("Pass")
else:
    print("fail")
"""   
Challenge:I have issues with some of the functions because it keeps popping out invalid syntax and all I do is go back to the program and fix the challenge and repeatedly until I get the right function to use.

Suggestion: I will like to reduce my if statement in order to get the right output timely, and also study the loop functions.

DEMO: As seen 
"""