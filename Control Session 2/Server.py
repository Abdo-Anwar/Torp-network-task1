import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345
Pk_Num= 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")

while True:
     
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    while True:   
        packet_num_bytes = client_socket.recv(4)
        if not packet_num_bytes:
            break

        packet_num = int.from_bytes(packet_num_bytes, 'big')
        print(f"Received packet number: {packet_num}")
        
        response = f"Packet {packet_num} received"
        client_socket.send(response.encode('utf-8'))

        if packet_num == 10:
            break
    
    client_socket.close()


server_socket.close()
