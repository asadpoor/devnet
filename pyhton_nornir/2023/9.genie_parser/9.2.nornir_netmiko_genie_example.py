from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def nornir_netmiko_genie_example(task):
    result=task.run(task=netmiko_send_command, command_string="show interfaces", use_genie=True)
    interfaces = result.result
#    rprint(interfaces)
#    rprint(type(interfaces))

#    for key, value in interfaces.items():
#        rprint("key=", key)
#        rprint("value=",value)

    for key in interfaces.keys():
#        rprint(interfaces[key])
#        rprint(type(interfaces[key]))
         rprint("interface ", key, " operational status is", interfaces[key]["oper_status"])

results=nr.run(task=nornir_netmiko_genie_example)
