""" Program Nmae: Multiplication Game for Kids
    Author: James Boluwatife
    E-mail: jamesbolu774@gmail.com
    Number: 09023494629
    Description: The program is built on the main aim of improving calculation skills for kids, it provides a multiplication question and request for an answer
"""
from random import randint
print('Welcome to the Multiplication game for kids')
print('You have Ten multiplication questions to be answered, Once you have answer all the questions your score will be shown to you') 
right = 0
wrong = 0
def multiplication():
    global right
    global wrong
    num1 = randint(1,5)
    num2 = randint(1,5)
    print('Question',1+i,':' ,num1,'x',num2)
    ans = eval(input('Answer = ') )
    if ans==num1*num2:
        print('Right!')
        right = right +1
    else:
        print('Wrong!')
        wrong = wrong + 1
    
for i in range(10):
    multiplication()
print('you scored', right, 'questions correctly and you were wrong in', wrong, 'questions')
