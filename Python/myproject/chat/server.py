import socket

# サーバーの設定
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # IPアドレスとポート番号
server_socket.listen(5)

print("サーバーが起動しました。クライアントを待っています...")

# クライアントの接続を待つ
client_socket, client_address = server_socket.accept()
print(f"クライアント {client_address} が接続しました。")

while True:
    message = client_socket.recv(1024).decode('utf-8')
    if not message:
        break
    print(f"クライアント: {message}")
    response = input("サーバー: ")
    client_socket.send(response.encode('utf-8'))

client_socket.close()
server_socket.close()
