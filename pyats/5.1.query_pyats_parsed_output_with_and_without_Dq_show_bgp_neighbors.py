############## Find all bgp neighbors in established state ##############

from genie.testbed import load
from genie.libs.parser.ios import show_interface
from pprint import pprint
import json
from genie.utils import Dq
import ipdb

testbed = load('testbed.yaml')
device = testbed.devices['R2']
device.connect(log_stdout=False)

parsed_output = device.parse('show bgp neighbors')

# to show clean structured ouput use pprint or json.dumps
#pprint(parsed_output)
print(json.dumps(parsed_output, indent=2))

print("\nlist of BGP established neighbors without using Dq filter: ")
for neighbor in parsed_output["vrf"]["default"]["neighbor"].keys():
  if parsed_output["vrf"]["default"]["neighbor"][neighbor]["session_state"] == "Established":
    print(neighbor)

print("\nlist of BGP established neighbors extracted using Dq filter: ")
print(parsed_output.q.contains("Established").get_values("neighbor"))

#ipdb.set_trace()

device.disconnect()
