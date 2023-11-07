import socket
import threading
import random

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        opciones = ["piedras", "papel", "tijeres"]
        jugada_server = random.choice(opciones)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.2'
    port = 12346
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()