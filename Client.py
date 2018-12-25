from socket import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Function that communicates with the server
def connectToServer():
    HOST = '127.0.0.1'
    PORT = 21568
    BUFSIZ = 20000
    ADDR = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    msg = ""

    while True:
        time = tcpCliSock.recv(1024)
        data = tcpCliSock.recv(BUFSIZ)
        with open('client-icon.png','wb') as f:
            f.write(data)
        msg = 'Received image from Server @ ' + time.decode('utf-8')
        break
    tcpCliSock.close()
    return msg

# Class that creates the App
class clientApp(App):
    def build(self):
        return super().build()

# Class that displays the data from the server
class client(BoxLayout):
    def showData(self):
        self.ids['msg'].text = 'Connected to Server'
        data = connectToServer()
        self.ids['msg'].text = data

if __name__ == '__main__':
    clientApp().run()
