a= [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ']
player1_symbol = 'X'
player2_symbol = 'O'
count = 1


def print_board(a = []):
    print(' '+a[0]+'\t| '+a[1]+'\t| '+a[2])
    print('---------------------')
    print(' '+a[3]+'\t| '+a[4]+'\t| '+a[5])
    print('---------------------')
    print(' '+a[6]+'\t| '+a[7]+'\t| '+a[8])

def check_winner(a, count):
        if( ((a[0] == a[1] == a[2] != ' ') | (a[3] == a[4] == a[5] != ' ') | (a[6] == a[7] == a[8] != ' '))):
            if (count % 2 == 0):
                print(player2_name+" won")
            else:
                print(player1_name+" won")
            return True
        elif((a[0] == a[3] == a[6] != ' ') | (a[1] == a[4] == a[7] != ' ') | (a[2] == a[5] == a[8] != ' ')):
            if (count % 2 == 0):
                print(player2_name+" won")
            else:
                print(player1_name+" won")
            return True
        elif((a[0] == a[4] == a[8]!= ' ') | (a[2] == a[4] == a[6] != ' ')):
            if (count % 2 == 0):
                print(player2_name+" won")
            else:
                print(player1_name+" won")
            return True
        return False
                

print("Welcome to Jumanji Tic Tac Toe Game")
player1_name = input("Enter Player 1 name (X): ")
player2_name = input("Enter Player 2 name (O): ")

current_player = player1_name

print(player1_name + ': ' +player1_symbol + '\t' + player2_name + ': ' +player2_symbol)

while (count < 10):
    
    pos = int(input(current_player +"'s turn Pls enter postion: "))
    if( (pos > 0) & (pos < 10)  ):
        if ((count % 2 == 0) & (a[pos-1] == ' ')):
            a[pos-1] = player2_symbol
            current_player = player1_name
        elif ((count % 2 != 0) & (a[pos-1] == ' ')):
            a[pos-1] = player1_symbol
            current_player = player2_name
        else:
            print('pls check your input')
            continue
        print_board(a)
        
        if (check_winner(a, count)):
            break
        count += 1
    else:
        print('pls check your input')
        continue

if( check_winner(a, count) == False):
    print('No winner the Game is Draw')




