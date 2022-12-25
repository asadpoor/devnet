from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def nornir_napalm_structured_output_example(task):
#    interfaces=task.run(task=napalm_get, getters=["get_interfaces"])
    config=task.run(task=napalm_get, getters=["get_config"])

### the result of the first example
#    print(type(interfaces.result))   #1
#    rprint(interfaces.result)        #2
#    rprint(interfaces.result["get_interfaces"])    #3
#    rprint(interfaces.result["get_interfaces"]["GigabitEthernet1"])     #4
#    rprint(interfaces.result["get_interfaces"]["GigabitEthernet1"]["is_enabled"])   #5


### the result of the second example
#    rprint(config.result)    #1
#    rprint(config.result["get_config"]) #2
    rprint(config.result["get_config"]["running"])    #3

nr.run(task=nornir_napalm_structured_output_example)
