import socket

def main():
    hst = '0.0.0.0'
    port = 12345

    s = socket.socket(socket.AF_NET, socket.SOCK_STREAM)

    s.bind host, port

    s.listen(1)
    print("En attente d'une connexion...")

    conn, addr = s.accept
    print(f"Connexion de {addr")

    while True:
        data = conn.recv(1024).decode('utf-8')

        print(f"Reçu de {addr}: {data}")
        message = input("Votre message: ")
        conn.send(message.encode('utf-8'))

    s.close()

if __name__ == "__main__":
    main()
