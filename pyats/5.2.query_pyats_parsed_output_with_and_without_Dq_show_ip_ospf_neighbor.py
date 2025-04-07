############## Find all ospf neighbors in full state ##############

from genie.testbed import load
from genie.libs.parser.ios import show_interface
from pprint import pprint
import json
from genie.utils import Dq
import ipdb

testbed = load('testbed.yaml')
device = testbed.devices['R2']
device.connect(log_stdout=False)

parsed_output = device.parse('show ip ospf neighbor')

# to show clean structured ouput use pprint or json.dumps
#pprint(parsed_output)
print(json.dumps(parsed_output, indent=2))


print("\nlist of ospf neighbors in full state extracted from loop:")
for interface in parsed_output["interfaces"].keys():
  for neighbor in parsed_output["interfaces"][interface]["neighbors"].keys():
    if "FULL" in parsed_output["interfaces"][interface]["neighbors"][neighbor]["state"]:
      print(neighbor)

print("\nlist of ospf neighbors in full state extracted from Dq:")
print(parsed_output.q.contains("FULL/DR").get_values("interfaces"))
print(parsed_output.q.contains("FULL/DR").get_values("neighbors"))

#ipdb.set_trace()

# Disconnect from the device
device.disconnect()
