from socket import *
import threading
import random

def Random(socket):
    socket.send("Send two numbers seperated by a space\n".encode())
    tempMessage = socket.recv(1024).decode()
    tempMessage = tempMessage.strip().split(" ")
    num1 = float (tempMessage[0])
    num2 = float (tempMessage[1])
    return f"Your random number between {tempMessage[0]} and {tempMessage[1]} is {random.uniform(num1, num2)}"



def Add(socket):
    socket.send("Send two numbers seperated by a space\n".encode())
    tempMessage = socket.recv(1024).decode()
    tempMessage = tempMessage.strip().split(" ")
    return f"{tempMessage[0]} + {tempMessage[1]} = {float (tempMessage[0]) + float (tempMessage[1])}"


def Subtract(socket):
    socket.send("Send two numbers seperated by a space\n".encode())
    tempMessage = socket.recv(1024).decode()
    tempMessage = tempMessage.strip().split(" ")
    return f"{tempMessage[0]} - {tempMessage[1]} = {float (tempMessage[0]) - float (tempMessage[1])}"


def ContinuousService(socket):
    returnMessage = ""
    socket.send("Connection to the server established\n".encode())
    socket.send('Send "help" for  a list of commands\n'.encode())
    while True: 
        tempMessage = socket.recv(1024).decode('latin-1')

        commandReceiver = tempMessage.strip().lower()
        print(commandReceiver)
        match commandReceiver:
            case 'random':
                returnMessage = Random(socket)
            case 'add':
                returnMessage = Add(socket)
            case 'subtract':
                returnMessage = Subtract(socket)
            case 'exit':
                break
            case _ : 
                returnMessage = f'"{commandReceiver}" is not a recognized command\n'
        returnMessage += "\n"
        socket.send(returnMessage.encode('latin-1'))
    socket.send("Disconneting from server".encode())
    socket.close()


serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with {addr}")
    threading.Thread(target=ContinuousService, args=(connectionSocket,)).start()