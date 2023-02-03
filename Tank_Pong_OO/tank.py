from config import *
from bullet import Bullet
import math


class Tank:
    def __init__(self, ang, w, h, xp, yp, image, color_bullet):
        self.ang = ang
        self.w = w
        self.h = h
        self.xp = xp
        self.yp = yp
        self.image = pygame.image.load(image)
        self.surface = pygame.transform.scale(self.image, (self.w, self.h))
        self.rotated = pygame.transform.rotate(self.image, self.ang)
        self.rect = self.image.get_rect(center=(self.xp + 25, self.yp + 25))
        self.bullets = 0
        self.count = 0
        self.color_bullet = color_bullet

    def shot_bullet(self):
        self.bullets = Bullet(self.xp, self.yp, self.ang, self.color_bullet)
        return self.bullets

    def move(self, keys, player_keys, permission):
        if keys[player_keys[0]] and permission:
            self.xp += math.cos(math.radians(self.ang))
            self.yp -= math.sin(math.radians(self.ang))
            self.draw()

        elif keys[player_keys[1]]:
            self.ang += 1
            self.draw()

        elif keys[player_keys[2]]:
            self.ang += -1
            self.draw()

    def move_left(self, keys, permission_1):
        # Move p1
        self.move(keys, [pygame.K_w, pygame.K_a, pygame.K_d], permission_1)

    def move_right(self, keys, permission_2):
        # Move p2
        self.move(keys, [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], permission_2)

    def draw(self):
        self.surface = pygame.transform.scale(self.surface, (self.w, self.h))
        self.rotated = pygame.transform.rotate(self.surface, self.ang)
        self.rect = self.rotated.get_rect(center=(self.xp + 25, self.yp + 25))
        screen.blit(self.rotated, self.rect)

    def get_information(self):
        return self.ang, self.rect

    def player_death(self, ball):
        ball, count_ball, color_bullet = ball[0], ball[1], ball[2]
        if ball.colliderect(self.rect) and color_bullet != self.color_bullet:
            self.count += 1
            count_ball += count_limit
            ang = 1
            self.ang = 0
            death_count = 0
            while death_count <= 720:
                if death_count == 720:
                    if self.count % 2 == 0 and self.count != 0:
                        self.yp = 100
                    elif self.count % 2 == 1 and self.count != 0:
                        self.yp = 650

                death_count += 1
                self.ang += ang

            return True
        return False
