# import sys
# sys.path.insert(1, 'tictactoe')

# from tictactoe import ai_ttt
# from tictactoe import tictactoe as ttt

# board = [
#   ['X', 'O', None],
#   [None, 'O', None],
#   ['X', None, 'X']
# ]
# print(ai_ttt.minimax_ai(board, 'O'))

# # ttt.play()
import snake
game = snake.Game(10, 10)

game.play()