import pygame

BLUE = (0, 128, 255)
ORANGE = (255, 100, 0)


pygame.init()
screen = pygame.display.set_mode((900, 800))
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

    pygame.draw.circle(screen, color, (300, 60), 40)
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()  # need to make any updates to the screen to be visible
