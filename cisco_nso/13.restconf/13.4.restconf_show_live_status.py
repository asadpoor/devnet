import requests
import json

HOST = "192.168.2.101"
PORT = "8080"
USER = "admin"
PASSWORD = "admin"

url = f"http://{HOST}:{PORT}/restconf/data/tailf-ncs:devices/device=R1/live-status"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
}

response = requests.request("GET", url, headers=headers, auth=(USER, PASSWORD), data=payload)

print(response.text)
