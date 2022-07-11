''' 
In this project, a circular ball bounces around a screen. A movement of the ball starts as soon as 
a user clicks anywhere on the canvas. For this project I used four methods of the graphics engine. 
The source code can be viewed in ~/.local/python3.6/site-packages/graphics.py depending on the operating system.

The constants function has parameters useful for setting up a canvas.

The window_configuration function sets up the appearance of the canvas. When canvas_window.getMouse() is annotated
in this section, no user click is required to start the movement. Internally, the coordinates of the window run from
(x_min,y_min) in the lower left corner to (x_max,y_max) in the upper right corner. Four options of 
['bold','normal','italic', 'bold italic'] are possible in label.setStyle. Four fonts from 
['helvetica','arial','courier','times roman'] are possible in setFace. For the font size, the possible range is 5 <= size <= 36.

The get_random_center() is supposed to randomly assign the center of the ball on the canvas.
The make_ball function is responsible for designing the look of the ball. Finally, the make_ball_move function controls 
the ball's motion so that when the ball hits the walls, it bounces back onto the canvas. The walls look like ridges. 
The bounce conditions are specified within the if statement.

The ball movement and how long the time interval between two movements is are controlled with the parameters delay 
and value within range function.
'''
    
from graphics import GraphWin, Text, Point, Circle    
import time, random


def constants():
    x_min = 0
    y_min = 0
    x_max = 800
    y_max = 800
    return x_min, y_min, x_max, y_max

def window_configuration():
    x_min, y_min, x_max, y_max = constants()
    canvas_window = GraphWin('Bouncing Ball',x_max,y_max)
    canvas_window.setCoords(x_min,y_min,x_max,y_max)
    canvas_window.setBackground('gray')
    
    canvas_window.getMouse()
    
    label = Text(Point(x_max/2,20),'Bouncing Ball by Kamal')
    label.setTextColor('white')
    label.setStyle('bold italic') 
    label.setFace('helvetica')    
    label.setSize(25)             
    label.draw(canvas_window)         
    return canvas_window

def get_random_center():
    x_min, y_min, x_max, y_max = constants()
    x = random.randrange(x_min,x_max+1)
    y = random.randrange(y_min,y_max+1)
    return Point(x,y)

def make_ball():
    radius_of_ball = 10
    center         = get_random_center() 
    canvas_window  = window_configuration()
    ball           = Circle(center,radius_of_ball)
    ball.setOutline('red')
    ball.setFill('blue')
    ball.draw(canvas_window)
    return ball

def make_ball_move(dx,dy):
    ball = make_ball()
    x_min, y_min, x_max, y_max = constants()
    delay = 0.002
    for i in range(1000):
        ball.move(dx,dy)
        center = ball.getCenter()
        x_now  = center.getX()
        y_now  = center.getY()
        if x_now > x_max or x_now < x_min:
            dx = -dx
        if y_now > y_max or y_now < y_min:
            dy = -dy
        time.sleep(delay)  #delay is in second   



if __name__=='__main__':
    make_ball_move(3,5)




    
