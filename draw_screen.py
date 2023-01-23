from blocks import blocks
from config import *


def draw_object(player):
    # draw L left
    list_reacts = []
    for cor in blocks(num_arena):
        aux = pygame.draw.rect(screen, "#c29f2e", (cor[1] * 25, cor[0] * 25 + 50, 25, 25))
        aux = aux.colliderect(player)
        list_reacts.append(aux)
    # draw screen
    screen_1 = pygame.draw.rect(screen, "#c29f2e", (0, 50, 1000, 25))
    screen_1 = screen_1.colliderect(player)
    list_reacts.append(screen_1)

    screen_2 = pygame.draw.rect(screen, "#c29f2e", (0, 725, 1000, 25))
    screen_2 = screen_2.colliderect(player)
    list_reacts.append(screen_2)

    screen_3 = pygame.draw.rect(screen, "#c29f2e", (975, 75, 25, 650))
    screen_3 = screen_3.colliderect(player)
    list_reacts.append(screen_3)

    screen_4 = pygame.draw.rect(screen, "#c29f2e", (0, 75, 25, 650))
    screen_4 = screen_4.colliderect(player)
    list_reacts.append(screen_4)

    # collision detection
    if True in list_reacts:
        return False
    else:
        return True
