import random
import tictactoe

def random_ai(board, player):
    indeces = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                indeces.append([y, x])
    random_move = random.choice(indeces)
    return random_move[0], random_move[1]

def finds_winning_moves_ai(board, player):
    indeces = []
    winning_move = None
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                indeces.append([y, x])
                
    for i in indeces:
        board[i[1]][i[0]] = player
        if tictactoe.get_winner(board) == player:
            winning_move = [i[0], i[1]]
            board[i[1]][i[0]] = None
            break
        elif tictactoe.get_winner(board) != player:
            board[i[1]][i[0]] = None
            
    if winning_move == None:
        winning_move = random.choice(indeces)
    
    return winning_move

def finds_winning_and_losing_moves(board, player):
    indeces = []
    winning_move = None
    losing_move = None
    random_move = None
    other_player = None
    if player == 'X':
        other_player = 'O'
    else:
        other_player = 'X'

    for y in range(3): # find all open spots on board
        for x in range(3):
            if board[y][x] == None:
                indeces.append([x, y])

    for i in indeces: # returns losing move
        board[i[1]][i[0]] = other_player
        if tictactoe.get_winner(board) == other_player:
            losing_move = [i[0], i[1]]
            board[i[1]][i[0]] = None
            break
        elif tictactoe.get_winner(board) != other_player:
            board[i[1]][i[0]] = None
            
    for i in indeces: # returns winning move
        board[i[1]][i[0]] = player
        if tictactoe.get_winner(board) == player:
            winning_move = [i[0], i[1]]
            board[i[1]][i[0]] = None
            break
        elif tictactoe.get_winner(board) != player:
            board[i[1]][i[0]] = None
    
    if losing_move != None and winning_move != None: # removes winning move and losing move from empty spot lists
        indeces.remove(losing_move)
        indeces.remove(winning_move)
        random_move = random.choice(indeces)
    elif losing_move != None and winning_move == None: # found losing move and remove it from empty spot lists
        indeces.remove(losing_move)
        random_move = random.choice(indeces)
    elif losing_move == None and winning_move != None: # found winning move and remove it from empty spot lists
        indeces.remove(winning_move)
        random_move = random.choice(indeces)

    return losing_move, winning_move, random_move
    
    
def human_player():
    user_move = input("Type in your move in the format x, y and press ENTER: ")
    formatted_move = []
    while True:
        try:
            formatted_move = eval(user_move)
            break
        except NameError:
            user_move = input("You can only enter numbers. Please try again: ")
    return formatted_move