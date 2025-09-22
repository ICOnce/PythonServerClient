from socket import *
import threading

def Listener(socket):
    while True:
        response = socket.recv(1024).decode()
        print(f'Response from server: {response}')

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', 12345))
threading.Thread(target=Listener, args=(clientSocket,)).start()
while True:
    request = input()
    clientSocket.send(request.encode())
    if request.lower() == 'exit':
        print('Exiting client.')
        break
clientSocket.close()