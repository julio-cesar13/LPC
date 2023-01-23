from ball import creation_ball_left, creation_ball_right, ball_death
from draw_screen import draw_object
from move import move_left, move_right, load_images
from collision import collision_objects, collision_ball, player_death
from config import *

pygame.init()

# color balls
green = (0, 255, 0)
blue = (0, 0, 255)

# score´s
score1 = 0
score2 = 0

# Score (player 1)
score_point_player1 = font.render("0", True, green)
score_point_player1_rect = score_point_player1.get_rect()
score_point_player1_rect.center = (sc_width / 4, 25)

# Score (player 2)
score_point_player2 = font.render("0", True, blue)
score_point_player2_rect = score_point_player2.get_rect()
score_point_player2_rect.center = (3 * sc_width / 4, 25)

# ball from left tank
ball_x_left = -5
ball_y_left = -5
ball_dx_left = 0
ball_dy_left = 0
ball_left = pygame.draw.rect(screen, green, (ball_x_left, ball_y_left, 5, 5))
count_balls_left = 0

# ball from right tank
ball_x_right = -5
ball_y_right = -5
ball_dx_right = 0
ball_dy_right = 0
ball_right = pygame.draw.rect(screen, green, (ball_x_right, ball_y_right, 5, 5))
count_balls_right = 0

# Load images
player1 = pygame.sprite.Sprite()
player2 = pygame.sprite.Sprite()

xp1 = 50
yp1 = 380
xp2 = sc_width - 100
yp2 = 380
radius = 25 * (2 ** 0.5)

ang_left = 0
ang_left_death = 0
left_death_count = 0

per_1 = False
per_2 = False

ang_right = 0
ang_right_death = 0
right_death_count = 0

clock = pygame.time.Clock()
game_loop = True

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    load_images(player1, ang_left, 50, 50, xp1, yp1, "sprites/player1.png")
    load_images(player2, ang_right, 50, 50, xp2, yp2, "sprites/player2.png")
    player2.image = pygame.transform.rotate(player2.image, 180)

    # players collide with objects
    per_1 = collision_objects(ang_left, ang_right, xp1, xp2, yp1, yp2)[0]
    per_2 = collision_objects(ang_left, ang_right, xp1, xp2, yp1, yp2)[1]

    # Move p1
    if move_left(keys, per_1, xp1, yp1, ang_left):
        xp1 = move_left(keys, per_1, xp1, yp1, ang_left)[0]
        yp1 = move_left(keys, per_1, xp1, yp1, ang_left)[1]
        ang_left = move_left(keys, per_1, xp1, yp1, ang_left)[2]

    # Move p2
    if move_right(keys, per_2, xp2, yp2, ang_right):
        xp2 = move_right(keys, per_2, xp2, yp2, ang_right)[0]
        yp2 = move_right(keys, per_2, xp2, yp2, ang_right)[1]
        ang_right = move_right(keys, per_2, xp2, yp2, ang_right)[2]

    # start player 1 ball
    elif creation_ball_left(keys, count_balls_left, xp1, yp1, ang_left):
        ball_x_left = creation_ball_left(keys, count_balls_left, xp1, yp1, ang_left)[0]
        ball_y_left = creation_ball_left(keys, count_balls_left, xp1, yp1, ang_left)[1]
        ball_dx_left = creation_ball_left(keys, count_balls_left, xp1, yp1, ang_left)[2]
        ball_dy_left = creation_ball_left(keys, count_balls_left, xp1, yp1, ang_left)[3]
        count_balls_left = creation_ball_left(keys, count_balls_left, xp1, yp1, ang_left)[4]
        ball_left = pygame.draw.rect(screen, green, (ball_x_left, ball_y_left, 5, 5))

    # start player 2 ball
    elif creation_ball_right(keys, count_balls_right, xp2, yp2, ang_right):
        ball_x_right = creation_ball_right(keys, count_balls_right, xp2, yp2, ang_right)[0]
        ball_y_right = creation_ball_right(keys, count_balls_right, xp2, yp2, ang_right)[1]
        ball_dx_right = creation_ball_right(keys, count_balls_right, xp2, yp2, ang_right)[2]
        ball_dy_right = creation_ball_right(keys, count_balls_right, xp2, yp2, ang_right)[3]
        count_balls_right = creation_ball_right(keys, count_balls_right, xp2, yp2, ang_right)[4]
        ball_right = pygame.draw.rect(screen, blue, (ball_x_right, ball_y_right, 5, 5))

    # check ball collisions with objects
    if collision_ball(ball_left, ball_x_left, ball_y_left, ball_dx_left, ball_dy_left):
        count_balls_left += 1
        ball_dx_left = collision_ball(ball_left, ball_x_left, ball_y_left, ball_dx_left, ball_dy_left)[0]
        ball_dy_left = collision_ball(ball_left, ball_x_left, ball_y_left, ball_dx_left, -ball_dy_left)[1]

    # check ball collisions with objects
    if collision_ball(ball_right, ball_x_right, ball_y_right, ball_dx_right, ball_dy_right):
        count_balls_right += 1
        ball_dx_right = collision_ball(ball_right, ball_x_right, ball_y_right, ball_dx_right, ball_dy_right, )[0]
        ball_dy_right = collision_ball(ball_right, ball_x_right, ball_y_right, ball_dx_right, -ball_dy_right, )[1]

    # check ball collision with player 2
    if player_death(ball_left, player2, score1, count_balls_left, ang_right, sc_width - 100, yp2):
        score1, count_balls_left, ang_right_death, right_death_count, xp2, yp2, ang_right = player_death(
            ball_left, player2, score1, count_balls_left, ang_right, xp2, yp2)

    # check ball collision with player 1
    if player_death(ball_right, player1, score2, count_balls_right, ang_left, 50, yp1):
        score2, count_balls_right, ang_left_death, left_death_count, xp1, yp1, ang_left = player_death(
            ball_right, player1, score2, count_balls_right, ang_left, xp1, yp1)

    if ball_death(count_balls_right):
        count_balls_right, ball_x_right, ball_y_right, ball_dx_right, ball_dy_right = ball_death(count_balls_right)

    if ball_death(count_balls_left):
        count_balls_left, ball_x_left, ball_y_left, ball_dx_left, ball_dy_left = ball_death(count_balls_left)

    ball_x_left = ball_x_left + ball_dx_left
    ball_y_left = ball_y_left + ball_dy_left

    ball_x_right = ball_x_right + ball_dx_right
    ball_y_right = ball_y_right + ball_dy_right

    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)

    score_point_player1 = font.render(str(score1), True, (0, 255, 0))
    score_point_player2 = font.render(str(score2), True, (0, 0, 255))

    screen.blit(score_point_player1, score_point_player1_rect)
    screen.blit(score_point_player2, score_point_player2_rect)

    ball_left = pygame.draw.rect(screen, green, (ball_x_left, ball_y_left, 5, 5))
    ball_right = pygame.draw.rect(screen, blue, (ball_x_right, ball_y_right, 5, 5))

    draw_object(player1.rect)

    pygame.display.flip()
    screen.fill("#9f4100")
    clock.tick(150)
