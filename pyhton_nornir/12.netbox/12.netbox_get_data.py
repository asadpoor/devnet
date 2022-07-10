from nornir import InitNornir
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = "rayka"
nr.inventory.defaults.password = "rayka-co.ir"

def getnetboxdata(task):
    rprint(f"My name is {task.host}")
    rprint(f"My IP address is {task.host.hostname}")
    rprint(f"My platform is {task.host.platform}")
    rprint(f"My data is {task.host.data}")

nr.run(task=getnetboxdata)
