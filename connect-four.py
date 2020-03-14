import pygame

BLUE = (0, 128, 255)  # TODO delete eventually
ORANGE = (255, 100, 0)  # TODO delete eventually
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
OPEN_TILE_COLOR = pygame.color.THECOLORS['white']  # TODO need to make gray
FIRST_PERSON_TITLE_COLOR = (255, 100, 0)  # TODO need to make red
SECOND_PERSON_TITLE_COLOR = (255, 100, 10)  # TODO need to make yellow
HORIZONTAL_SPACES = 7 + 1
VERTICAL_SPACES = 6 + 1
RADIUS = 40


def set_up_board(screen):
    board_spaces = dict()
    color = BLUE
    screen.fill(pygame.color.THECOLORS['mediumblue'])
    for i in range(1, VERTICAL_SPACES):
        for j in range(1, HORIZONTAL_SPACES):
            screen_location = (int(j*(SCREEN_HEIGHT /
                                      VERTICAL_SPACES) - RADIUS), int(i*(SCREEN_WIDTH/HORIZONTAL_SPACES) - RADIUS))
            pygame.draw.circle(screen, OPEN_TILE_COLOR,
                               screen_location, RADIUS)
            board_spaces[(i, j)] = screen_location
  #  pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    pygame.display.update()  # need to make any updates to the screen to be visible
    r
    return board_spaces


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    set_up_board(screen)
    done = False
    clear_board = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                clear_board = True  # clear the board when you press the space key
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
