import requests
import json

HOST = "192.168.2.101"
PORT = "8080"
USER = "admin"
PASSWORD = "admin"

url = f"http://{HOST}:{PORT}/restconf/data/tailf-ncs:devices/device=R1/config/tailf-ned-cisco-ios:interface/Loopback=300"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
}

response = requests.request("DELETE", url, headers=headers, auth=(USER, PASSWORD), data=payload)

print(response.text)
