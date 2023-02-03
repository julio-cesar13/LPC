import math
from config import *
from collision import detection_collision


class Bullet:
    def __init__(self, xp, yp, angle, color_bullet):
        self.count = 0
        self.angle = angle
        self.rect = pygame.Rect(25 + xp + 25 * math.cos(math.radians(self.angle)),
                                25 + yp - 25 * math.sin(math.radians(self.angle)), 5, 5)
        self.dx = speed_ball * math.cos(math.radians(self.angle))
        self.dy = speed_ball * -math.sin(math.radians(self.angle))
        self.color = color_bullet

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        if not detection_collision(self.rect):
            self.dy *= -1
            x = self.rect.x + self.dx
            y = self.rect.y + self.dy
            rect = pygame.Rect(x, y, 5, 5)
            self.count += 1
            if not detection_collision(rect) and not (self.rect.x == -50):
                self.dx *= -1
                self.dy *= -1
                self.rect.x = self.rect.x + self.dx * 2

        if self.count > count_limit:
            self.rect = pygame.Rect(-50, 0, 5, 5)

        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
        self.draw()

    def trash(self):
        return self.rect.x

    def get(self):
        return self.rect, self.count, self.color
