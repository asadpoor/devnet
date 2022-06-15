from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def napalm_get_example(task):
#    interfaces=task.run(task=napalm_get, getters=["get_interfaces"])
    config=task.run(task=napalm_get, getters=["get_config"])

#    print(interfaces.result)
#    rprint(interfaces.result)
#    rprint(interfaces.result["get_interfaces"])
#    rprint(interfaces.result["get_interfaces"]["GigabitEthernet1"])
#    rprint(interfaces.result["get_interfaces"]["GigabitEthernet1"]["is_enabled"])

#    rprint(config.result)
#    rprint(config.result["get_config"])
    rprint(config.result["get_config"]["running"])

results=nr.run(task=napalm_get_example)
