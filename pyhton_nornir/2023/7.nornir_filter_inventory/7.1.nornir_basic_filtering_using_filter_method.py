from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_basic_filtering_using_filter_method_example(task):
    task.run(task=netmiko_send_command, command_string="show ip int brief | exc unass")

nr_filter = nr.filter(type="router", city="babolsar")
results=nr_filter.run(task=nornir_basic_filtering_using_filter_method_example)
print_result(results)
