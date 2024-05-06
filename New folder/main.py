from turtle import *
import pyautogui
import tkinter as tk
from PIL import Image
import pygame

wnx,wny=pyautogui.size()



pygame.mixer.init()

e = Image.open("assets/bar.gif")
q = e.resize((1920,300),resample=Image.LANCZOS)
q.save("assets/bar.gif")

e = Image.open("assets/nerd.gif")
q = e.resize((150,150),resample=Image.NEAREST)
q.save("assets/nerd1.gif")

e = Image.open("assets/nerd.gif")
q = e.resize((300,300),resample=Image.NEAREST)
q.save("assets/nerd2.gif")

e = Image.open("assets/button.gif")
nerdw,nerdh = e.size


e = Image.open("assets/bg.png")
q = e.resize((wnx,wny),resample=Image.LANCZOS)
q.save("assets/bg.png")

e = Image.open("assets/human.gif")
q = e.resize((50,50),resample=Image.LANCZOS)
human_wid,human_hei = q.size
q.save("assets/human.gif")

def play():
  if running:
    pygame.mixer.music.load("music/starter.mp3")
    pygame.mixer.music.play(loops=0)





wn = Screen()
canvas = wn.getcanvas()
wn._root.overrideredirect(10)
wn.bgpic("assets/bg.png")
wn.tracer(0)
wn.setup(wnx,wny)
canvas.config(bd=0, highlightthickness=0)

q = "assets/"

running = True

play()

wn.addshape(f"{q}amogus.gif")
wn.addshape(f"{q}bar.gif")
wn.addshape(f"{q}bird.gif")
wn.addshape(f"{q}button.gif")
wn.addshape(f"{q}button1.gif")
wn.addshape(f"{q}character.gif")
wn.addshape(f"{q}click.gif")
wn.addshape(f"{q}click1.gif")
wn.addshape(f"{q}connecter.gif")
wn.addshape(f"{q}cool.gif")
wn.addshape(f"{q}dedbutton.gif")
wn.addshape(f"{q}hi.gif")
wn.addshape(f"{q}human.gif")
wn.addshape(f"{q}nerd.gif")
wn.addshape(f"{q}nerd1.gif")
wn.addshape(f"{q}nerd2.gif")
wn.addshape(f"{q}player.gif")
wn.addshape(f"{q}robot.gif")
wn.addshape(f"{q}verbar.gif")
wn.addshape(f"{q}human1.gif")

bar = Turtle()
wn.addshape("assets/bar.gif")
bar.shape("assets/bar.gif")
bar.pu()

player = Turtle()
wn.addshape("assets/human.gif")
player.shape("assets/human.gif")
player.pu()

node = Turtle()
wn.addshape("assets/click.gif")
node.shape("assets/click.gif")
node.pu()
node.goto(-600,300)



bar.goto(0,-wny/2 + 150)

verbar = Turtle()
wn.addshape("assets/verbar.gif")
verbar.shape("assets/verbar.gif")
verbar.pu()
verbar.ht()
verbar.goto(wnx/2 - 240 ,0)

button = Turtle()
button.shape("assets/button.gif")
button.pu()
button.goto(-400,-390)

planet_clone = Turtle()
wn.addshape("assets/nerd1.gif")
planet_clone.shape("assets/nerd1.gif")
planet_clone.pu()
planet_clone.goto(-400,-390)

click1 = 0

def clicked(x,y):
   global click1
   if -nerdw/2 + button.xcor() <= x <= nerdw/2 + button.xcor() and -nerdh/2 + button.ycor() <= y <= nerdh/2 + button.ycor():
      player.shape(f"{q}nerd.gif")
      click1 = 1
   elif click1 == 1:
      player.goto(x,y)

wn.onclick(clicked)


while running:
    
   wn.update()

