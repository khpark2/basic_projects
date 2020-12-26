class Snake:
    pass

class Apple:
    pass

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board_matrix(self):
        board = []
        for _ in range(self.height):
            sublist = []
            for _ in self.width:
                sublist.append(None)
            board.append(sublist)
        return board

    def render(self, board_matrix):
        matrix = self.board_matrix
        print('')
        
        print("Height: " + str(self.height))
        print("Width: " + str(self.width))

