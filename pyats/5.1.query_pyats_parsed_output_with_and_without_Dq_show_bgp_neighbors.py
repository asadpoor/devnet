############## Find all bgp neighbors in established state ##############

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
parsed_output = R1.parse("show bgp neighbors")

#if
#  parsed_output["vrf"]["default"]["neighbor"]["192.168.2.92"]["session_state"] == 'Established'
#then
#  192.168.2.92

#or

#if
#  parsed_output["vrf"]["default"]["neighbor"][neighbor]["session_state"] == 'Established'
#then
#  neighbor


for n in parsed_output["vrf"]["default"]["neighbor"].keys():
  if parsed_output["vrf"]["default"]["neighbor"][n]["session_state"] == "Established":
    print(n)

print(parsed_output.q.contains("Established").get_values("neighbor"))


#ipdb.set_trace()

# Disconnect from the device
R1.disconnect()
