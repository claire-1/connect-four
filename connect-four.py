import heapq
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
ROW_SPACES = 6 + 1
COLUMN_SPACES = 7 + 1
RADIUS = 40
EMPTY = 0
PLAYER_1 = "player 1"
PLAYER_2 = "player 2"


def set_up_board(screen):
    board_spaces_locations = dict()
    board_column_locations = dict()
    board = dict()
    color = BLUE
    screen.fill(pygame.color.THECOLORS['mediumblue'])
    for col in range(1, COLUMN_SPACES):
        board_column_heap = list()
        for row in range(1, ROW_SPACES):

            screen_location = (math.floor(col*(SCREEN_HEIGHT /
                                               ROW_SPACES) - RADIUS), math.floor(row*(SCREEN_WIDTH/ROW_SPACES) - RADIUS))
            pygame.draw.circle(screen, OPEN_TILE_COLOR,
                               screen_location, RADIUS)
            board_spaces_locations[screen_location] = (row, col)

           # board_column_heap.append((row, screen_location))
            heapq.heappush(board_column_heap,
                           (ROW_SPACES - row, screen_location))
            # print("for location " + str((row, col)) +
            #       "filling in board_column_heap " + str(board_column_heap))

            board[(row, col)] = EMPTY  # TODO maybe don't need
        # TODO how going to get all spaces in column?
        board_column_locations[col] = board_column_heap
  #  pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    pygame.display.update()  # need to make any updates to the screen to be visible

    return (board_spaces_locations, board, board_column_locations)


def clear_board():
    pass  # TODO


def player_move(screen, move, player_color):
    pass  # TODO


def row_winner(board, row, col, player):
    if (board[row, col] == player
        and board[row + 1, col] == player
        and board[row + 2, col] == player
            and board[row + 3, col] == player):
        return player

    return None  # keep playing


def col_winner(board, row, col, player):
    if (board[row, col] == player
        and board[row, col + 1] == player
        and board[row, col + 2] == player
            and board[row, col + 3] == player):
        return player

    return None  # keep playing


def left_diagonal_winner(board, row, col, player):
    # starts from the top right corner
    print("row " + str(row))
    print("col " + str(col))
    print("left  " + str(board[(row, col)]))
    # print("left  " + str(board[(row-1, col-1)]))
    # print("left  " + str(board[(row-2, col-2)]))
    # print("left  " + str(board[(row-3, col-3)]))
    if (board[row, col] == player
        and board[row+1, col-1] == player
        and board[row+2, col-2] == player
            and board[row+3, col-3] == player):
        return player

    return None


def right_diagonal_winner(board, row, col, player):
    print("row " + str(row))
    print("col " + str(col))
    print("right  " + str(board[(row, col)]))
    # starts from the top right corner
    if (board[row, col] == player
        and board[row+1, col+1] == player
        and board[row+2, col+2] == player
            and board[row+3, col+3] == player):
        return player

    return None


def print_board(board, screen):
    for (row, col) in board:
        font = pygame.font.SysFont(None, 50)
        text = font.render(
            "The winner is " + str((row, col)), True, ORANGE)
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH/2 - col, SCREEN_HEIGHT/2 - row))

    screen.blit(text, text_rect)


def game_status(board):
   # print("BOARD " + str(board))

    # Check for row win
    for (row, col) in board:
        if (row + 3) < ROW_SPACES:
            winner = row_winner(board, row, col, PLAYER_1)
            if winner is not None:
                print("WINNER1")
                return (winner, False)

            winner = row_winner(board, row, col, PLAYER_2)
            if winner is not None:
                print("WINNER2")
                return (winner, False)

        if (col + 3) < COLUMN_SPACES:
            winner = col_winner(board, row, col, PLAYER_1)
            if winner is not None:
                print("WINNER1")
                return (winner, False)

            winner = col_winner(board, row, col, PLAYER_2)
            if winner is not None:
                print("WINNER2")
                return (winner, False)

        if (col + 3) < COLUMN_SPACES and (row + 3) < ROW_SPACES:
            print("right winner?")
            winner = right_diagonal_winner(board, row, col, PLAYER_1)
            if winner is not None:
                print("WINNER1")
                return (winner, False)

            winner = right_diagonal_winner(board, row, col, PLAYER_2)
            if winner is not None:
                print("WINNER2")
                return (winner, False)

        if (col - 3) > 0 and (row + 3) < ROW_SPACES:
            print("left winner?")
            winner = left_diagonal_winner(board, row, col, PLAYER_1)
            if winner is not None:
                print("WINNER1")
                return (winner, False)

            winner = left_diagonal_winner(board, row, col, PLAYER_2)
            if winner is not None:
                print("WINNER2")
                return (winner, False)
        # if (col - 3) > 0 and (row - 3) > 0:
        #     print("left winner?")
        #     winner = left_diagonal_winner(board, row, col, PLAYER_1)
        #     if winner is not None:
        #         print("WINNER1")
        #         return (winner, False)

        #     winner = left_diagonal_winner(board, row, col, PLAYER_2)
        #     if winner is not None:
        #         print("WINNER2")
        #         return (winner, False)

    return (None, True)  # no winner and still playing
    #     if winner is not None:
    #         return winner
    # else:
    #     return
    # if (board[row, col] == PLAYER_1
    #     and board[row + 1, col] == PLAYER_1
    #     and board[row + 2, col] == PLAYER_1
    #         and board[row + 3, col] == PLAYER_1):

    #     return PLAYER_1  # winner

    # Check for col win
    # Check for right diagonal win
    # Check for left diagonal win
    pass  # TODO need to figure out how are going to decide who won


