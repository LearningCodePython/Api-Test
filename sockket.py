# @ By Cristo Emiliano Hernandez Daria
#
import requests
import socket
import sys
import json

# Primero Generamos un Token
url = "http://192.168.0.45:8088/api/v1.1.0/login"
payload="{ \"username\": \"api\",\"password\": \"6b0e4416872b14b0214416825910c718\",\"port\": \"8260\"}"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)
jsonResponse = response.json()

print("Print each key-value pair from JSON response")
for key, value in jsonResponse.items():
    print(key, ":", value)

token = (jsonResponse["token"])

# Crear un TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el zócalo al puerto
server_address = ('10.19.19.16', 8260)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Escuche las conexiones entrantes
sock.listen(2)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
#        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(128)
            print(data)
            if data:
                print('sending data back to the client')
#                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
        



