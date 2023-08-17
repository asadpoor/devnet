import requests

url = "http://192.168.2.101:8080/restconf/data/tailf-ncs:devices/device=R1/config/tailf-ned-cisco-ios:interface/"

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
