import socket
import threading
from datetime import datetime

host = 'localhost'
port = 25000

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((host, port))

    print(sock.recv(1600))

    sock.send(bytes(input('>'), 'utf-8'))

    print(sock.recv(1600))


    sock.close()


client()
