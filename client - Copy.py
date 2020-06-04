import socket
import time
import atexit

def goodbye():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b'bye')
    s.close()

atexit.register(goodbye)

host = "quisomjo.ddns.net"
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'hello')
s.close()
time.sleep(200)