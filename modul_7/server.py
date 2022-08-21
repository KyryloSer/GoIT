import socket


def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    data = conn.recv(1024).decode()
    print("from connected user: " + str(data))
    conn.send("OK".encode())
    conn.close()


if __name__ == '__main__':
    server_program()
