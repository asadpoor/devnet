from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_scrapli_send_commands_example(task):
    task.run(task=send_commands, commands=["show ip interface brie | exc unassigned","show interface gigabitEthernet 1 | inc address"])

results = nr.run(task=nornir_scrapli_send_commands_example)
print_result(results)
