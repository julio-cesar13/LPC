from turtle import *       

def tree(sz, level):   
    
    if level > 0:
        colormode(255)       
        pencolor(0, 255//level, 0)         
        forward(sz)  
        right(angle)
        
        tree(0.8 * sz, level-1)
          
        pencolor(0, 255//level, 0)         
        left( 2 * angle )
  
        tree(0.8 * sz, level-1)
          
        pencolor(0, 255//level, 0)         
        right(angle)
        backward(sz)          

speed(100)  
left(90)
angle = 30

tree(80,7)

done()