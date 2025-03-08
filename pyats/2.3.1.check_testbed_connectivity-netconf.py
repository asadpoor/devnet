# Import the logging module to enable logging within the script
import logging

# Import the loader module from pyATS to handle testbed files
from pyats.topology import loader

# Set up logging with the DEBUG level to capture detailed information
logging.basicConfig(level=logging.DEBUG)

# Load the testbed configuration from the specified YAML file
# This file defines the devices and their connection details
testbed = loader.load('2.3.testbed-netconf.yaml')

# Access the device named 'R1' from the testbed
# 'R1' should be defined in the testbed YAML file with its connection parameters
device = testbed.devices['R1']

# Establish a NETCONF connection to 'R1'
# This uses the NETCONF details specified in the testbed file
device.connect(via='netconf')

# Perform desired operations on the device here
# For example, you can send NETCONF RPCs or retrieve information

# Disconnect the NETCONF session to 'R1'
# It's important to close the connection after operations are complete
device.netconf.disconnect()
