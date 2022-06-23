from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def textfsm_nornir_netmiko_example(task):
    netmiko_result=task.run(task=netmiko_send_command, command_string="show interfaces", use_textfsm=True)
    interfaces = netmiko_result.result
#    rprint(interfaces)
#    rprint(type(interfaces))

    for interface in interfaces:
#        rprint(interface)
#        rprint(type(interface))
        rprint("interface", interface["interface"], "with IP address", interface["ip_address"], "is physically ", interface["link_status"], "and line protocol is", interface["protocol_status"])

results=nr.run(task=textfsm_nornir_netmiko_example)