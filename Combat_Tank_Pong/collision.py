from config import *
import math
from draw_screen import draw_object
from move import load_images


def collision_objects(angle_left, angle_right, xp1, xp2, yp1, yp2):
    # players collide with objects
    collision_1 = pygame.sprite.Sprite()
    load_images(collision_1, angle_left, 10, 50,
                xp1 + 30 * math.cos(math.radians(-angle_left)),
                yp1 + 30 * math.sin(math.radians(-angle_left)), "sprites/collision_object.png")

    collision_2 = pygame.sprite.Sprite()
    load_images(collision_2, angle_right, 10, 50, xp2 - 30 * math.sin(math.radians(angle_right + 90)),
                yp2 - 30 * math.cos(math.radians(angle_right + 90)), "sprites/collision_object.png")

    if draw_object(collision_1):
        per_1 = True
    else:
        per_1 = False

    # collision player 2 with objects
    if draw_object(collision_2):
        per_2 = True
    else:
        per_2 = False

    return per_1, per_2


def collision_ball(ball, ball_x, ball_y, ball_dx, ball_dy):
    if not draw_object(ball):
        ball_dy *= -1
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy
        ball = (ball_x, ball_y, 5, 5)
        if not draw_object(ball):
            ball_dx *= -1
            ball_dy *= -1
        return ball_dx, ball_dy


def player_death(ball, player, score, count_ball, angle, xp, yp):
    if ball.colliderect(player):
        score += 1
        count_ball += count_limit
        ang = 10
        death_count = 0
        while death_count <= 144:
            if death_count == 144:
                if score % 2 == 0 and score != 0:
                    yp = 100
                    angle = 0
                elif score % 2 == 1 and score != 0:
                    yp = 650
                    angle = 0

            death_count += 1
            angle += ang
        return score, count_ball, ang, death_count, xp, yp, angle

    else:
        return False
