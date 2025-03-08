# Import the loader module from pyATS to handle testbed files
from pyats.topology import loader

# Load the testbed configuration from the specified YAML file
# This file defines the devices and their connection details
testbed = loader.load('2.1.testbed-cli.yaml')

# Access the device named 'R1' from the testbed
# 'R1' should be defined in the testbed YAML file with its connection parameters
device = testbed.devices['R1']

# Establish a CLI (Command-Line Interface) connection to 'R1'
# This uses the connection details specified in the testbed file
device.connect(via='cli')

# Perform desired operations on the device here
# For example, you can execute commands or retrieve information

# Disconnect the CLI session to 'R1'
# It's important to close the connection after operations are complete
device.disconnect()
