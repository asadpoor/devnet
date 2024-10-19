from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
commands=["router ospf 1", "router-id 1.1.1.1", "network 10.0.0.0 0.255.255.255 area 0"]

def netmiko_send_config_exmaple(task):
    task.run(task=netmiko_send_config, config_commands=commands)

results=nr.run(task=netmiko_send_config_exmaple)
print_result(results)
