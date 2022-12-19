import turtle

def triangle(x,y):
        t.penup()
        
        t.goto(x,y)
        
        t.pendown()
        
        t.forward(100)
        for i in range(2):
            t.left(120)
            t.forward(200)
        t.left(120)
        t.forward(100)
                 
t = turtle.Turtle()  
turtle.onscreenclick(triangle,1)
turtle.listen()
turtle.done()   