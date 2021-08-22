#!/usr/bin/python3
import requests
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



target_ip = input("Enter The IP You Want To Track: ")
api = "http://ip-api.com/json/"

res = requests.get(api + target_ip)

data = res.json()

print("IP query Is: ", data["query"])
print("IP status Is: ", data["status"])
print("IP countryCode Is: ", data["countryCode"])
print("IP region Is: ", data["region"])
print("IP regionName Is: ", data["regionName"])
print("IP city Is: ", data["city"])
print("IP zip Is: ", data["zip"])
print("IP lat Is: ", data["lat"])
print("IP lon Is: ", data["lon"])
print("IP timezone Is: ", data["timezone"])
print("IP isp Is: ", data["isp"])
print("IP org Is: ", data["org"])
print("IP as Is: ", data["as"])


target_ip = input(".")

