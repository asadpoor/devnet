import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

nr.inventory.hosts["R1"].username=os.environ["username"]
nr.inventory.hosts["R1"].password=os.environ["password"]

def netmiko_send_commands_example(task):
    task.run(task=send_command, command="show ip interface brief | exc unassigned")

results=nr.run(task=netmiko_send_commands_example)
print_result(results)

