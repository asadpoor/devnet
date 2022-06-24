from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def textfsm_nornir_scrapli_example(task):
    scrapli_result=task.run(task=send_command, command="show ip interface brief")
    interfaces = scrapli_result.scrapli_response.genie_parse_output()
    rprint(interfaces)
#    rprint(type(interfaces))
#    rprint(interfaces["interface"])
#    rprint(type(interfaces["interface"]))


#    for key, value in interfaces["interface"].items():
#        rprint("key=",key)
#        rprint("value=",value)

#    for key in interfaces["interface"].keys():
#        rprint("key=", key)
#        rprint(interfaces["interface"][key])
#        rprint(type(interfaces["interface"][key]))
#        rprint("IP Address of", key, " is ", interfaces["interface"][key]["ip_address"])



results=nr.run(task=textfsm_nornir_scrapli_example)