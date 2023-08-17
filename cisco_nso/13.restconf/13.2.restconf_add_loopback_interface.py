import requests
import json

HOST = "192.168.2.101"
PORT = "8080"
USER = "admin"
PASSWORD = "admin"

url = f"http://{HOST}:{PORT}/restconf/data/tailf-ncs:devices/device=R1/config/tailf-ned-cisco-ios:interface/"

payload = json.dumps({
  "Loopback": [
    {
      "name": "300",
      "ip": {
        "address": {
          "primary": {
            "address": "4.5.16.17",
            "mask": "255.255.255.255"
          }
        }
      }
    }
  ]
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("POST", url, headers=headers, auth=(USER, PASSWORD), data=payload)

print(response.text)
