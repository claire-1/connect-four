import math

import pygame

BLUE = (0, 128, 255)  # TODO delete eventually
ORANGE = (255, 100, 0)  # TODO delete eventually
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
OPEN_TILE_COLOR = pygame.color.THECOLORS['white']  # TODO need to make gray
PLAYER_1_TITLE_COLOR = pygame.color.THECOLORS['red']  # TODO need to make red
# TODO need to make yellow
PLAYER_2_TITLE_COLOR = pygame.color.THECOLORS['yellow']
HORIZONTAL_SPACES = 7 + 1
VERTICAL_SPACES = 6 + 1
RADIUS = 40
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2


def set_up_board(screen):
    board_spaces_locations = dict()
    board_column_locations = dict()
    board = dict()
    color = BLUE
    screen.fill(pygame.color.THECOLORS['mediumblue'])
    for i in range(1, VERTICAL_SPACES):
        board_column_heap = list()
        for j in range(1, HORIZONTAL_SPACES):

            screen_location = (math.floor(j*(SCREEN_HEIGHT /
                                             VERTICAL_SPACES) - RADIUS), math.floor(i*(SCREEN_WIDTH/HORIZONTAL_SPACES) - RADIUS))
            pygame.draw.circle(screen, OPEN_TILE_COLOR,
                               screen_location, RADIUS)
            board_spaces_locations[screen_location] = (i, j)

            board_column_heap.append(j, screen_location)

            board[(i, j)] = EMPTY  # TODO maybe don't need
        # TODO how going to get all spaces in column?
        board_column_locations[i] = board_column_heap
  #  pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    pygame.display.update()  # need to make any updates to the screen to be visible

    return (board_spaces_locations, board, board_column_locations)


def clear_board():
    pass  # TODO


def player_move(screen, move, player_color):
    pass  # TODO


def game_status(screen, board_spaces):
    pass  # TODO need to figure out how are going to decide who won


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    (board_spaces_locations, board, board_column_locations) = set_up_board(screen)
    playing = True
    clear_board = False
    whose_move = PLAYER_1

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                clear_board = True  # clear the board when you press the space key

            if event.type != pygame.MOUSEBUTTONUP:
                continue  # wait for the user to click something
            # TODO here

            (clicked_x, clicked_y) = event.pos
            for (screen_location, board_location) in board_spaces_locations:
                x_squared = (clicked_x - screen_location[0])**2
                y_squared = (clicked_y - screen_location[1])**2

                if (math.sqrt(x_squared + y_squared)) < 60:
                    (row, col) = board_location
                    # TODO here -- trying to get the lowest filled in space
                    heapq.pop(board_column_locations[VERTICAL_SPACES - col])

                    if whose_move == PLAYER_1:
                        pygame.draw.circle(screen, PLAYER_1_TITLE_COLOR,
                                           screen_location, RADIUS)
                        whose_move = PLAYER_2
                    else:
                        pygame.draw.circle(screen, PLAYER_2_TITLE_COLOR,
                                           screen_location, RADIUS)
                        whose_move = PLAYER_1
                    # TODO need to find the last filled in location in a column and then fill in that spot
                    # really need a dictionary that allows for searching on both the key and the value

        if clear_board:
            # TODO
            color = BLUE
        else:
            # TODO
            color = ORANGE

      #  pygame.draw.circle(screen, color, (300, 60), 40)
      #  pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

        pygame.display.flip()  # need to make any updates to the screen to be visible


if __name__ == "__main__":
    # execute only if run as a script
    main()
