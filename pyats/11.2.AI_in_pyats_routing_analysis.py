import os
import json
import logging
from pyats import aetest
from openai import OpenAI
from rich.table import Table
from dotenv import load_dotenv
from rich.console import Console
from genie.utils.diff import Diff
from pyats.log.utils import banner
from pyats.topology import loader

# Load the testbed from the YAML file
testbed = loader.load("testbed.yaml")

# ---------------
# Get logger for script
# ---------------
log = logging.getLogger(__name__)

# Set up logging to a file and console
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of the log entries
    handlers=[
        logging.StreamHandler(),  # Output to console
        logging.FileHandler("pyats_openai_log.log", mode='w')  # Output to log file
    ]
)

# Instantiate OpenAI client
load_dotenv()

# Load the API keys from an environment variable or secure source
openai_api_key = os.getenv('OPENAI_API_KEY')

# Instantiate OpenAI client
client = OpenAI()

# ---------------
# AE Test Setup
# ---------------

# Modify the connect_to_devices to accept the testbed as an argument explicitly
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
    
    @aetest.subsection
    def connect_to_devices(self):
        """Connect to all the devices"""
        testbed.connect()

    # ---------------
    # Mark the loop for Learn Interfaces
    # ---------------
    @aetest.subsection
    def loop_mark(self, testbed):
        aetest.loop.mark(Test_Cisco_IP_Route, device_name=testbed.devices)

# ---------------
# Test Case #1
# ---------------
class Test_Cisco_IP_Route(aetest.Testcase):
    """Parse pyATS learn interface and test against thresholds"""

    @aetest.test
    def setup(self, testbed, device_name):
        """Testcase Setup section"""
        # Set current device in loop as self.device
        self.device = testbed.devices[device_name]

    @aetest.test
    def get_ip_route(self):
        self.ip_routes = self.device.parse("show ip route")

    @aetest.test
    def test_ip_route(self):
        # Test ip route
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            #model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful network assistant who will help the user understand the Cisco IOS XE device's routing table."},
                {"role": "user", "content": f"Please analyze the following Cisco IOS XE routing table and help me understand the state of this device's routing table. Summarize and highlight anything important such as the default route or other key pieces of information.\n { self.ip_routes }"},
            ]
        )
        choices = response.choices
        if choices:
            choice = choices[0]
            content = choice.message.content
            log.info("Please analyze the following Cisco IOS XE routing table and help me understand the state of this device's routing table. Summarize and highlight anything important such as the default route or other key pieces of information.")
            log.info(content)
    
            # Create and format the strings
            line1 = "Please analyze the following Cisco IOS XE routing table and help me understand the state of this device's routing table. Summarize and highlight anything important such as the default route or other key pieces of information."
            line2 = content + "\n"
    
            # Append the strings to a file
            with open('routing_table.txt', 'w') as file:
                file.write(line1)
                file.write(line2)

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        testbed.disconnect()

# For running as its own executable
if __name__ == '__main__':
    aetest.main(testbed=testbed)
