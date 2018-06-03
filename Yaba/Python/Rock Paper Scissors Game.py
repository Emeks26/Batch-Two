# Precious Oti 07052327067
import random


p1 = "";
comp = ("r","p","s")
cc = 0
p2 = ""
game_type = "0"


def game_rules():
    print("TO SELECT ROCK PRESS 'R' ")
    print("TO SELECT PAPER PRESS 'P' ")
    print("TO SELECT SCISSSORS PRESS 'S' ")

    if game_type == "2":
        player_comp()
    else:
        player_player()

def check_result_pp():
    if p1 == "r":
        print("\nPLAYER 1 CHOSE  'ROCK' ")
        if p2 == "r":
            print("PLAYER 2 CHOSE  'ROCK' ")
            print("\n====== ROCK CAN'T BEAT ROCK =========")
            print("======== ITS A TIE =========")
        
        elif p2 == "p":
            print("PLAYER 2 CHOSE  'PAPER' ")
            print("\n====== PAPER BEATS ROCK =========")
            print("======== PLAYER 2 WINS  =========")

        elif p2 == "s":
            print("PLAYER 2 CHOSE  'SCISSORS' ")
            print("\n====== ROCK BEATS SCISSORS =========")
            print("======== PLAYER 1 WINS =========")

    elif p1 == "p":
        print("\nPLAYER 1 CHOSE  'PAPER' ")
        if p2 == "r":
            print("PLAYER 2 CHOSE  'ROCK' ")
            print("\n====== PAPER BEATS ROCK =========")
            print("======== PLAYER 1 WINS =========")
        
        elif p2 == "p":
            print("PLAYER 2 CHOSE  'PAPER' ")
            print("\n====== PAPER CAN'T BEAT PAPER =========")
            print("======== ITS A TIE =========")

        elif p2 == "s":
            print("PLAYER 2 CHOSE  'SCISSORS' ")
            print("\n====== SCISSORS BEATS PAPER =========")
            print("======== PLAYER 2 WINS =========")

    elif p1 == "s":
        print("\nPLAYER 1 CHOSE  'SCISSORS' ")
        if p2 == "r":
            print("PLAYER 2 CHOSE  'ROCK' ")
            print("\n====== ROCK BEATS SCISSORS =========")
            print("======== PLAYER 2 WINS =========")
        
        elif p2 == "p":
            print("PLAYER 2 CHOSE  'PAPER' ")
            print("\n====== SCISSORS BEATS PAPER =========")
            print("======== PLAYER 1 WINS =========")

        elif p2 == "s":
            print("PLAYER 2 CHOSE  'SCISSORS' ")
            print("\n====== SCISSORS CAN'T BEAT SCISSORS =========")
            print("======== ITS A TIE =========")

    else:
        print("AAAAAAAHHHHHHHH")


    print("\n\nTO START A NEW GAME PRESS  'N' ")
    print("TO GO TO MAIN MENU PRESS  'X' ")
    print("PRESS ANY OTHER KEY TO QUIT")

    restart = input("").lower()

    if restart == "n":
        game_rules()
    elif restart == "x":
        main_menu()
    else:
        print("========= GOOD BYE ==========")
        
    

