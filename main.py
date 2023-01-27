import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
finish = False
while not finish:
    square = pygame.Surface((300, 300))
    square.set_alpha(100, 0)
    square.fill((255, 0, 0))
    screen.blit(square, (0, 0))

    square = pygame.Surface((300, 300))
    square.set_alpha(100, 0)
    square.fill((0, 255, 0))
    screen.blit(square, (200, 0))

    square = pygame.Surface((300, 300))
    square.set_alpha(100, 0)
    square.fill((0, 0, 255))
    screen.blit(square, (100, 200))

    pygame.display.flip()

pygame.quit()
