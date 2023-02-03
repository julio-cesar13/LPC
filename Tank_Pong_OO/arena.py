from blocks import Blocks
import pygame


class Arena:
    def __init__(self, num_arena, screen):
        self.num_arena = num_arena
        self.screen = screen

    def draw_object(self):
        # draw L left
        blocks = Blocks(self.num_arena)
        list_reacts = []
        for cor in blocks.blocks():
            aux = pygame.draw.rect(self.screen, "#c29f2e", (cor[1] * 25, cor[0] * 25 + 50, 25, 25))
            list_reacts.append(aux)
        # draw screen
        screen_1 = pygame.draw.rect(self.screen, "#c29f2e", (0, 50, 1000, 25))
        list_reacts.append(screen_1)

        screen_2 = pygame.draw.rect(self.screen, "#c29f2e", (0, 725, 1000, 25))
        list_reacts.append(screen_2)

        screen_3 = pygame.draw.rect(self.screen, "#c29f2e", (975, 75, 25, 650))
        list_reacts.append(screen_3)

        screen_4 = pygame.draw.rect(self.screen, "#c29f2e", (0, 75, 25, 650))
        list_reacts.append(screen_4)

        return list_reacts
