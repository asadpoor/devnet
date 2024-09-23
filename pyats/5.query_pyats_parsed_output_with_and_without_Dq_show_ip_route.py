############## Find all the routes which are connected ##############

import json
from genie.testbed import load
import ipdb

# Load the testbed file
testbed = load("testbed.yaml")

# Get all devices from the testbed
devices = testbed.devices

R1 = testbed.devices["R1"]

# Connect to device, learn BGP feature, and disconnect from the device
R1.connect(log_stdout=False)
parsed_output = R1.parse("show ip route")

#if
#  parsed_output["vrf"]["default"]["address_family"]["ipv4"]["routes"]["172.16.1.1/32"]["source_protocol"] == connected
#then
#  172.16.1.1/32

#or

#if
#  parsed_output["vrf"]["default"]["address_family"]["ipv4"]["routes"][route]["source_protocol"] == connected
#then
#  route


for route in parsed_output["vrf"]["default"]["address_family"]["ipv4"]["routes"]:
  if parsed_output["vrf"]["default"]["address_family"]["ipv4"]["routes"][route]["source_protocol"] == "connected":
    print(route)

print(parsed_output.q.contains('connected').get_values('routes'))
print(parsed_output.q.contains('ospf').get_values('routes'))

#ipdb.set_trace()

# Disconnect from the device
R1.disconnect()
