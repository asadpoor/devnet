from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result
import re


nr = InitNornir(config_file="config.yaml")

ntp = """
ntp server 1.2.3.4
ntp server 5.6.7.8
"""

ospf = """
router ospf 1
 router-id 1.1.1.1
 network 10.11.0.0 0.0.255.255 area 1
 network 10.12.0.0 0.0.255.255 area 2
"""

def nornir_napalm_replace_config_example(task):
    config=task.run(task=napalm_get, getters=["get_config"])
    running_config=config.result["get_config"]["running"]

###### example1
#    to_be_replaced = re.compile("^ntp server([^!]+)", flags=re.MULTILINE)
#    running_config_new = re.sub(to_be_replaced, ntp, running_config)

###### example2
    to_be_replaced = re.compile("^router ospf([^!]+)", flags=re.MULTILINE)
    running_config_new = re.sub(to_be_replaced, ospf, running_config)

    task.run(task=napalm_configure, configuration=running_config_new, replace=True)


results=nr.run(task=nornir_napalm_replace_config_example)
print_result(results)
