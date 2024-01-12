import socket
import threading
import rsa

# this one is client 2
# the ip needs to be the same as the server, otherwise we will get Error [61]


def main(ip, user):
    print("Starting the process of communication...")
    public_key, private_key = rsa.newkeys(1024)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # c2_ip = "127.0.0.1"
    client.connect((ip, 52409))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))
    ip_address = client.getsockname()
    print(f"You're connected using the following IP-address and Port: {ip_address}")

    def sending_messages(c):
        while True:
            message = input("")
            # c.send(message.encode())
            # this line is going to be for testing encryption on WireShark
            c.send(rsa.encrypt(message.encode(), public_partner))
            print(f"{user}: " + message)

    def receiving_message(c):
        while True:
            print("Admin: " + rsa.decrypt(c.recv(1024), private_key).decode())
            # print("Admin: " + c.recv(1024).decode())
            # this line is going to be for testing encryption on WireShark

    threading.Thread(target=sending_messages, args=(client,)).start()
    threading.Thread(target=receiving_message, args=(client,)).start()

    return client
