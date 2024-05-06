import turtle
from tkinter import *
from PIL import Image
import pyautogui
import pygame

pygame.mixer.init()# initialise the pygame
 
open = False

x,y = pyautogui.size()

q = Image.open("platform.gif")
w = q.resize((x-7,y-981),resample=Image.LANCZOS)
w.save("platform.gif")

q = Image.open("bg.gif")
w = q.resize((x,y),resample=Image.LANCZOS)
w.save("bg.gif")

e = Image.open("present.gif")
p_w,p_h = e.size
print(p_w,p_h)

p = Image.open("anvil.gif")
a_w,a_h = p.size
print(a_w,a_h)

wn = turtle.Screen()
wn._root.overrideredirect(10)
wn.setup(x,y)
wn.tracer(0)
canvas = wn.getcanvas()

canvas.config(bd=0,highlightthickness=0)

images = ["anvil.gif","bg.gif","box.gif","broken_sword1.gif","christmas tree.gif","hotbar.gif","inventory.gif","mail.gif","message.gif","platform.gif","present.gif","pressE.gif","sink.gif","sprite.gif","sprite1.gif","sprite2.gif","sprite3.gif","sword1.gif"]
for i in images:
 wn.addshape(i)

bg = turtle.Turtle()
bg.shape("bg.gif")
bg.goto(0,0)



press = turtle.Turtle()
press.shape("pressE.gif")
press.hideturtle()
press.goto(0,0)

hotbar = turtle.Turtle()
hotbar.shape("hotbar.gif")
hotbar.pu()
hotbar.goto(-40,-150)

tree = turtle.Turtle()
tree.shape("christmas tree.gif")
tree.pu()
tree.speed(0)
tree.goto(600,-170)

anvil = turtle.Turtle()
anvil.shape("anvil.gif")
anvil.pu()
anvil.speed(0)
anvil.goto(-100,-280)

sink = turtle.Turtle()
sink.shape("sink.gif")
sink.pu()
sink.speed(0)
sink.goto(-600,-250)

present = turtle.Turtle()
present.shape("present.gif")
present.pu()
present.speed(0)
present.goto(500,-265)

player = turtle.Turtle()
player.shape("sprite.gif")
player.pu()
player.speed(0)
player.goto(0,-250)

platform = turtle.Turtle()
platform.shape("platform.gif")
platform.pu()
platform.speed(0)
platform.goto(-5,-345)



inventory = turtle.Turtle()
inventory.shape("inventory.gif")
inventory.pu()
inventory.speed(0)
inventory.goto(0,-445)

def collision():
   global open
   if player.distance(present) < 64:
       open = True
   else:
      open = False
    
def states():
   if open == True:
      press.showturtle()
   else:
      press.hideturtle()

def bye():
    global run
    run = False
def left():
   x = player.xcor()
   x -= 10
   player.setx(x)
def right():
   x = player.xcor()
   x += 10
   player.setx(x)
wn.listen()

run = True
wn.onkeypress(bye,"q")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")

while run:
    collision()
    states()
    print(open)
    wn.update()
