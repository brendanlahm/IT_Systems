############################################### Client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9991))

client.send("hello".encode('ascii'))

while(client):
    print("Awaiting Message...")
    message = client.recv(1024).decode('ascii')
    print(message)

client.close()


