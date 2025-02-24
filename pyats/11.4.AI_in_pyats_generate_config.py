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

# Load OpenAI API key
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()

# ---------------
# AE Test Setup
# ---------------

class common_setup(aetest.CommonSetup):
    """Common Setup section"""

    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect()

    @aetest.subsection
    def loop_mark(self, testbed):
        aetest.loop.mark(Generate_Config, device_name=list(testbed.devices.keys()))


# ---------------
# Test Case
# ---------------
class Generate_Config(aetest.Testcase):
    """Parse pyATS learn interface and test against thresholds"""

    @aetest.setup
    def setup(self, testbed, device_name):
        """Setup section to initialize device"""
        self.device = testbed.devices[device_name]

    @aetest.test
    def generate_loopback_config(self):
        # Test config
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            #model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful Cisco IOS XE network configuration assistant who will help the user generate configuration commands."},
                {"role": "user", "content": "Please generate the configuration for a new logical interface called loopback100 with a description of configuration via AI and an IP address of 192.168.200.200/24. Please also enable the port. Please respond only with the configuration and no notes or other characters."}
            ]
        )
        choices = response.choices
        if choices:
            choice = choices[0]
            self.config = choice.message.content
            print(self.config)

    @aetest.test
    def get_raw_config(self):
        """Configure the device with generated configuration"""
        self.device.configure(self.config.replace("```", "").replace("plaintext", ""))

# ---------------
# Cleanup
# ---------------
class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        testbed.disconnect()


# ---------------
# Main Execution
# ---------------
if __name__ == '__main__':
    aetest.main(testbed=testbed)
