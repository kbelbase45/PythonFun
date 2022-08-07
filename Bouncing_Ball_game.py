''' 
In this project, particles bounces in a box. A movement of the particles start as soon as 
the user clicks anywhere on the canvas. For this project I used four methods of the graphics engine. 
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
    ''' Define the size of box. The four corners of box are 
        (x_min,y_min),(x_min,y_max),(x_max,y_min),(x_max,y_max)'''
    
    x_min = 0
    y_min = 0
    x_max = 800
    y_max = 800
    return x_min, y_min, x_max, y_max

def window_configuration():
    ''' Set the appearance of the box like color, window name, etc.'''
    
    x_min, y_min, x_max, y_max = constants()
    canvas_window = GraphWin('Bouncing Ball by Kamal',x_max,y_max)
    canvas_window.setCoords(x_min,y_min,x_max,y_max)
    canvas_window.setBackground('gray')
    
    canvas_window.getMouse()
    
    label = Text(Point(380,20),'Two ball are bouncing')
    label.setTextColor('green')
    label.setStyle('bold italic') 
    label.setFace('helvetica')    
    label.setSize(20)             
    label.draw(canvas_window)         
    return canvas_window

def calculate_ranges_points(canvas_window,radius_of_ball):
    x_min, y_min, x_max, y_max = constants()
    
    xLow  = radius_of_ball
    yLow  = radius_of_ball
    xHigh = canvas_window.getWidth() - radius_of_ball
    yHigh = canvas_window.getHeight() - radius_of_ball

    x = random.randrange(xLow,xHigh+1)
    y = random.randrange(yLow,yHigh+1)
    
    return x,y

def get_random_center(canvas_window):
    radius_of_ball  = 10
    radius_of_ball1 = radius_of_ball+3
    
    x,y   = calculate_ranges_points(canvas_window,radius_of_ball)        
            
    x1,y1 = calculate_ranges_points(canvas_window,radius_of_ball1)
    
    return Point(x,y), Point(x1,y1), radius_of_ball, radius_of_ball1

def make_ball():    
    canvas_window  = window_configuration()
    center,center1, radius_of_ball, radius_of_ball1  = get_random_center(canvas_window)     
    ball           = Circle(center,radius_of_ball)
    ball1          = Circle(center1,radius_of_ball1)
    
    ball.setOutline('red')
    ball.setFill('blue')
    ball.draw(canvas_window)
    
    ball1.setOutline('blue')
    ball1.setFill('red')
    ball1.draw(canvas_window)    
    return ball,ball1, radius_of_ball, radius_of_ball1

def make_ball_move(dx,dy):
    dx1,dy1 = dx+2,dy-2
    ball,ball1, R, R1          = make_ball()
    x_min, y_min, x_max, y_max = constants()
    delay = 0.008
    for i in range(2000):
        ball.move(dx,dy)
        center = ball.getCenter()
        x_now  = center.getX()
        y_now  = center.getY()
                
        if x_now > (x_max - R) or x_now < R:
            dx = -dx
        if y_now > (y_max - R) or y_now < R:
            dy = -dy
        
        ball1.move(dx1,dy1)
        center1 = ball1.getCenter()
        x1_now  = center1.getX()
        y1_now  = center1.getY()                

        if x1_now > (x_max - R1 ) or x1_now < R1:
            dx1 = -dx1
        if y1_now > (y_max - R1 ) or y1_now < R1:
            dy1 = -dy1
        
        if x_now == x1_now and y_now == y1_now:
            print(' Case exist')
        
        time.sleep(delay)  #delay is in second   



if __name__=='__main__':
    make_ball_move(3,5)




    
