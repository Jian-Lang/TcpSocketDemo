from socket import *
serverName = "DESKTOP-1TLE6PJ"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input Sentence')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server:',modifiedSentence.decode())
clientSocket.close()