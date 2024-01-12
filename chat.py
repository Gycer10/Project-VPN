import socket
import threading
import rsa
import main

# this one is client 1

public_key, private_key = rsa.newkeys(1024)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# c1_ip = "192.168.1.104"
# c1_ip = "212.81.196.37"
# c1_ip = "88.3.66.183"
c1_ip = "127.0.0.1"
# apparently the IP will change depending on the Wi-Fi I'm connected to
server.bind((c1_ip, 52409))
server.listen()
print(f"Listening and sending from {server}")
client, _ = server.accept()
client.send(public_key.save_pkcs1("PEM"))
ip_address = client.getsockname()
print(f"The IP of the client 1 is: {ip_address}")
public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))


def sending_messages(c):
    while True:
        message = input("")
        # c.send(message.encode())
        # this line is going to be for testing encryption on WireShark
        c.send(rsa.encrypt(message.encode(), public_partner))
        print("You: " + message)


def receiving_message(c):
    while True:
        print("Worker: " + rsa.decrypt(c.recv(1024), private_key).decode())
        # print("Worker: " + c.recv(1024).decode())
        # this line is going to be for testing encryption on WireShark


threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_message, args=(client,)).start()
