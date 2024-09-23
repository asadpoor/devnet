from genie.testbed import load

testbed = load("testbed.yaml")

devices = testbed.devices
for device_name, device in devices.items():
  print("device name = ", device_name)
  print("device = ", device)
  print("\n")

R1 = testbed.devices["R1"]

# Connect to device, learn BGP feature, and disconnect from the device
R1.connect()
ospf_state = R1.learn("ospf")
R1.disconnect()

# Print BGP feature output
print(ospf_state.info)


