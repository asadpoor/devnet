import requests
import json
from nornir import InitNornir
from rich import print as rprint
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml


requests.packages.urllib3.disable_warnings()

nr = InitNornir(config_file="config.yaml")

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def load_data(task):
  hosts_data = task.run(task=load_yaml, file=f"./host_vars/{task.host}_.yaml")
  task.host["hdata"] = hosts_data.result


def restconf_edit_config_with_template(task):
    template_to_load = task.run(task=template_file, template="ospf_.j2", path="templates")
    payload = template_to_load.result
    module = "Cisco-IOS-XE-native:native/router/router-ospf/ospf"
    url = f"https://{task.host.hostname}:443/restconf/data/{module}"

    response = requests.put(url, headers=headers, data=payload, auth=(f"{task.host.username}", f"{task.host.password}"), verify=False)
    print(response)

nr.run(task=load_data)
results = nr.run(task=restconf_edit_config_with_template)
print_result(results)
