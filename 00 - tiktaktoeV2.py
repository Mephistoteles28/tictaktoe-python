def menu():
    print("WELCOME TO TICTACTOE GAMES")
    print("1. Play")
    print("2. Exit")


def display(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')

def marker_input():
    marker = ''
    while marker != 'O' and marker != 'X':
        marker = input("Choose between 'O' or 'X' : ").upper()
    if marker == 'O':
        return ('O', 'X')
    elif marker == 'X':
        return ('X', 'O')
    
def user_input(board, marker):
    index_input = int(input('What index do you want to fill : '))

    if board[index_input] != ' ':
        print("Already filled!")
        if marker == 'X':
            board[index_input] = 'O'
        elif marker == 'O':
            board[index_input] = 'X'
        user_input(board, marker)
    else :
        board[index_input] = marker
    return board

def check_win(board, marker):
    '''
    Check if the player one / player two is winning. Vertical, Horizontal, Cross
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    '''
    # Vertical, player one
    if (board[1] == marker[0] and board[2] == marker[0] and board[3] == marker[0]) or (board[4] == marker[0] and board[5] == marker[0] and board[6] == marker[0]) or (board[7] == marker[0] and board[8] == marker[0] and board[9] == marker[0]):
        return True
    # Vertical, player two
    elif (board[1] == marker[1] and board[2] == marker[1] and board[3] == marker[1]) or (board[4] == marker[1] and board[5] == marker[1] and board[6] == marker[1]) or (board[7] == marker[1] and board[8] == marker[1] and board[9] == marker[1]):
        return True
    # Horizontal, player one
    elif (board[1] == marker[0] and board[4] == marker[0] and board[7] == marker[0]) or (board[2] == marker[0] and board[5] == marker[0] and board[8] == marker[0]) or (board[3] == marker[0] and board[6] == marker[0] and board[9] == marker[0]):
        return True
    #Horizontal, player two
    elif (board[1] == marker[1] and board[4] == marker[1] and board[7] == marker[1]) or (board[2] == marker[1] and board[5] == marker[1] and board[8] == marker[1]) or (board[3] == marker[1] and board[6] == marker[1] and board[9] == marker[1]):
        return True
    #Cross, player 1
    elif (board[1] == marker[0] and board[5] == marker[0] and board[9] == marker[0]) or (board[3] == marker[0] and board[5] == marker[0] and board[7] == marker[0]):
        return True
    # Cross, player 2
    elif (board[1] == marker[1] and board[5] == marker[1] and board[9] == marker[1]) or (board[3] == marker[1] and board[5] == marker[1] and board[7] == marker[1]):
        return True

    return False

def check_draw(board):
    if ' ' not in board:
        return True
    return False


# int main()
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display(board)
# Display menu and choose the input
menu()
menu_input = int(input("Choose what you want to do : "))
# Decide what marker to use for player 1
marker = (marker_input())
player1_marker = marker[0]
player2_marker = marker[1]

while menu_input != 2 :
    # Player one move
    print("Make a move player 1, ")
    player1_input = user_input(board, player1_marker)
    display(board)
    # Check if player one win
    check_win(board, marker)
    if check_win(board, marker) == True:
        print("Player one is win!!")
        break

    # Player two move
    print("Make a move player 2, ")
    player2_input = user_input(board, player2_marker)
    display(board)
    # Check if player two win
    check_win(board, marker)
    if check_win(board, marker) == True:
        print("Player two is win!!")
        break

    # Check if draw
    draw = check_draw(board)
    if draw == True:
        print("It is a draw")
        break
# If exit   
if menu_input == 2:
    print("See you again!")



