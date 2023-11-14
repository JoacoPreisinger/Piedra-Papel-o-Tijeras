import socket
import threading
from getpass import getpass

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        jugada_servidor = getpass(f"Eleji una opcion:\n1.Piedra \n2.Papel \n3.Tijeras")
        jugada_cliente = data.decode('utf-8')
        while jugada_servidor > "3" or jugada_servidor < "1":
            print("Opcion incorrecta, vuelva a elejir otra opción\n")
            jugada_servidor = getpass(f"Eleji una opcion:\n1.Piedra \n2.Papel \n3.Tijeras")
        
        if jugada_servidor == jugada_cliente:
            print(f"¡Empate!\n")
            responder = "¡Empate!\n"
        elif  jugada_cliente == "2":
            if jugada_servidor == "1":
                print("¡Perdiste!\n")
                responder = "¡Ganaste!\n"
            else:
                print("¡Ganaste!\n")
                responder = "¡Perdiste!\n"
        elif jugada_cliente == "3":
            if jugada_servidor == "2":
                print("¡Perdiste!\n")
                responder = "¡Ganaste!\n"
            else:
                print("¡Ganaste!\n")
                responder = "¡Perdiste!\n"
        elif jugada_cliente == "1":
            if jugada_servidor == "3":
                print("¡Perdiste!\n")
                responder = "¡Ganaste!\n"
            else:
                print("¡Ganaste!\n")
                responder = "¡Perdiste!\n"
                
        client_socket.sendall(responder.encode('utf-8'))
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