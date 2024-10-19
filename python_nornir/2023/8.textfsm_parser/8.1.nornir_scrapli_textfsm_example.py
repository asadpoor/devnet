from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def nornir_scrapli_textfsm_example(task):
    result=task.run(task=send_command, command="show ip interface brief")
    interfaces = result.scrapli_response.textfsm_parse_output()
#    rprint(interfaces)
#    rprint(type(interfaces))

    for interface in interfaces:
#        rprint(interface)
#        rprint(type(interface))
        rprint("interface", interface["intf"], "with IP address", interface["ipaddr"] , "is physically ", interface["status"], "and line protocol is", interface["proto"])


results=nr.run(task=nornir_scrapli_textfsm_example)