def check_result_pc():
    if p1 == "r":
        print("\nPLAYER 1 CHOSE  'ROCK' ")
        if comp[cc] == "r":
            print("COMPUTER CHOSE  'ROCK' ")
            print("\n====== ROCK CAN'T BEAT ROCK =========")
            print("======== ITS A TIE =========")
        
        elif comp[cc] == "p":
            print("COMPUTER CHOSE  'PAPER' ")
            print("\n====== PAPER BEATS ROCK =========")
            print("======== COMPUTER WINS  =========")

        elif comp[cc] == "s":
            print("COMPUTER CHOSE  'SCISSORS' ")
            print("\n====== ROCK BEATS SCISSORS =========")
            print("======== PLAYER 1 WINS =========")

    elif p1 == "p":
        print("\nPLAYER 1 CHOSE  'PAPER' ")
        if comp[cc] == "r":
            print("COMPUTER CHOSE  'ROCK' ")
            print("\n====== PAPER BEATS ROCK =========")
            print("======== PLAYER 1 WINS =========")
        
        elif comp[cc] == "p":
            print("COMPUTER CHOSE  'PAPER' ")
            print("\n====== PAPER CAN'T BEAT PAPER =========")
            print("======== ITS A TIE =========")

        elif comp[cc] == "s":
            print("COMPUTER CHOSE  'SCISSORS' ")
            print("\n====== SCISSORS BEATS PAPER =========")
            print("======== COMPUTER WINS =========")

    elif p1 == "s":
        print("\nPLAYER 1 CHOSE  'SCISSORS' ")
        if comp[cc] == "r":
            print("COMPUTER CHOSE  'ROCK' ")
            print("\n====== ROCK BEATS SCISSORS =========")
            print("======== COMPUTER WINS =========")
        
        elif comp[cc] == "p":
            print("COMPUTER CHOSE  'PAPER' ")
            print("\n====== SCISSORS BEATS PAPER =========")
            print("======== PLAYER 1 WINS =========")

        elif comp[cc] == "s":
            print("COMPUTER CHOSE  'SCISSORS' ")
            print("\n====== SCISSORS CAN'T BEAT SCISSORS =========")
            print("======== ITS A TIE =========")

    else:
        print("AAAAAAAHHHHHHHH")

    print("\n\nTO START A NEW GAME PRESS  'N' ")
    print("TO GO TO MAIN MENU PRESS  'X' ")
    print("PRESS ANY OTHER KEY TO QUIT")

    restart = input("").lower()

    if restart == "n":
        game_rules()
    elif restart == "x":
        main_menu()
    else:
        print("========= GOOD BYE ==========")
        

def player_comp():
    print("\n======== PLAYER 1's TURN TO PLAY =========")
    global p1
    p1 = input("PLEASE SELECT A TYPE   ====  ").lower()
    print(p1)
    while p1 != "r" and p1 != "p" and p1 != "s":
        print("\n!!!!!!!!! WRONG INPUT !!!!!!!!!")
        print("TO SELECT ROCK PRESS 'R' ")
        print("TO SELECT PAPER PRESS 'P' ")
        print("TO SELECT SCISSSORS PRESS 'S' ")
        p1 = input("\nPLEASE SELECT A TYPE   ====  ").lower()

    global cc
    cc = random.randint(0,2)
    print(cc)

    check_result_pc()
        

def player_player():
    print("\n======== PLAYER 1's TURN TO PLAY =========")
    global p1
    p1 = input("PLEASE SELECT A TYPE   ====  ").lower()
    while p1 != "r" and p1 != "p" and p1 != "s":
        print("\n!!!!!!!!! WRONG INPUT !!!!!!!!!")
        print("TO SELECT ROCK PRESS 'R' ")
        print("TO SELECT PAPER PRESS 'P' ")
        print("TO SELECT SCISSSORS PRESS 'S' ")
        p1 = input("\nPLEASE SELECT A TYPE   ====  ").lower()

    print("\n======== PLAYER 2's TURN TO PLAY =========")
    global p2
    p2 = input("PLEASE SELECT A TYPE   ====  ").lower()
    while p2 != "r" and p2 != "p" and p2 != "s":
        print("\n!!!!!!!!! WRONG INPUT !!!!!!!!!")
        print("TO SELECT ROCK PRESS 'R' ")
        print("TO SELECT PAPER PRESS 'P' ")
        print("TO SELECT SCISSSORS PRESS 'S' ")
        p2 = input("\nPLEASE SELECT A TYPE   ====  ").lower()

    check_result_pp()


def main_menu():
    global comp
    global p1
    global p2
    global cc
    global game_type

    p1 = ""
    p2 = ""
    cc = 0
    
    game_type = input("======= For P1 vs P2 PRESS 1 ======== \n======= For P1 vs COMPUTER PRESS 2 ======== \n")

    while game_type != "1" and game_type != "2":
        print("!!!!!!!! INVALID INPUT SELECTED TRY AGAIN !!!!!!!!")
        game_type = input("======= For P1 vs P2 PRESS 1 ======== \n======= For P1 vs COMPUTER PRESS 2 ======== \n")
    
    if game_type == "1":
        print("========== GET READY =========")
        print("======== PLAYER 1 VS PLAYER 2 =========")
        game_rules()

    else:
        print("========== GET READY =========")
        print("======== PLAYER 1 VS COMPUTER =========")
        game_rules()

#start game == go to main menu
main_menu()



