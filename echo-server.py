# @ By Cristo Emiliano Hernandez Daria
#
import socket

# Crear un TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el zócalo al puerto
server_address = ('', 8260)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Escuche las conexiones entrantes
sock.listen()

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        #Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(128)
            print(data)
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
        



