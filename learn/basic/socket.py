from socket import *
from time import ctime

# tcpSock = socket(AF_INET, SOCK_STREAM)
# udpSock = socket(AF_INET, SOCK_DGRAM)

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break

    print(data)
tcpCliSock.close()