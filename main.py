import tictactoe

board = tictactoe.new_board()
board[0][1] = 'X'
board[1][1] = 'O'
tictactoe.render(board)