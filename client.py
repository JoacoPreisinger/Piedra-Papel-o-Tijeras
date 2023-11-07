import socket
import random

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0,1'
    port = 12346
    client_socket.connect((host, port))

    while True:
        