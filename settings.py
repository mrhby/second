from socket import *
from time import ctime

HOST = ' '
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST , PORT)

tc = socket(AF_INET, SOCK_STREAM)
tc.bind(ADDR)
tc.listen(5)

while True:
	print('waiting for connection...')
	tcp, addr = tc.accept()
	print('...connection from : ' , addr)
	while True:
		data = tcp.recv(BUFSIZ)
        tcp.send('[%s] %s' % (bytes(ctime(),'utf-8'),data))
    tcp.close()
tp.close()
