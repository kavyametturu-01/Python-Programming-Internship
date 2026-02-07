import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 34567))
server.listen()

clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            for c in clients:
                if c != client:
                    c.send(message)
        except:
            clients.remove(client)
            client.close()
            break

print("Server is running...")

while True:
    client, address = server.accept()
    print("Client connected:", address)
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
