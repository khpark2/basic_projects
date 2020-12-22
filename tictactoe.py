def new_board():
    board = []
    row_board = []
    i = 0
    j = 0
    while i < 3:
        row_board = []
        j = 0
        while j < 3:
            row_board.append(None)
            j += 1
        board.append(row_board)
        i += 1
    return(board)

def render(board):
    print('  1 2 3')
    print('  ' + ('-' * 6))
    rendered_row = []
    for y in range(3): # iterate for each row
        for x in range(3): # iterate for each element in each row
            if board[x][y] == None:
                rendered_row.append(' ')
            else:
                rendered_row.append(board[x][y])
        print(str(y+1) + '|' + ' '.join(rendered_row) + '|')
        rendered_row = []
    print('  ' + ('-' * 6))

def get_move():
    user_move = input("Type in your move in the format x, y and press ENTER: ")
    formatted_move = eval(user_move)
    return formatted_move

def make_move(board, player):

    while True:
        x, y = get_move()
        if board[x][y] != None:
            board[x][y] = player
            break
        else:
            print("That is an invalid move!")
    return(board)

def play():
    board = new_board()
    Player1 = 'O'
    Player2 = 'X'
    player_turn = Player1
    turn_counter = 0
    while turn_counter < 9:
        make_move(board, player_turn)
        render(board)
        if player_turn == Player1:
            player_turn = Player2
        elif player_turn == Player2:
            player_turn = Player1
        turn_counter += 1
