#Name:Emmanuel Chinonso Royce; E-mail:emmanuelroyce850@gmail.com; phone number:08161705790.
'''This code program is a guessing game. It uses the python while loop to run the game program, so it continues running until the user guesses the correct answer, which is number(5). If Guess is >5, the program prints "Too high", else it prints "Too low". The program continues asking the user to Guess the number, until the right number is entered. When the right number is entered, it prints "You win!" and "Game over!". Thank you.'''

print("Welcome!")
guess = 0
while guess != 5:
    g = input("Guess the number:")
    guess = int(g)
    if guess == 5:
        print("You win!")
    else:
        if guess >5:
            print("Too high!")
        else:
            print("Too low!")
    print("Game over!")
