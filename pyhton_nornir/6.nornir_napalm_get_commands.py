from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def napalm_get_example(task):
    task.run(task=napalm_get, getters=["get_facts", "get_interfaces", "get_config"])

results=nr.run(task=napalm_get_example)
print_result(results)
