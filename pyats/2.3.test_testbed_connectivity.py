from pyats.topology import loader

# Load the testbed
testbed = loader.load('testbed.yaml')

# Access the device
device = testbed.devices['R1']

# Connect using CLI (default)
device.connect()

# Or connect using REST
device.connect(alias='rest')

# Or connect using NETCONF
device.connect(alias='netconf')
