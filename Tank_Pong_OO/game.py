from tank import Tank
from config import *
from score import Score

pygame.init()


class Game:
    def __init__(self):
        # color balls
        self.player1_rect = pygame.Rect(50, 380, 50, 50)
        self.player2_rect = pygame.Rect(sc_width - 100, 380, 50, 50)

        self.bullets = []

        self.score_a = self.score_b = 0

        self.clock = pygame.time.Clock()
        self.game_loop = True

        self.tank_1 = Tank(0, self.player1_rect, "sprites/player1.png", green)
        self.tank_2 = Tank(180, self.player2_rect, "sprites/player2.png", blue)

    def run(self):
        score_1 = Score(self.score_a, 300, green)
        score_2 = Score(self.score_b, 700, blue)

        while self.game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.bullets.append(self.tank_1.shot_bullet())
                    if event.key == pygame.K_DOWN:
                        self.bullets.append(self.tank_2.shot_bullet())

            keys = pygame.key.get_pressed()

            # Move p1
            self.tank_1.control(keys, [pygame.K_w, pygame.K_a, pygame.K_d], 0)
            self.tank_1.draw()
            # Move p2
            self.tank_2.control(keys, [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], 1)
            self.tank_2.draw()

            # start shot
            for b in self.bullets:
                b.move()
                if b.get_data()[0] == -50:
                    self.bullets.remove(b)

                elif self.tank_1.player_death(b.get_data()):
                    self.score_a += 1
                    score_2.upload_score(self.score_a)
                    self.bullets.remove(b)

                elif self.tank_2.player_death(b.get_data()):
                    self.score_b += 1
                    score_1.upload_score(self.score_b)
                    self.bullets.remove(b)

            score_1.draw(screen)
            score_2.draw(screen)

            arena.draw_object()

            pygame.display.flip()
            screen.fill("#9f4100")
            self.clock.tick(150)


game = Game()
game.run()
