import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

print("Waiting for a connection...")

client, address = server.accept()
print(f"Connection from {address} has been established!")

# Send initial position to the client
client.sendall(b'100,100')

while True:
    # Receive and process data from the client
    data = client.recv(1024)
    if not data:
        print("lost connectetion")
        break
    # Process data here as needed

client.close()
server.close()
