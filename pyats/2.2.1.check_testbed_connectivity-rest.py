# Import the logging module to enable logging within the script
import logging

# Import the urllib3 module to handle HTTP requests
import urllib3

# Import the loader module from pyATS to handle testbed files
from pyats.topology import loader

# Import the warnings module to manage warning messages
import warnings

# Suppress specific warnings related to deprecated arguments
warnings.filterwarnings("ignore", message="default_tokens is a deprecated argument")

# Disable warnings about insecure HTTP requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set up logging with the DEBUG level to capture detailed information
logging.basicConfig(level=logging.DEBUG)

# Load the testbed configuration from the specified YAML file
# This file defines the devices and their connection details
testbed = loader.load('2.2.testbed-rest.yaml')

# Access the device named 'R1' from the testbed
# 'R1' should be defined in the testbed YAML file with its connection parameters
device = testbed.devices['R1']

# Establish a REST connection to 'R1'
# This uses the REST API details specified in the testbed file
device.connect(via='rest')

# Perform desired operations on the device here
# For example, you can send REST API requests or retrieve information

# Disconnect the REST session to 'R1'
# It's important to close the connection after operations are complete
device.rest.disconnect()
