from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=send_commands, commands=["show ip interface brief","show interface gigabitEthernet 1"])
print_result(results)
