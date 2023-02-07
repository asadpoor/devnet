from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from rich import print as rprint
from genie.utils import Dq

nr = InitNornir(config_file="config.yaml")

def genie_Dq_example(task):
    result=task.run(task=netmiko_send_command, command_string="show interfaces", use_genie=True)
    interfaces = result.result
    rprint(interfaces)
#    rprint(interfaces["GigabitEthernet1"]["counters"]["out_pkts"])

#    rprint("return the list of values of out_pkts key :", \
#     Dq(interfaces).get_values("out_pkts"))

#    rprint("return the value of out_pkts key of index 0 in the list:", \
#      Dq(interfaces).get_values("out_pkts")[0])

#    rprint("return the value of out_pkts key of GigabitEthernet1 interface:", 
#      Dq(interfaces).contains("GigabitEthernet1").get_values("out_pkts"))

#
#    rprint("return the value of out_pkts if it is greater than zero: ", \
#      interfaces.q.value_operator("out_pkts", '>', 0).get_values("out_pkts"))

#    rprint("keep the dictionary path which contain the key_value pair of enabled:True ", \
#      interfaces.q.contains_key_value('enabled', True))

#    rprint("keep the dictionary path which contain the key_value pair of enabled:True and rebuild the dictionary", \
#      interfaces.q.contains_key_value('enabled', True).reconstruct())

#    rprint("keep the path which does not contains False string and te´hen return the value of out_pkts key : ", \
#      Dq(interfaces).not_contains(False).get_values("out_pkts"))

#    rprint("keep the path with key of line_protocol which value is matched with regex u.* : ", \
#      interfaces.q.contains_key_value('line_protocol', 'u.*', value_regex=True).reconstruct())

#    rprint("keep the path with key matching with regex line.* and the value of up : ", \
#      interfaces.q.contains_key_value('line.*', 'up', key_regex=True).reconstruct())

results=nr.run(task=genie_Dq_example)

# Dq: Dictionary query allow to question Python dictionary in a very intuitive syntax.
# https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html

# contains: Filters down the dictionary and only keep the paths which contains the provided string
# not_contains: Only keep paths which does not contains the provided string. remove unwanted path and have a dictionary wizh only desired keys/paths.
# reconstruct: rebuilds a dictionary from Dq output 
# get_values: return a list of the values of the provided key
# contains_key_value: similar to contains except instead of only the expected value the parent key is also provided
# value_operator: filter down based on the value of a certain key with {==, !=, >=, <=, >, <}
# count: count how many element match the requirement.
# key_regex: if looking for keys with a regex pattern you need to set key_regex to True. 
# value_regex: for applying regex pattern on values, you need to set value_regex variable to True.
