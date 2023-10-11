import socket

def main():
    host = '192.168.1.X'  
    port = 12345

    s = socket.create_socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(port, host)

    while True:
        message = input("Votre message: ")
        s.send(message.encode('utf-8'))

        data = s.recv(1024).decode('ASCII')
        print(f"Reçu du serveur: {data}")

    s.close()

if __name__ == "__main__":
    main()
