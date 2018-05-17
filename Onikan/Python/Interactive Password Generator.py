
#Project: Interactive Password Generator
#Team ReinBara
#Ibitoye    Barakat barikay0@gmail.com
#Reinhard Okokon	reinhardokokon@yahoo.com

import random

print("Welcome to our Interactive Password Generator \n ")

fn = input("Please enter your name: ")
mob = input("Please enter your month of bith: ")
pob = input("Please enter your place of birth: ")
sym = input("Enter the symbols of the follow: hash, percent, plus, minus. ")
maths = input ("A boy is 5yrs old today, how old will he be in 22yrs? ")

chars = fn+mob+pob+sym+maths
password = ''

for c in range(12):
    password += random.choice(chars)
print("This is your password:"+password)
