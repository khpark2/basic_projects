import random

import time

DEAD = 0

LIVE = 1


def dead_state(width, height):
    return [[DEAD for _ in range(height)] for _ in range(width)]


def random_state(width, height):

    state = dead_state(width, height)

    for x in range(0, state_width(state)):

        for y in range(0, state_height(state)):

            random_number = random.random()

            if random_number > 0.85:

                cell_state = LIVE

            else:

                cell_state = DEAD

            state[x][y] = cell_state

    return state


def state_width(state):
    return len(state)


def state_height(state):
    return len(state[0])

def render(state):
    display_as = {
        DEAD: ' ',
        # This is "unicode" for a filled-in square. You can also just use a thick

        # "ASCII" character like a '$' or '#'.

        LIVE: u"\u2588"
    }
    lines = []
    for y in range(0, state_height(state)):
        line = ''
        for x in range(0, state_width(state)):
            line += display_as[state[x][y]] * 2
        lines.append(line)
    print("\n".join(lines))


def next_cell_value(cell_coords, state):
    width = state_width(state)
    height = state_height(state)
    x = cell_coords[0]
    y = cell_coords[1]
    n_live_neighbors = 0
    # Iterate around this cell's neighbors
    for x1 in range((x - 1), (x + 1) + 1):
        # Make sure we don't go off the edge of the board
        if x1 < 0 or x1 >= width: continue
        for y1 in range((y - 1), (y + 1) + 1):

            # Make sure we don't go off the edge of the board

            if y1 < 0 or y1 >= height: continue

            # Make sure we don't count the cell as a neighbor of itself!

            if x1 == x and y1 == y: continue

            if state[x1][y1] == LIVE:

                n_live_neighbors += 1

    if state[x][y] == LIVE:

        if n_live_neighbors <= 1:

            return DEAD

        elif n_live_neighbors <= 3:

            return LIVE

        else:

            return DEAD

    else:

        if n_live_neighbors == 3:

            return LIVE

        else:

            return DEAD


def next_board_state(init_board_state): # this code is original
    for row in range(len(init_board_state)):
        for column in range(len(init_board_state[0])):
            try:
                current_cell = init_board_state[row][column]
                top_left_cell = [0, 0]
                top_right_cell = [0, len(init_board_state[0]) - 1]
                bottom_left_cell = [len(init_board_state) - 1, 0]
                bottom_right_cell = [len(init_board_state) - 1, len(init_board_state[0]) - 1]
                top_edge = [0, column]
                left_edge = [row, 0]
                right_edge = [row, len(init_board_state[0]) - 1]
                bottom_edge = [len(init_board_state) - 1, column]

                live_cells_row_above = init_board_state[row - 1][column - 1] + 
                init_board_state[row - 1][column] + init_board_state[row - 1][column + 1]  # total live cells row above current cell
                live_cells_same_row = init_board_state[row][column - 1] + 
                init_board_state[row][column + 1]  # total live cells row on current cell
                live_cells_row_below = init_board_state[row + 1][column - 1] + init_board_state[row + 1][column] + init_board_state[row + 1][column + 1]  # total live cells row below current cell
                live_cells_column_left = init_board_state[row - 1][column - 1] + 
                init_board_state[row][column - 1] + init_board_state[row + 1][column - 1]
                live_cells_same_column = init_board_state[row - 1][column] + 
                init_board_state[row + 1][column]
                live_cells_column_right = init_board_state[row - 1][column + 1] + 
                init_board_state[row][column + 1] + init_board_state[row + 1][column + 1]

                if row == 0 and column == 0:
                    live_cells_total = init_board_state[row][column + 1] + 
                    init_board_state[row + 1][column] + init_board_state[row + 1][column + 1]
                elif row == 0 and column == top_right_cell[1]:
                    live_cells_total = init_board_state[row][column - 1] + 
                    init_board_state[row + 1][column - 1] + init_board_state[row + 1][column]
                elif row == bottom_left_cell[0] and column == 0:
                    live_cells_total = init_board_state[row - 1][column] + 
                    init_board_state[row - 1][column + 1] + init_board_state[row][column + 1]
                elif row == bottom_right_cell[0] and column == bottom_right_cell[1]:
                    live_cells_total = init_board_state[row - 1][column] + 
                    init_board_state[row - 1][column - 1] + init_board_state[row][column - 1]
                elif row == 0 and (column != 0 or column != len(init_board_state[0]) - 1):
                    live_cells_total = init_board_state[row][column - 1] + 
                    init_board_state[row][column + 1] + live_cells_row_below
                elif row == len(init_board_state) and 
                (column != 0 or column != len(init_board_state[0]) - 1):
                    live_cells_total = live_cells_row_above + live_cells_same_row
                elif (row != 0 or row != len(init_board_state)) and column == 0:
                    live_cells_total = live_cells_same_column + live_cells_column_right
                elif (row != 0 or row != len(init_board_state)) and 
                column == len(init_board_state[0]) - 1:
                    live_cells_total = live_cells_same_column + live_cells_column_left
                else:
                    live_cells_total = live_cells_row_above + live_cells_same_row + live_cells_row_below  # total cells surrounding current_cell if it is does not have edge surrounding current_cell

                init_board_state[row][column] = cell_evaluator(current_cell, live_cells_total)
                print(current_cell)

            except IndexError:
                pass

    return init_board_state


def cell_evaluator(cell, total):
    if cell == 1 and (total == 0 or total == 1 or total > 3):
        cell = 0
    elif cell == 0 and total == 3:
        cell = 1
        
    return cell