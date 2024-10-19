import sys
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

nr.inventory.hosts["R1"].username=sys.argv[1]
nr.inventory.hosts["R1"].password=sys.argv[2]

def get_password_by_sysargv_example(task):
    task.run(task=send_command, command="show ip interface brief | exc unassigned")

results=nr.run(task=get_password_by_sysargv_example)
print_result(results)

