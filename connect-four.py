import heapq
import math

import pygame

BLUE = (0, 128, 255)  # TODO delete eventually
ORANGE = (255, 100, 0)  # TODO delete eventually
BOARD_WIDTH = 900
FOOTER_COLOR = pygame.color.THECOLORS["darkseagreen"]
FOOTER_HEIGHT = 200
BOARD_HEIGHT = 800
OPEN_TILE_COLOR = pygame.color.THECOLORS['white']  # TODO need to make gray
PLAYER_1_TITLE_COLOR = pygame.color.THECOLORS['firebrick3']
PLAYER_2_TITLE_COLOR = pygame.color.THECOLORS['gold1']
BACKGROUND_COLOR = pygame.color.THECOLORS["darkcyan"]
GENERAL_TEXT_COLOR = pygame.color.THECOLORS['darkorange3']
ROW_SPACES = 6 + 1
COLUMN_SPACES = 7 + 1
RADIUS = 40
EMPTY = 0
PLAYER_1 = "red player"
PLAYER_2 = "yellow player"
CLEAR_BOARD = 0
QUIT_GAME = 1
HEADER_HEIGHT = 100


def set_up_screen():
    screen = pygame.display.set_mode(
        (BOARD_WIDTH, BOARD_HEIGHT + FOOTER_HEIGHT + HEADER_HEIGHT))
    screen.fill(BACKGROUND_COLOR)

    return screen


