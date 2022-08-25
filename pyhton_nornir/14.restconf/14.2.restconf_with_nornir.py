import requests
from nornir import InitNornir
from rich import print as rprint

requests.packages.urllib3.disable_warnings()

nr = InitNornir(config_file="config.yaml")

header1 = {"Accept": "application/yang-data+json"}


def restconf_nornir_example(task):
    url = f"https://{task.host.hostname}:443/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf"
    response = requests.get(url=url, headers=header1, auth=(f"{task.host.username}", f"{task.host.password}"), verify=False)
    task.host["data"] = response.json()
#    result = task.host["data"]
#    result = task.host["data"]["Cisco-IOS-XE-ospf:router-ospf"]
#    result = task.host["data"]["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]
    result = task.host["data"]["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"]
#    print(type(result))
#    rprint(result)

# dictionary parsing
#    for key, value in result.items():
#      print("key=", key)
#      print("value=", value)


# list parsing
    for ospf_process_id in result:
      print(ospf_process_id["router-id"])


nr.run(task=restconf_nornir_example)

