# echo-client.py

import socket

HOST = "192.168.0.114"  # The server's hostname or IP address
PORT = 8260  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, soy el cliente de una conexion TCP")
    data = s.recv(1024)

print(f"Received {data!r}")