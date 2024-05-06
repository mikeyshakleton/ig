from turtle import *
import pyautogui

x,y = pyautogui.size()
m_x,m_y = pyautogui.position()

wn = Screen()
wn.setup(x,y)
wn.bgcolor("white")
wn.tracer(0)

player = Turtle()
player.shape("square")
player.color("red")
player.pu()
player.goto(0,-50)
player.dy = 0
player.dx = 0

ground1 = Turtle()
ground1.shape("square")
ground1.color("green")
ground1.pu()
ground1.goto(0,-150)
ground1.shapesize(5,40)

time = 0


      
speed1 = 1.9
speedx = 0
ground = False

def can_walk():
   global ground
   if speed1 == 0:
      ground = True
      

while True:
    m_x,m_y = pyautogui.position()
    ground1.setx(m_x)
    player.dx += speedx
    player.sety(player.ycor() + player.dy)
    player.setx(player.xcor() + player.dx)
    
    if player.ycor() < ground1.ycor() + 66:
        if speed1 > 0:
         player.dy *= -speed1
         speed1 -= 0.3
        elif speed1 < 1:
           speed1 = 0
    else:
        if speed1 > 0:
         player.dy -= 1
        elif speed1 < 1:
         player.dy = 0
        hi = False
    can_walk()
    m_x,m_y = pyautogui.position()
        
    wn.update()