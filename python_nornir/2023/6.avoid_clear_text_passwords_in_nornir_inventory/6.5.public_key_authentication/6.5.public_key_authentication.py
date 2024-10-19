from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def public_key_authentication_example(task):
    task.run(task=send_command, command="show ip interface brief | exc unassigned")

results=nr.run(task=public_key_authentication_example)
print_result(results)
