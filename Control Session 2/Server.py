import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345
Pk_Num = 0  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"Server listening on {HOST}:{PORT}")

while True:
    packet_num_bytes, client_address = server_socket.recvfrom(4)
    
    if not packet_num_bytes:
        continue
    
    packet_num = int.from_bytes(packet_num_bytes, 'big')
    
    if packet_num == Pk_Num:
        print(f"Received packet number: {packet_num}")
        Pk_Num += 1
        response = f"Packet {packet_num} received"
        server_socket.sendto(response.encode('utf-8'), client_address)
    
    if packet_num == 10:
        break

server_socket.close()
