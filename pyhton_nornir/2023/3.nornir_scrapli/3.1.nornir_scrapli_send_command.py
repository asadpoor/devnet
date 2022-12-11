from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_scrapli_send_command_example(task):
    task.run(task=send_command, command="show ip interface brief | exc unassigned")

results = nr.run(task=nornir_scrapli_send_command_example)
print_result(results)
