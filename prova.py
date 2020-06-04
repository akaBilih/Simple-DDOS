import urllib2 as url 
from os import system as command
import subprocess

command("cls")
data = url.urlopen("http://quisomjo.ddns.net/ddos.txt") 
print(data.read())






subprocess.Popen("ssh {user}@{host} {cmd} ".format(user="admin", host="quisomjo.ddns.net", cmd='mkdir /volume1/web/hola'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()