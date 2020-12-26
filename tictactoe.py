import ai_ttt


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
    return (board)


def render(board):
    print('  0 1 2')
    print('  ' + ('-' * 6))
    rendered_row = []
    for y in range(3):  # iterate for each row
        for x in range(3):  # iterate for each element in each row
            if board[x][y] == None:
                rendered_row.append(' ')
            else:
                rendered_row.append(board[x][y])
        print(str(y) + '|' + ' '.join(rendered_row) + '|')
        rendered_row = []
    print('  ' + ('-' * 6))


def get_move(board, player, algorithm_ai):
    if algorithm_ai == 'random_ai':
        coords = ai_ttt.random_ai(board, player)
    elif algorithm_ai == 'finds_winning_moves_ai':
        coords = ai_ttt.finds_winning_moves_ai(board, player)
    elif algorithm_ai == 'finds_winning_and_losing_moves':
        coords = ai_ttt.finds_winning_and_losing_moves(board, player)
    elif algorithm_ai == 'human_player':
        coords = ai_ttt.human_player()
    elif algorithm_ai == 'minimax_ai':
        coords = ai_ttt.minimax_ai(board, player)
        
    while True:
        try:
            formatted_move = (coords[0], coords[1])
            break
        except NameError:
            user_move = input("You can only enter numbers. Please try again: ")
    return formatted_move


def make_move(board, player, algorithm_ai):
    while True:
        y, x = get_move(board, player, algorithm_ai)
        if board[y][x] == None:
            board[y][x] = player
            break
        else:
            print("That is an invalid move!")

    return board


def play():
    board = new_board()
    Player1 = 'O'
    Player2 = 'X'
    player_turn = Player1
    turn_counter = 0
    algorithm_ai = 'human_player'
    move = None
    while turn_counter < 9:
        make_move(board, player_turn, algorithm_ai)
        render(board)
        if player_turn == Player1:
            player_turn = Player2
            algorithm_ai = 'minimax_ai'
        elif player_turn == Player2:
            player_turn = Player1
            algorithm_ai = 'human_player'
        turn_counter += 1
        if get_winner(board) == None:
            pass
        elif get_winner(board) == 'X' or get_winner(board) == 'O':
            print(get_winner(board))
            break
    if get_winner(board) == None:
        print("It is a draw!")


def get_winner(board): # used only if game is over
    for row in board:
        if row[0] == row[1] and row[0] == row[2]:
            return row[0]
            break
        else:
            pass
    for column in range(3):
        if board[0][column] == board[1][column] and board[0][column] == board[2][column]:
            return board[0][column]
            break
        else:
            pass
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return str(board[0][0])
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return str(board[1][1])
    else:
        return None
    
