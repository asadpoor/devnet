############## Find all ospf neighbors in full state ##############

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
parsed_output = R1.parse("show ip ospf neighbor")

#if
#  parsed_output["interfaces"]["GigabitEthernet1"]["neighbors"]["2.2.2.2"]["state"] contains "FULL"
#then
#  2.2.2.2

#or

#if
#  parsed_output["interfaces"][interface]["neighbors"][neighbor]["state"] contains "FULL"
#then
#  neighbor


for interface in parsed_output["interfaces"].keys():
  for neighbor in parsed_output["interfaces"][interface]["neighbors"].keys():
    if "FULL" in parsed_output["interfaces"][interface]["neighbors"][neighbor]["state"]:
      print(neighbor)

# no coorrect output
print(parsed_output.q.contains("FULL").get_values("neighbors"))

#ipdb.set_trace()

# Disconnect from the device
R1.disconnect()
