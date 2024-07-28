import socket

# Enter the host's ip address i.e 192.168.1.2
HOST = "ip address"

# Alternatively use the following to get the hosts' ip address automatically
# host = socket.gethostbyname("hostname")

# Choose a port not one of the well-known:)
PORT = "Port number"

# create a socket object. AF_INET tells it's Ipv4 while SOCK_STREAM defines the TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the ip address and port number

server.bind((HOST, PORT))

# server listens to incoming connections from clients

server.listen()

# Handle incoming connections

while True:
    connect_server, address = server.accept()
    print(f"Connected to {address}")
    message = connect_server.recv(1024).decode('utf-8')
    print(f"Message received is {message}")
    connect_server.send("Got your message").decode('utf-8')

    connect_server.close()

    print("Connection with {address} closed!")

