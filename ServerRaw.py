from socket import *
import threading


def RequestHandler(socket, requst):
    if requst == 'help':
        socket.send('Random'.encode())

serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with {addr}")
    socket.send("Connection to the server established\n".encode())
    socket.send('Send "help" for  a list of commands\n'.encode())
    request = socket.recv(1024).decode()
    threading.Thread(target=RequestHandler, args=(connectionSocket, request,)).start()