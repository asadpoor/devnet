import getpass
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

default_password=getpass.getpass(prompt="Enter Default Password: ")
cisco_group_password=getpass.getpass(prompt="Enter Cisco Group Password: ")
juniper_group_password=getpass.getpass(prompt="Enter Juniper Group Password: ")
R1_password=getpass.getpass(prompt="Enter Router R1 Password: ")

nr.inventory.defaults.password=default_password
nr.inventory.groups["cisco"].password=cisco_group_password
nr.inventory.groups["juniper"].password=cisco_group_password
nr.inventory.hosts["R1"].password=R1_password

def netmiko_send_commands_example(task):
    task.run(task=netmiko_send_command, command_string="show ip int brief | exc unass")

results=nr.run(task=netmiko_send_commands_example)
print_result(results)

