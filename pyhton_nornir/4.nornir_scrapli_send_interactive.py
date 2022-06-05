from ast import Interactive
from nornir import InitNornir
from nornir_scrapli.tasks import send_interactive
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def interactive_commands_exmple(task):
    interact_lists=[
#        ("copy running-config flash:backup3", "Destination filename [backup3]?", False),
#        ("\n", f"{task.host}#", False),
        ("ping", "Protocol [ip]:", False),
        ("\n", "Target IP address:", False),
        ("8.8.8.8", "Repeat count [5]:", False),
        ("\n", "Datagram size [100]:", False),
        ("\n", "Timeout in seconds [2]:"  , False),
        ("\n", "Extended commands [n]:"  , False),
        ("\n", "Sweep range of sizes [n]:"  , False),
        ("\n", f"{task.host}#", False),
    ]
#    task.host.connections['scrapli'].connection.channel.timeout_ops = timeout
    task.run(task=send_interactive, interact_events=interact_lists, timeout_ops=200 )

results=nr.run(task=interactive_commands_exmple)
print_result(results)
