import random
import tictactoe

def random_ai(board, player):
    indeces = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                indeces.append([x, y])
    random_move = random.choice(indeces)
    return random_move[0], random_move[1]

def finds_winning_moves_ai(board, player):
    indeces = []
    winning_move = None
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                indeces.append([x, y])
                
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
    