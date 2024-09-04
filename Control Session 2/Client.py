import socket as sk
global Pk_Num
Pk_Num= 0


server_ip='192.168.1.26'
server_port=12345
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
while True:
    msg=input("Enter message: ")
    
   
    sock.sendto(Pk_Num.to_bytes(4, 'big'), (server_ip, server_port))    
    data, _ = sock.recvfrom(1024)
    print(data.decode('utf-8'))
    Pk_Num += 1

    if msg=='exit':
        print("exiting")
        break
sock.close()