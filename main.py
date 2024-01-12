import customtkinter
import gui
import database
import socket
# import threading
# import rsa
import rot_proxies
# import chat
# import vpn


def mes(a, b):
    # res = database.insert('hello@no.com', 123, 'Test')
    # print(f"{res}")
    print(f"We have modified your previous IP to a new one: {a} -> {b}")


def sign_up():
    root = customtkinter.CTkToplevel()
    root.title("Create your account")
    root.geometry("500x350")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Create your account", font=("Roboto", 20))
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="E-mail")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    def nick():
        frame1 = customtkinter.CTkFrame(master=root)
        frame1.pack(pady=20, padx=60, fill="both", expand=True)

        label1 = customtkinter.CTkLabel(master=frame, text="Enter your name/nick-name", font=("Roboto", 15))
        label1.pack(pady=12, padx=10)

        entry11 = customtkinter.CTkEntry(master=frame, placeholder_text="name")
        entry11.pack(pady=12, padx=10)

        button1 = customtkinter.CTkButton(master=frame, text="Continue", command=mes(""))
        button1.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Continue", command=nick)
    button.pack(pady=12, padx=10)


def cht():
    root = customtkinter.CTk()
    root.title(f"Internal Chat")
    root.geometry("500x350")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # text = chat.sending_messages()

    # label = customtkinter.CTkLabel(master=frame, text=text, font=("Roboto", 12))
    # label.pack(pady=12, padx=10)


def main():

    # conn = server.main()

    root = customtkinter.CTk()
    root.title(f"Start using {ip_add}")
    root.geometry("500x350")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    def login():
        root1 = customtkinter.CTkToplevel()
        root1.title("Worker's Interface")
        root1.geometry("800x550")

        # this is the part where we should call the rot_proxies to create the VPN secure connection
        new_ip = rot_proxies.change_ip(ip_add)
        print(f"New IP assigned: {new_ip}")

        # retrieve the user connected from the database
        e = entry1.get()
        user = database.usr(e)
        print(f"User doing connection is {user}")

        # here goes the communication with the server with encryption
        print("Trying to make connection with the server")
        gui.main(new_ip, user)

        frame1 = customtkinter.CTkFrame(master=root1)
        frame1.pack(pady=20, padx=60, fill="both", expand=True)

        label1 = customtkinter.CTkLabel(master=frame1, text="You have logged into the Company's system", font=("Roboto",
                                                                                                               12))
        label1.pack(pady=12, padx=10)

        button2 = customtkinter.CTkButton(master=frame1, text="All good", command=mes(ip_add, new_ip))
        button2.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=12, padx=10)

    button1 = customtkinter.CTkButton(master=frame, text="Sign up", command=sign_up)
    button1.pack(pady=12, padx=10)

    root.mainloop()


if __name__ == "__main__":
    global user
    hostname = socket.gethostname()
    ip_add = socket.gethostbyname(hostname)
    customtkinter.set_appearance_mode("black")
    customtkinter.set_default_color_theme("dark-blue")
    main()
