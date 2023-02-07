from nornir import InitNornir
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = "rayka"
nr.inventory.defaults.password = "rayka-co.ir"

def getnetboxdata(task):
    rprint(f"device name: {task.host}")
    rprint(f"device IP address: {task.host.hostname}")
    rprint(f"device platform: {task.host.platform}")
    rprint(f"device inventory data: {task.host.data}")

nr.run(task=getnetboxdata)
