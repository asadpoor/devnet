from nornir import InitNornir
from nornir_scrapli.tasks import send_interactive
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def interactive_commands_exmple(task):
    interact_lists=[
        # Example1
#        ("copy running-config flash:backup", "Destination filename [backup]?", False),
#        ("\n", f"{task.host}#", False),
        # Example2
        ("ping", "Protocol [ip]:", False),
        ("ip", "Target IP address:", False),
        ("8.8.8.8", "Repeat count [5]:", False),
        ("5", "Datagram size [100]:", False),
        ("100", "Timeout in seconds [2]:"  , False),
        ("2", "Extended commands [n]:"  , False),
        ("n", "Sweep range of sizes [n]:"  , False),
        ("n", f"{task.host}#", False),
    ]
    task.run(task=send_interactive, interact_events=interact_lists)

results=nr.run(task=interactive_commands_exmple)
print_result(results)
