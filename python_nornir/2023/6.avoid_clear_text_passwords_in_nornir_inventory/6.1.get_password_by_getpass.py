import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

mypassword=getpass.getpass(prompt="Enter Password: ")
nr.inventory.defaults.password=mypassword
#nr.inventory.groups["cisco"].password=mypassword
#nr.inventory.hosts["R1"].password=mypassword

def get_password_by_getpass_example(task):
    task.run(task=send_command, command="show ip interface brief | exc unassigned")
results=nr.run(task=get_password_by_getpass_example)
print_result(results)
