############################################### Server
import socket

host = '127.0.0.1'
port = 9991

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print("Server started at port ", port)

while True:
    client, address = server.accept()
    print("Connected with {}".format(str(address)))
    client.send('Accept'.encode('ascii'))
    data = client.recv(1024).decode('ascii')
    client.send('Connected to server!'.encode('ascii'))
    print(data)


