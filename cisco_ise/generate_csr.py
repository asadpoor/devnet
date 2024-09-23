import requests
import json

url = "https://192.168.2.123:443/api/v1/certs/certificate-signing-request"
username = "admin"
password = "Asadp00r.ir"

payload = json.dumps({
  "digestType": "SHA-256",
  "keyLength": "2048",
  "keyType": "RSA",
  "usedFor": "MULTI-USE",
  "allowWildCardCert": False,
  "hostnames": [
    "ise34"
  ],
  "portalGroupTag": "default",
  "sanDNS": [],
  "sanDir": [],
  "sanIP":  [],
  "sanURI": [],
  "subjectCity": "Tehran",
  "subjectCommonName": "ise34.rayka-co.local",
  "subjectCountry": "IR",
  "subjectOrg": "RAYKA",
  "subjectOrgUnit": "security",
  "subjectState": "Tehran"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

# Disable SSL verification and add basic authentication
response = requests.post(url, headers=headers, data=payload, auth=(username, password), verify=False)

print(response.text)
