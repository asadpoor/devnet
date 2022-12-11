from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_save_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def netmiko_send_config_from_file_exmaple(task):
    task.run(task=netmiko_send_config, config_file="config_file.txt")

def netmiko_save_config_exmaple(task):
    task.run(task=netmiko_save_config)
    
results=nr.run(task=netmiko_send_config_from_file_exmaple)
print_result(results)

results=nr.run(task=netmiko_save_config_exmaple)
print_result(results)
