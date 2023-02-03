from config import *
import math


def load_images(sprite, ang, w, h, xp, yp, image):
    sprite.image = pygame.image.load(image)
    sprite.image = pygame.transform.scale(sprite.image, (w, h))
    sprite.image = pygame.transform.rotate(sprite.image, ang)
    sprite.rect = sprite.image.get_rect(center=(xp + 25, yp + 25))


def detection_collision(player):
    rect = arena.draw_object()
    detection = []
    for x in rect:
        detection.append(x.colliderect(player))
    if True in detection:
        return False
    else:
        return True


def collision_objects(obj, obj_2):
    angle_left, rect_1 = obj[0], obj[1]
    angle_right, rect_2 = obj_2[0], obj_2[1]
    # players collide with objects
    collision_1 = pygame.sprite.Sprite()
    load_images(collision_1, angle_left, 10, 50,
                rect_1.x + 30 * math.cos(math.radians(-angle_left)),
                rect_1.y + 30 * math.sin(math.radians(-angle_left)), "sprites/collision_object.png")

    collision_2 = pygame.sprite.Sprite()
    load_images(collision_2, angle_right, 10, 50, rect_2.x - 30 * math.sin(math.radians(angle_right - 90)),
                rect_2.y - 30 * math.cos(math.radians(angle_right - 90)), "sprites/collision_object.png")

    if detection_collision(collision_1):
        per_1 = True
    else:
        per_1 = False

    # collision player 2 with objects
    if detection_collision(collision_2):
        per_2 = True
    else:
        per_2 = False

    return per_1, per_2
