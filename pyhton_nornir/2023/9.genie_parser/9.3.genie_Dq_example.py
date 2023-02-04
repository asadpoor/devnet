from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from rich import print as rprint
from genie.utils import Dq

nr = InitNornir(config_file="config.yaml")

def genie_Dq_example(task):
    result=task.run(task=netmiko_send_command, command_string="show interfaces", use_genie=True)
    interfaces = result.result
#    rprint(interfaces)
#    rprint(interfaces["GigabitEthernet1"]["counters"]["out_pkts"])

    rprint("keep the path which contains GigabitEthernet1 and does not contain False : ", \
      Dq(interfaces).contains("GigabitEthernet1").not_contains(False))

    rprint("keep the path which contains GigabitEthernet1 and and does not contain False and rebuild the dictionary : ", \
      Dq(interfaces).contains("GigabitEthernet1").not_contains(False).reconstruct())

    rprint("keep the path which contains GigabitEthernet1 and return the list of value of out_pkts key :", \
      Dq(interfaces).contains("GigabitEthernet1").get_values("out_pkts"))

    rprint("keep the path which contain the key_value pair of enable_True and return the index of 0 of the ouput list: ", \
      interfaces.q.contains_key_value('enabled', True).get_values("[0]"))

    rprint("keep the path which contain the key_value pair of enable_True and return the key out_pkts: ", \
      interfaces.q.not_contains_key_value('enabled', False).get_values("out_pkts"))

    rprint("keep the path which the value of in_crc_errors is less than 100 and from the list output return the first element : ", \
      interfaces.q.value_operator('in_crc_errors', '<', 100).get_values('[0]',0))

    rprint("count the number of elemenet matching the key in_crc_errors with the value greater  than 100 : ", \
      interfaces.q.value_operator('in_crc_errors', '>', 100).count())

    rprint("keep the path with key of line_protocol which value is matched with regex u.* : ", \
      interfaces.q.contains_key_value('line_protocol', 'u.*', value_regex=True))

    rprint("keep the path with key matching with regex line.* and the value of up : ", \
      interfaces.q.contains_key_value('line.*', 'up', key_regex=True))

results=nr.run(task=genie_Dq_example)

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
