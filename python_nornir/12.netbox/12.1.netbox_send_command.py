from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = "rayka"
nr.inventory.defaults.password = "rayka-co.ir"


def netbox_send_command(task):
    task.run(task=send_command, command="show ip interface brief")


results = nr.run(task=netbox_send_command)
print_result(results)