def play(screen, board_spaces_locations, board, board_column_locations):
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

            (clicked_x, clicked_y) = event.pos
            for (clicked_circle_screen_loc, board_location) in board_spaces_locations.items():
                x_squared = (clicked_x - clicked_circle_screen_loc[0])**2
                y_squared = (clicked_y - clicked_circle_screen_loc[1])**2

                if (math.sqrt(x_squared + y_squared)) < 60:
                    (row, col) = board_location
                    # print("column " + str(col))

                    if (len(board_column_locations[col]) == 0):
                        continue

                    (placement_row, open_screen_loc) = heapq.heappop(
                        board_column_locations[col])

                    if whose_move == PLAYER_1:
                        pygame.draw.circle(screen, PLAYER_1_TITLE_COLOR,
                                           open_screen_loc, RADIUS)
                        whose_move = PLAYER_2
                    else:
                        whose_move = PLAYER_1
                        pygame.draw.circle(screen, PLAYER_2_TITLE_COLOR,
                                           open_screen_loc, RADIUS)

                    pygame.display.flip()
                    board[(placement_row, col)] = whose_move
                    (winner, playing) = game_status(board)
                    if winner is not None:
                        # pygame.draw.rect(
                        #     screen, pygame.color.THECOLORS["orange"], pygame.Rect(30, 30, 60, 60))
                        # None lets you use the default system font
                        display_winner(screen, winner)
                        pygame.display.flip()
                        return winner
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

        # pygame.display.flip()  # need to make any updates to the screen to be visible


def display_winner(screen, winner):
    font = pygame.font.SysFont(None, 100)
    text = font.render(
        "The winner is " + str(winner), True, ORANGE)
    text_rect = text.get_rect(
        center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    screen.blit(text, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    (board_spaces_locations, board, board_column_locations) = set_up_board(screen)
    winner = play(screen, board_spaces_locations,
                  board, board_column_locations)
    # display_winner(screen, winner)
    # playing = True
    # clear_board = False
    # whose_move = PLAYER_1

    # while playing:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             playing = False
    #         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #             clear_board = True  # clear the board when you press the space key

    #         if event.type != pygame.MOUSEBUTTONUP:
    #             continue  # wait for the user to click something

    #         (clicked_x, clicked_y) = event.pos
    #         for (clicked_circle_screen_loc, board_location) in board_spaces_locations.items():
    #             x_squared = (clicked_x - clicked_circle_screen_loc[0])**2
    #             y_squared = (clicked_y - clicked_circle_screen_loc[1])**2

    #             if (math.sqrt(x_squared + y_squared)) < 60:
    #                 (row, col) = board_location
    #                 (placement_row, open_screen_loc) = heapq.heappop(
    #                     board_column_locations[col])

    #                 board[(placement_row, col)] = whose_move

    #                 if whose_move == PLAYER_1:
    #                     pygame.draw.circle(screen, PLAYER_1_TITLE_COLOR,
    #                                        open_screen_loc, RADIUS)
    #                     whose_move = PLAYER_2
    #                 else:
    #                     whose_move = PLAYER_1
    #                     pygame.draw.circle(screen, PLAYER_2_TITLE_COLOR,
    #                                        open_screen_loc, RADIUS)

    #                 (winner, playing) = game_status(board)
    #                 if winner is not None:
    #                     # pygame.draw.rect(
    #                     #     screen, pygame.color.THECOLORS["orange"], pygame.Rect(30, 30, 60, 60))
    #                     # None lets you use the default system font
    #                     font = pygame.font.SysFont(None, 100)
    #                     text = font.render(
    #                         "The winner is " + str(winner), True, ORANGE)
    #                     text_rect = text.get_rect(
    #                         center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    #                     screen.blit(text, text_rect)
    #                 # TODO need to find the last filled in location in a column and then fill in that spot
    #                 # really need a dictionary that allows for searching on both the key and the value

    #     if clear_board:
    #         # TODO
    #         color = BLUE
    #     else:
    #         # TODO
    #         color = ORANGE

    #  pygame.draw.circle(screen, color, (300, 60), 40)
    #  pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    # pygame.display.flip()  # need to make any updates to the screen to be visible

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                (board_spaces_locations, board,
                 board_column_locations) = set_up_board(screen)
                winner = play(screen, board_spaces_locations,
                              board, board_column_locations)
                # TODO HERE handle and tied game
            # TODO handle resetting the board to play again
            pygame.display.flip()


if __name__ == "__main__":
    # execute only if run as a script
    main()
