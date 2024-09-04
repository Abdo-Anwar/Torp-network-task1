import socket as sk
import re
global Pk_Num
Pk_Num= 0


server_ip='192.168.1.26'
server_port=12345
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

while True:
    msg = input("Enter message: ")
    
    sock.sendto(Pk_Num.to_bytes(4, 'big'), (server_ip, server_port))    
    data, _ = sock.recvfrom(1024)
    response = data.decode('utf-8')

    if response.startswith("Expected packet number:"):
        match = re.search(r"Expected packet number: (\d+)", response)
        if match:
            Pk_Num = int(match.group(1))
            print(f"Correction received: {response}")
        else:
            print("Received correction message but couldn't parse the packet number.")
    else:
        print(f"Server response: {response}")
        Pk_Num += 1

    if msg == 'exit':
        print("exiting")
        break

sock.close()