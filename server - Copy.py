import socket
import time
import atexit
    


host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port


def goodbye():
    try:
        s.close()
    except socket.error:
        pass

atexit.register(goodbye)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print(host , port)
totalConections = 0
while True:
    s.listen(1)
    conn, addr = s.accept()
    


    try:
        data = conn.recv(1024)

        if not data: break

        if data == 'bye':
            totalConections -= 1
            print(addr[0] + " disconnected from attack. Total connected: {num}".format(num=totalConections))
            continue
        
        if data == 'hello':
            totalConections += 1
            print(addr[0] + " started attaking. Total connected: {num}".format(num=totalConections))

        

    except socket.error:
        print("Error Occured.")

    conn.close()
    time.sleep(.5)

