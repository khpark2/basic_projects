def new_board():
    board = []
    row_board = []
    i = 0
    j = 0
    while i < 3:
        while j < 3:
            row_board.append(None)
            j += 1
        board.append(row_board)
        i += 1
    print(board)

