import socket

# サーバーに接続
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    message = input("クライアント:looser ")
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    if not response:
        break
    print(f"サーバー: {response}")

client_socket.close()
