from socket import *

HOST = '::1'
BUFSIZ = 1024
PORT = 21567
ADDR  = (HOST, PORT)

tcp = socket(AF_INET6, SOCK_STREAM)
tcp.connect(ADDR)

while True:
    data = input('> ')
    if not data:
    	break
    tcp.send(data)
    data = tcp.recv(BUFSIZ)
    if not data:
    	break
    print(data.decode('utf-8'))
tcp.close()





