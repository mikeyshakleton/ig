import socket
from turtle import Screen, Turtle

screen = Screen()
screen.setup(500, 500)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

# Receive initial position from the server
initial_pos = client.recv(1024).decode()
x, y = map(int, initial_pos.split(','))

# Create a Turtle for the player
player = Turtle()
player.shape('square')
player.color('red')
player.penup()
player.goto(x, y)

# Example: Send player's new position to the server
new_pos = '150,150'
client.sendall(new_pos.encode())

screen.mainloop()

client.close()
