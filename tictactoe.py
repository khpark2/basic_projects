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