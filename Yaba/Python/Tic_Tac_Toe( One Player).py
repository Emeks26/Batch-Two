import random

# list for the tic-tac-toe
a= [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ']
player1_symbol = 'x'
player2_symbol = 'O'
player2_name = 'Computer'
count = random.randint(0,1) # randomly select player 0 for player 1 and 1 for player 2

# function for printing tic tac toe board

def print_board(a = []):
    print('\n\n '+a[0]+'\t| '+a[1]+'\t| '+a[2])
    print('---------------------')
    print(' '+a[3]+'\t| '+a[4]+'\t| '+a[5])
    print('---------------------')
    print(' '+a[6]+'\t| '+a[7]+'\t| '+a[8])

# function for checking winner
def check_winner(a):
        if( ((a[0] == a[1] == a[2] != ' ') | (a[3] == a[4] == a[5] != ' ') | (a[6] == a[7] == a[8] != ' '))):
            return True
        elif((a[0] == a[3] == a[6] != ' ') | (a[1] == a[4] == a[7] != ' ') | (a[2] == a[5] == a[8] != ' ')):
            return True
        elif((a[0] == a[4] == a[8]!= ' ') | (a[2] == a[4] == a[6] != ' ')):
            return True
        else:
            return False

def future_check(val):
    for i in range(0,9):
        b = a[:]
        if(b[i] == ' '):
            b[i] = val
            if(check_winner(b)):
                return i
    return -1

print("Welcome to Jumanji Tic Tac Toe Game")
player1_name = input("Enter Player name (X): ")
current_player = player1_name
print(player1_name + ': ' +player1_symbol + '\t' + player2_name + ': ' +player2_symbol)
print_board(['1','2','3','4','5','6','7','8','9'])
for i in range(9):
    if(count % 2 != 0):
        pos = int(input(current_player +"'s turn Pls enter postion: "))
        if( (pos > 0) & (pos < 10)  ):
            if (a[pos-1] == ' '):
                a[pos-1] = player1_symbol
            else:
                print('pls check your input')
                continue
    else:
        print('\ncomputer\'s turn ')
        if(future_check('O') != -1):
            a[future_check('O')] = player2_symbol
        elif(future_check('x') != -1):
            a[future_check('x')] = player2_symbol
        else:
            pos = random.randint(0,8)
            if(a[pos] == ' ' ):
                a[pos] = player2_symbol
            else:
                continue

    print_board(a)
    if(check_winner(a) & (count % 2 == 0)):
        print(player2_name + ' wins')
        break
    elif(check_winner(a) & (count % 2 != 0)):
        print(player1_name + ' wins')
        break
    count += 1
if( check_winner(a) == False):
    print('No winner the Game is Draw')
