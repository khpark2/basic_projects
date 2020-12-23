import random


def random_ai(board, player):
    indeces = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                indeces.append([x, y])
    random_move = random.choice(indeces)
    return random_move[0], random_move[1]