from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_napalm_get_example(task):
    task.run(task=napalm_get, getters=["get_facts", "get_interfaces", "get_interfaces_ip", "get_config"])

results=nr.run(task=nornir_napalm_get_example)
print_result(results)
