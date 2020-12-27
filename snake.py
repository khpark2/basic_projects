UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, postion):
        self.body = self.body[1:] + position

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]


class Apple:
    pass


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0, 5), (1, 5), (2, 5), (3, 5)], UP)

    def board_matrix(self):
        board = []
        for _ in range(self.height):
            sublist = []
            for _ in range(self.width):
                sublist.append(None)
            board.append(sublist)
        return board

    def render(self):
        matrix = self.board_matrix()
        num_dashes = len(matrix[0])
        head = self.snake.head()
        print("+" + ("-" * num_dashes) + "+")

        for part in self.snake.body[:-1]:
            x, y = part
            matrix[self.height - 1 - y][x] = "X"
        matrix[self.height - 1 - head[1]][head[0]] = "O"

        for row in matrix:
            rendered_row = []
            for element in row:
                if element == None:
                    rendered_row.append(" ")
                elif element != None:
                    rendered_row.append(element)
            print("|" + "".join(rendered_row) + "|")
        print("+" + ("-" * num_dashes) + "+")

    def play(self):
        command = input("").upper
        if command == 'W':
            snake.self.set_direction('UP')
            