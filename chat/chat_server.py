import socket
from threading import Thread
from datetime import datetime

host = 'localhost'
port = 25000

user_dict = {}

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)

    while True:
        client_sock, addr = sock.accept()

        Thread(target=client_handler, args=(client_sock, addr)).start()


def client_handler(client_sock, addr):

    client_sock.send(b'Chat Program' + bytes(str(datetime.now()), 'utf-8'))

    user_dict.update({addr : client_sock})

    while True:
        message = client_sock.recv(1600)
        for user_socket in user_dict.values():
            if message:
                user_socket.sendall(message)

server()
