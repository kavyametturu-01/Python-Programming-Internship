import socket
import threading
import tkinter as tk

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 34567))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            chat_box.config(state='normal')
            chat_box.insert(tk.END, message + "\n")
            chat_box.config(state='disabled')
        except:
            break

def send_message():
    message = message_entry.get()
    if message.strip() == "":
        return

    # show your own message
    chat_box.config(state='normal')
    chat_box.insert(tk.END, "You: " + message + "\n")
    chat_box.config(state='disabled')

    # send message to server
    client.send(("Friend: " + message).encode())
    message_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chat Application")

chat_box = tk.Text(root, height=15, width=50, state='disabled')
chat_box.pack(padx=10, pady=10)

message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

root.mainloop()
