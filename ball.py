import math
from config import *


def creation_ball_left(keys, count_balls_left, xp1, yp1, angle_left):
    if keys[pygame.K_q] and count_balls_left == 0:
        ball_x_left = 25 + xp1 + 25 * math.cos(math.radians(angle_left))
        ball_y_left = 25 + yp1 - 25 * math.sin(math.radians(angle_left))
        ball_dx_left = speed_ball * math.cos(math.radians(angle_left))
        ball_dy_left = speed_ball * -math.sin(math.radians(angle_left))
        count_balls_left = 0
        return ball_x_left, ball_y_left, ball_dx_left, ball_dy_left, count_balls_left
    else:
        return False


def creation_ball_right(keys, count_balls_right, xp2, yp2, angle_right):

    if keys[pygame.K_SEMICOLON] and count_balls_right == 0:
        ball_x_right = 25 + xp2 + 25 * math.cos(math.radians(angle_right + 180))
        ball_y_right = 25 + yp2 - 25 * math.sin(math.radians(angle_right + 180))
        ball_dx_right = speed_ball * math.cos(math.radians(angle_right + 180))
        ball_dy_right = speed_ball * -math.sin(math.radians(angle_right + 180))
        count_balls_right = 0
        aux = False
        return ball_x_right, ball_y_right, ball_dx_right, ball_dy_right, count_balls_right
    else:
        return False


def ball_death(count_ball):
    if count_ball > count_limit:
        count_ball = 0
        ball_x = -100
        ball_y = -100
        ball_dx = 0
        ball_dy = 0

        return count_ball, ball_x, ball_y, ball_dx, ball_dy
    else:
        return False
