from socket import *

from time import ctime
import threading

HOST = ''
PORT = 21568
BUFSIZ = 20000
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

# Starts the server and creates a thread to handle clients
def startServer():
    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...connected from:', addr)

        miniserver = disposableServer(tcpCliSock, addr)
        miniserver.start()
    tcpSerSock.close()

# A mini server to communicate with the client
class disposableServer(threading.Thread):
    def __init__(self,tcpCliSock, addr):
        threading.Thread.__init__(self)
        self.tcpCliSock = tcpCliSock
        self.addr = addr

    def run(self):
        self.listen()

    def listen(self):
        sfile = open("icon.png", "rb")
        bytedata = sfile.read()
        sfile.close()
        while True:
            self.tcpCliSock.send(bytes('[%s]' % (ctime()), 'utf-8'))  # Send the timestamp
            self.tcpCliSock.send(bytedata)  # Send the image as bytes

        self.tcpCliSock.close()


if __name__ == '__main__':
    startServer()
