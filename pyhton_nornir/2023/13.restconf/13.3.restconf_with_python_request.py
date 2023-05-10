import requests
import xmltodict
from rich import print as rprint

requests.packages.urllib3.disable_warnings()

HOST = "192.168.2.91"
PORT = "443"
USER = "rayka"
PASSWORD = "rayka-co.com"

header1 = {"Accept": "application/yang-data+xml"}
header2 = {"Accept": "application/yang-data+json"}

url0 = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces"
url1 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native"
url2 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/ip/domain"

url3 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router"
url4 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf"
url5 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf/ospf"
url6 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf/ospf/process-id"
url7 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf/ospf/process-id=1"

url75 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"
url8 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

url9 = f"https://{HOST}:{PORT}/restconf/data/openconfig-interfaces:interfaces?content=config"
url10 = f"https://{HOST}:{PORT}/restconf/data/openconfig-interfaces:interfaces?content=nonconfig"


url11 = f"https://{HOST}:{PORT}/restconf/data/openconfig-interfaces:interfaces/interface=GigabitEthernet1?content=nonconfig"

url12 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/bgp"

url13 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/ntp"

url14 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/ip/access-list/Cisco-IOS-XE-acl:extended"

url15 = f"https://{HOST}:{PORT}/restconf/data/openconfig-acl:acl?content=config"

response = requests.get(url=url5, headers=header2, auth=(USER, PASSWORD), verify=False)

# print result inf the format of text or original format
#rprint(response.text)
#rprint(response.content)

# if the result is in the content of xml
#xml_response = response.content
#dic_response = xmltodict.parse(xml_response)
#rprint(dic_response)

# if the result is in the content of json
#rprint(response.json())
#rprint(type(response.json()))

dic_response=response.json()
#print(type(dic_response))
# with url11
#dic_response=dic_response["openconfig-interfaces:interface"]["state"]["counters"]["in-octets"]
#for  key,value in dic_response.items():
#  print("key=",key)
#  print("value=",value)

rprint(dic_response)
