# board = [[ "-", "-", "-"],
#          [ "-", "-", "-"],
#          [ "-", "-", "-"]]

# board[0][1] = "X"
# print(board)

# def print_board(board):
#     print("*" * 17)
#     print(f"*    {board[0][0]}|{board[0][1]}|{board[0][2]}    *")
#     print(f"*    __|__|__    *")

# print_board(board)

board = [[ "-", "-", "-"],
         [ "-", "-", "-"],
         [ "-", "-", "-"]]
    

def print_board(board):
    print("*" * 17)
    print(f"*     {board[0][0]}|{board[0][1]}|{board[0][2]}     *")
    print(f"*   ___|_|___   *")
    print(f"*     {board[1][0]}|{board[1][1]}|{board[1][2]}     *")
    print(f"*   ___|_|___   *")
    print(f"*     {board[2][0]}|{board[2][1]}|{board[2][2]}     *")
    print(f"*      | |      *")
    print("*" * 17)

def player_input(player):
    print(f"{player}'s turn")
    x = int(input("Enter row: "))
    y = int(input("Enter column: "))
    board[x-1][y-1] = player
    print_board(board)

def check_win(board):
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] == board[0][1] == board[0][2] != "-":
        winner = True
    elif board [1][0] == board [1][1] == board [1][2] and board [1][0] == board [1][1] == board [1][2] != "-":
        winner = True
    elif board [2][0] == board [2][1] == board [2][2] and board [2][0] == board [2][1] == board [2][2] != "-":
        winner = True
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] == board[1][0] == board[2][0] != "-":
        winner = True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] == board[1][1] == board[1][2] != "-":
        winner = True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] == board[2][1] == board[2][2] != "-":
        winner = True
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == board[1][1] == board[2][2] != "-":
        winner = True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == board[1][1] == board[2][0] != "-":
        winner = True
    else:
        winner = False
    # create all the posible combination for winner + check tie (if all possitions are != '-' and winner == False then you tie)
    return winner

def check_tie(board):
    if board[0][0] != "-" and board[0][1] != "-" and board[0][2] != "-" and board[1][0] != "-" and board [1][1] != "-" and board [1][2] != "-" and board [2][0] != "-" and board[2][1] != "-" and board[2][2] != "-":
        tie = True
    else:
        tie = False
    return tie

def play():
    print('welcome')
    player = "X"
    print(f"It's {player}'s turn")
    while True:
        print_board(board)
        player_input(player)
        winresult = check_win(board)
        tieresult = check_tie(board)
        if winresult == True:
            print(f"The winner is {player}")
            break
        elif tieresult == True:
            print("The game is over")
            break
        else:
            if player == "X":
                player = "0"
            elif player == "0":
                player = "X"

play()