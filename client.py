import socket
import random
from getpass import getpass

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.2'
    port = 12346
    client_socket.connect((host, port))

    while True:
        jugada_cliente = getpass(f"Eleji una opcion:\n1.Piedra \n2.Papel \n3.Tijeras")
        if jugada_cliente > "3"or jugada_cliente < "1":
            print("Opción incorrenta, vuelva a seleccionar otra opcíon\n")
            continue
        client_socket.sendall(jugada_cliente.encode('utf-8'))
        data2 = client_socket.recv(1024)
        respuesta = data2.decode('utf-8')
        print(respuesta)


if __name__ == "__main__":
    main()