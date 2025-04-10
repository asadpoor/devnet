############## Find all the routes which are connected ##############

from genie.testbed import load
from genie.libs.parser.ios import show_interface
from pprint import pprint
import json
from genie.utils import Dq
import ipdb

testbed = load('testbed.yaml')
device = testbed.devices['R2']
device.connect(log_stdout=False)

parsed_output = device.parse('show ip route')

# to show clean structured ouput use pprint or json.dumps
#pprint(parsed_output)
print(json.dumps(parsed_output, indent=2))

print("\nconnected routes without Dq filter :")
for route in parsed_output["vrf"]["default"]["address_family"]["ipv4"]["routes"]:
  if parsed_output["vrf"]["default"]["address_family"]["ipv4"]["routes"][route]["source_protocol"] == "connected":
    print(route)

print("\nconnected routes extracted using Dq filter:")
print(parsed_output.q.contains('connected').get_values('routes'))

ipdb.set_trace()

device.disconnect()
