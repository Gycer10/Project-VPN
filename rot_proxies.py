import socket
import os
import tqdm


def change_ip(a):
    i_ip = a
    n_ip = a
    # n_ip = "88.3.66.183"

    return n_ip


def sender():
    host = '192.168.1.104'
    port = 59074
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    file = open("image.png", "rb")
    file_size = os.path.getsize("image.png")

    client.send("received_image.png".encode())
    client.send(str(file_size).encode())

    data = file.read()
    client.sendall(data)
    client.send(b"<END>")

    file.close()
    client.close()


def receiver():
    host = '192.168.1.104'
    port = 59074
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    client, addr = server.accept()

    file_name = client.recv(1024).decode()
    print(file_name)
    # file_size = client.recv(1024).decode()
    # print(file_size)

    file = open(file_name, "wb")

    file_bytes = b""

    # done = False
    #
    # progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))
    #
    # while not done:
    #     data = client.recv(1024)
    #     if file_bytes[-5:] == b"<END>":
    #         done = True
    #     else:
    #         file_bytes += data
    #     progress.update(1024)

    file.write(file_bytes)

    file.close()
    client.close()
    server.close()


# i = int(input("select if you're receiver [1] or sender [2]"))
# if i == 1:
#     receiver()
# elif i == 2:
#     sender()
# else:
#     print("Not such option available")
