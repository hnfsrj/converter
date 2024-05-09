import kivy
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


import socket
import threading


kivy.require('1.9.0')

HOST = socket.gethostbyname(socket.gethostname())
PORT = 7432

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((HOST,PORT))


class Interface(GridLayout):
    def __init__(self):
        super().__init__()

        self.cols = 1
        self.rows = 2

        self.add_widget(Label(text="application"))

        self.submit = Button(text="Wecheat:CLIENT")
        self.submit.bind(on_press=self.submitter)
        self.add_widget(self.submit)

    def submitter(self,instance):
        print("client sending msg")
        connection.send("hey".encode("utf-8"))

class Application(App):
    def build(self):
        return Interface()
    



def receiver():
    global connection

    while True:
        message = connection.recv(1024).decode("utf-8")
        print(message)

thread = threading.Thread(target=receiver)
thread.start()

if __name__=="__main__":
    Application().run()
