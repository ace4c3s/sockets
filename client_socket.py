#This implements a socket creation in the client side

import socket

# Specifify the server's ip address
HOST = "server's ip address"

# Specifify the server's port to connect to 
PORT = "port number"

# Create a socket object 
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
socket.connect((HOST, PORT))

# Encode the message to send 
socket.send("Hello There!".encode('utf-8'))

# Print the message from the server to verify connection
print(socket.recv(1024))