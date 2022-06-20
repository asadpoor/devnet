from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")

def netmiko_send_commands_example(task):
    task.run(task=netmiko_send_command, command_string="show ip int brief | exc unass")

nr_filter = nr.filter( (F(type="router") | F(city="babolsar")) & ~F(core="True") & F(as__le="65001") & F(city__contains="bol") )
results=nr_filter.run(task=netmiko_send_commands_example)
print_result(results)
