from tank import Tank
from collision import collision_objects
from config import *
from score import Score

pygame.init()


class Game:
    def __init__(self):
        # color balls
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.xp1 = 50
        self.yp1 = 380
        self.xp2 = sc_width - 100
        self.yp2 = 380

        self.ang_left = 0

        self.per_1 = False
        self.per_2 = False

        self.bullets = []

        self.score_a = self.score_b = 0

        self.clock = pygame.time.Clock()
        self.game_loop = True

        self.tank_1 = Tank(0, 50, 50, self.xp1, self.yp1, "sprites/player1.png", (0, 255, 0))
        self.tank_2 = Tank(180, 50, 50, self.xp2, self.yp2, "sprites/player2.png", (0, 0, 255))

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

            # players collide with objects
            per_1 = collision_objects(self.tank_1.get_information(), self.tank_2.get_information())[0]
            per_2 = collision_objects(self.tank_1.get_information(), self.tank_2.get_information())[1]

            # Move p1
            self.tank_1.move_left(keys, per_1)
            self.tank_1.draw()

            # Move p2
            self.tank_2.move_right(keys, per_2)
            self.tank_2.draw()

            # start shot
            for b in self.bullets:
                b.move()
                if b.trash() == -50:
                    self.bullets.remove(b)
                elif self.tank_1.player_death(b.get()):
                    self.score_a += 1
                    score_2.upload_score(self.score_a)
                    self.bullets.remove(b)
                elif self.tank_2.player_death(b.get()):
                    print(b.get())
                    self.score_b += 1
                    score_1.upload_score(self.score_b)
                    self.bullets.remove(b)

            score_1.draw(screen)
            score_2.draw(screen)

            arena.draw_object()

            pygame.display.flip()
            screen.fill("#9f4100")
            self.clock.tick(100)


game = Game()
game.run()
