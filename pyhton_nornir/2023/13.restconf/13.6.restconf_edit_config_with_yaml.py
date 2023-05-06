import requests
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.data import load_yaml
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")
requests.packages.urllib3.disable_warnings()
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def load_data(task):
    data = task.run(task=load_yaml, file=f"host_vars/{task.host}.yaml")
    task.host["hdata"] = data.result

def restconf_edit_config_with_yaml(task):
    USERNAME = f"{task.host.username}"
    PASSWORD = f"{task.host.password}"

    module1 = "Cisco-IOS-XE-native:native/router/router-ospf"
    url1 = f"https://{task.host.hostname}:443/restconf/data/{module1}"
    response = requests.put(url=url1, headers=headers, auth=(USERNAME, PASSWORD), verify=False, json=task.host["hdata"]["ospf_config"])
    print(response)

    module2 = "Cisco-IOS-XE-native:native/ntp"
    url2 = f"https://{task.host.hostname}:443/restconf/data/{module2}"
    response = requests.put(url=url2, headers=headers, auth=(USERNAME, PASSWORD), verify=False, json=task.host["hdata"]["ntp_config"])
    print(response)

    module3 = "openconfig-acl:acl"
    url3 = f"https://{task.host.hostname}:443/restconf/data/{module3}"
    response = requests.put(url=url3, headers=headers, auth=(USERNAME, PASSWORD), verify=False, json=task.host["hdata"]["acl_config"])
    print(response)


load_results = nr.run(task=load_data)
configure_results = nr.run(task=restconf_edit_config_with_yaml)
