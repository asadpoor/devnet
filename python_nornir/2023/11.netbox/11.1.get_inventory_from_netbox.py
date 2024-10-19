from nornir import InitNornir
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

# it is not recommended to store username and password in automation script. 
# in the next script we use environment variables to read the username and password.
nr.inventory.defaults.username = "rayka"
nr.inventory.defaults.password = "rayka-co.ir"

def get_inventory_from_netbox(task):
    rprint(f"device name: {task.host}")
    rprint(f"device IP address: {task.host.hostname}")
    rprint(f"device platform: {task.host.platform}")
    rprint(f"device inventory data: {task.host.data}")

nr.run(task=get_inventory_from_netbox)
