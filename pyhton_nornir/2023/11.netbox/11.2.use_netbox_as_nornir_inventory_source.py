import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

# before running the script export username and password in environment variables in automation machine
#majid@devnet:$ export USERNAME='rayka'
#majid@devnet:$ export PASSWORD='rayka-co.com'

# read username and password from environment variables and storethem into nornir username and password variables
nr.inventory.defaults.username = os.environ['USERNAME']
nr.inventory.defaults.password = os.environ['PASSWORD']

# you can any other methods to not store clear text password in automation script
# like  public key authentication, sysargv, GPG or getpass, ...

def use_netbox_as_nornir_inventory_source(task):
    task.run(task=send_command, command="show ip interface brief")

results = nr.run(task=use_netbox_as_nornir_inventory_source)
print_result(results)