def set_up_header(screen):
    font = pygame.font.SysFont(None, 75)
    text = font.render("Welcome to Connect Four!", True, FOOTER_COLOR)
    text_rect = text.get_rect(
        center=(BOARD_WIDTH/2, HEADER_HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.display.update()


def set_up_board(screen):
    set_up_header(screen)

    board_spaces_locations = dict()
    board_column_locations = dict()
    board = dict()
    for col in range(1, COLUMN_SPACES):
        board_column_heap = list()
        for row in range(1, ROW_SPACES):

            screen_location = (math.floor(col*((BOARD_HEIGHT) /
                                               ROW_SPACES) - RADIUS), math.floor(row*(BOARD_WIDTH/COLUMN_SPACES) - RADIUS + HEADER_HEIGHT))
            pygame.draw.circle(screen, OPEN_TILE_COLOR,
                               screen_location, RADIUS)
            board_spaces_locations[screen_location] = (row, col)

            heapq.heappush(board_column_heap,
                           (ROW_SPACES - row, screen_location))

            board[(row, col)] = EMPTY
        board_column_locations[col] = board_column_heap

    pygame.display.update()  # need to make any updates to the screen to be visible

    return (board_spaces_locations, board, board_column_locations)


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
    if (board[row, col] == player
        and board[row+1, col-1] == player
        and board[row+2, col-2] == player
            and board[row+3, col-3] == player):
        return player

    return None


def right_diagonal_winner(board, row, col, player):
    if (board[row, col] == player
        and board[row+1, col+1] == player
        and board[row+2, col+2] == player
            and board[row+3, col+3] == player):
        return player

    return None


def display_turn(screen, player):
    cover_up_text = pygame.Rect(0, 0, BOARD_WIDTH, FOOTER_HEIGHT)
    cover_up_text.center = (BOARD_WIDTH/2, (BOARD_HEIGHT + FOOTER_HEIGHT/2))
    pygame.draw.rect(
        screen, FOOTER_COLOR, cover_up_text)

    font = pygame.font.SysFont(None, 50)

    if player == PLAYER_1:
        text = font.render(
            "Next move: " + str(player), True, PLAYER_1_TITLE_COLOR)
    elif player == PLAYER_2:
        text = font.render(
            "Next move: " + str(player), True, PLAYER_2_TITLE_COLOR)

    text_rect = text.get_rect(
        center=(BOARD_WIDTH/2, (BOARD_HEIGHT + FOOTER_HEIGHT/2)))

    screen.blit(text, text_rect)

    text = font.render("press space bar to clear", True, GENERAL_TEXT_COLOR)
    text_rect = text.get_rect(
        center=(BOARD_WIDTH/2, (BOARD_HEIGHT + FOOTER_HEIGHT/5)))
    screen.blit(text, text_rect)
    pygame.display.flip()


def game_status(board):
    # Check for row win
    for (row, col) in board:
        if (row + 3) < ROW_SPACES:
            winner = row_winner(board, row, col, PLAYER_1)
            if winner is not None:
                return (winner, False)

            winner = row_winner(board, row, col, PLAYER_2)
            if winner is not None:
                return (winner, False)

        if (col + 3) < COLUMN_SPACES:
            winner = col_winner(board, row, col, PLAYER_1)
            if winner is not None:
                return (winner, False)

            winner = col_winner(board, row, col, PLAYER_2)
            if winner is not None:
                return (winner, False)

        if (col + 3) < COLUMN_SPACES and (row + 3) < ROW_SPACES:
            winner = right_diagonal_winner(board, row, col, PLAYER_1)
            if winner is not None:
                return (winner, False)

            winner = right_diagonal_winner(board, row, col, PLAYER_2)
            if winner is not None:
                return (winner, False)

        if (col - 3) > 0 and (row + 3) < ROW_SPACES:
            winner = left_diagonal_winner(board, row, col, PLAYER_1)
            if winner is not None:
                return (winner, False)

            winner = left_diagonal_winner(board, row, col, PLAYER_2)
            if winner is not None:
                return (winner, False)
    return (None, True)  # no winner and still playing


def play(screen, board_spaces_locations, board, board_column_locations):
    playing = True
    clear_board = False
    whose_move = PLAYER_1

    while playing:
        display_turn(screen, whose_move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT_GAME
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return CLEAR_BOARD  # no winner b/c want to clear board when you press the space key

            if event.type != pygame.MOUSEBUTTONUP:
                continue  # wait for the user to click something

            (clicked_x, clicked_y) = event.pos
            for (clicked_circle_screen_loc, board_location) in board_spaces_locations.items():
                x_squared = (clicked_x - clicked_circle_screen_loc[0])**2
                y_squared = (clicked_y - clicked_circle_screen_loc[1])**2

                if (math.sqrt(x_squared + y_squared)) < 60:
                    (row, col) = board_location

                    if (len(board_column_locations[col]) == 0):
                        # all the spaces in the column are taken so the click was on accident
                        continue

                    (placement_row, open_screen_loc) = heapq.heappop(
                        board_column_locations[col])

                    if whose_move == PLAYER_1:
                        pygame.draw.circle(screen, PLAYER_1_TITLE_COLOR,
                                           open_screen_loc, RADIUS)
                        board[(placement_row, col)] = whose_move
                        (winner, playing) = game_status(board)
                        whose_move = PLAYER_2
                    else:
                        pygame.draw.circle(screen, PLAYER_2_TITLE_COLOR,
                                           open_screen_loc, RADIUS)
                        board[(placement_row, col)] = whose_move
                        (winner, playing) = game_status(board)
                        whose_move = PLAYER_1

                    pygame.display.flip()

                    if winner is not None:
                        display_winner(screen, winner)
                        return winner


def display_winner(screen, winner):
    font = pygame.font.SysFont(None, 100)
    text = font.render(
        str(winner) + " won!", True, pygame.color.THECOLORS["darkorange2"])
    text_rect = text.get_rect(
        center=(BOARD_WIDTH/2, BOARD_HEIGHT/2))

    screen.blit(text, text_rect)
    pygame.display.flip()


def main():
    pygame.init()
    screen = set_up_screen()
    (board_spaces_locations, board, board_column_locations) = set_up_board(screen)
    winner = play(screen, board_spaces_locations,
                  board, board_column_locations)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if winner == CLEAR_BOARD or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                screen = set_up_screen()
                (board_spaces_locations, board,
                 board_column_locations) = set_up_board(screen)
                winner = play(screen, board_spaces_locations,
                              board, board_column_locations)
            if event.type == pygame.QUIT or winner == QUIT_GAME:
                waiting = False
                pygame.quit()
                return


if __name__ == "__main__":
    # execute only if run as a script
    main()
