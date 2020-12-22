import game


if __name__ == "__main__":
    board = game.random_state(10, 10)
    next_state = game.next_board_state(board)
    while True:
        print(game.render(game.next_board_state(next_state)))