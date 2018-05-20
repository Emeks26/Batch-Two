#Name: Unufe Eloho Phone_Number: 09092448203 email_add: elohounufe@gmail.com

#This imports the random module
import random

#This defines the valid_number argument and checks if user inputted a valid int
def valid_number(s):
    if s.isdigit() and 1 <= int(s) <= 50:
        return True
    else:
        return False
	    
#This defines the Guess the number function.
def guess_the_number():
    number = random.randint(1,51)
    guessed_number = False
    guess = input("Guess a number within 1 and 50: ")
    num_guesses = 0
    while not guessed_number:
        if not valid_number(guess):
            guess = input("Please provide a valid number: ")
            continue
        else:
            num_guesses +=1
            guess = int(guess)

        if guess < number:
            guess = input("Too low. Guess Again: ")
        elif guess > number:
            guess = input("Too High. Guess Again: ")
        else:
            print("You got it in", num_guesses, "guesses!")
            guessed_number = True

    print ("Thanks for Playing.")

guess_the_number()
