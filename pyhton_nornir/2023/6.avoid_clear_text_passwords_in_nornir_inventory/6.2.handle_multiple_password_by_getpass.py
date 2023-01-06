import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

default_password=getpass.getpass(prompt="Enter Default Password: ")
cisco_group_password=getpass.getpass(prompt="Enter Cisco Group Password: ")
R1_password=getpass.getpass(prompt="Enter Router R1 Password: ")

nr.inventory.defaults.password=default_password
nr.inventory.groups["cisco"].password=cisco_group_password
nr.inventory.hosts["R1"].password=R1_password

def get_multiple_password_by_getpass_example(task):
    task.run(task=send_command, command="show ip interface brief | exc unassigned")

results=nr.run(task=get_multiple_password_by_getpass_example)
print_result(results)
