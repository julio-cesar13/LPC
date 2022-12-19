import turtle
import random

turtle.bgcolor("black")


def match(player, die):
    player_one_turn = input("Pressione 'Enter' para rolar o dado:")
    die_outcome = random.choice(die)
    print("O resultado do dado: ")
    print(die_outcome)
    print("O numero de passos será: ")
    print(20 * die_outcome)
    player.forward(20 * die_outcome)


def creation_player(color):
    x = turtle.Turtle()
    x.color(color)
    x.shape("turtle")
    return x


def creation_space(position, player):
    player.goto(position)
    player.pendown()
    player.circle(30)
    player.penup()


player_one = creation_player("green")
player_one.penup()
player_two = creation_player("blue")
player_two.penup()
creation_space((300, 70), player_one)
player_one.goto(-200, 100)
creation_space((300, -130), player_two)
player_two.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if player_one.pos() >= (290, 100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (290, -100):
        print("Player Two Wins!")
        break
    else:
        match(player_one, die)
        match(player_two, die)