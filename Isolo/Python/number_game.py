#Name: Adekeye Abiodun Joshua, E-mail:abiodun.adekeye0@gmail.com, Mobile: 08028366011 / 08140274860
#Guess Number Game: this project makes use of random modules to generate a number which is unknown to the user and the user is required to guess what the number is.if the user guesses wrong or right the program return some sort of indication to show that the guess is wrong or right.

from random import randint
secret_num = randint(1, 100)

for num_guesses in range(3):
    guess = eval(input('Enter your guess(1-100):  '))
    if guess<secret_num:
       print('The number is HIGHER than what you entered', 2-num_guesses, 'guesses left.\n')
    elif guess>secret_num:
       print('The number is LOWER than what you entered', 2-num_guesses, 'guesses left.\n')
    else:
       print('You got it!')
       break
       
else:
       print('You lose! The correct number is'  , secret_num)
       print('Please, try and play again')
