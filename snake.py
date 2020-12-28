import random 

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]

    def extend_body(self, position):
        self.body.append(position)


class Apple:
    def __init__(self, location):
        self.location = location


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], UP)

    def board_matrix(self):
        board = []
        for _ in range(self.height):
            sublist = []
            for _ in range(self.width):
                sublist.append(None)
            board.append(sublist)
        apple_spot = self.current_apple.location
        board[apple_spot[0]][apple_spot[1]] = "*"
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
    
    
    def next_position(self, position, step):
           return (position[0] + step[0], position[1] + step[1])
    
    
    def play(self):
        self.render()
        while True:    
            command = input("").upper()
            if command == 'W' and self.snake.direction != DOWN:
                self.snake.set_direction(UP)

            elif command == 'S' and self.snake.direction != UP:
                self.snake.set_direction(DOWN)

            elif command == 'A' and self.snake.direction != RIGHT:
                self.snake.set_direction(LEFT)

            elif command == 'D' and self.snake.direction != LEFT:
                self.snake.set_direction(RIGHT)

            elif command == '':
                self.snake.set_direction(self.snake.direction)

            
            next_position = self.next_position(self.snake.head(), self.snake.direction)
            
            if next_position == self.snake.body:
                print("GAME OVER STUPID!")
                break
            elif next_position == self.current_apple.location:
                self.snake.extend_body(next_position)
                self.generate_apple()
            else:
                self.snake.take_step(next_position)
            self.render()


    def generate_apple(self):
        while True:
            new_apple = (random.randint(1, self.width - 1), random.randint(1, self.height-1))
            if new_apple != self.snake.body:
                break
            
        self.current_apple = Apple(new_apple)