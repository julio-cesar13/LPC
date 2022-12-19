import turtle 
from math import pi

def square(n, factor):
    first = 0 
    second = 1
    square_a = first 
    square_b = second 
    
    for i in range(3):
        t.forward(second* factor)
        t.left(90)
        
    t.forward(second*factor)    
    square_a, square_b = square_b,  square_a +square_b 
    
    for i in range(1, n):
        t.backward(square_a * factor)
        t.right(90)
        t.forward(square_b * factor)
        t.left(90)
        t.forward(square_b * factor)
        t.left(90)
        t.forward(square_b * factor)        
        square_a , square_b = square_b,  square_a + square_b 
        
    t.penup()
    t.home() 
    t. goto(factor, 0)
    t.left(90)
    t.pendown()   
    
    t.pencolor("green")
 
    for i in range(n):
        print(second)
        fdwd = pi * second* factor / 2
        fdwd /= 90
        for j in range(90):
            t.forward(fdwd)
            t.left(1)
        first , second = second , first + second
            
t = turtle. Turtle()
factor = 10
N = int(turtle.numinput("Numero de sequência","O Número digitado deve ser maior que 0"))
t.speed(100)
square(N, factor)
turtle.done()

                  