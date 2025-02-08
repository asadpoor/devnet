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
        aetest.loop.mark(Test_Config, device_name=list(testbed.devices.keys()))


# ---------------
# Test Case
# ---------------
class Test_Config(aetest.Testcase):
    """Parse pyATS learn interface and test against thresholds"""

    @aetest.setup
    def setup(self, testbed, device_name):
        """Testcase Setup section"""
        self.device = testbed.devices[device_name]

    @aetest.test
    def get_raw_config(self):
        self.raw_config = self.device.execute("show run")

    @aetest.test
    def test_config_general(self):
        """Analyze running config using OpenAI API"""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful network assistant who will help the user understand the Cisco IOS XE device's running configuration."},
                {"role": "user", "content": f"Please analyze the following Cisco IOS XE running configuration and help me understand configuration of this device. Summarize and highlight anything important in the configuration.\n\n{self.raw_config}"},
            ]
        )

        choices = response.choices
        if choices:
            choice = choices[0]
            content = choice.message.content

            log.info("Configuration Analysis:")
            log.info(content)

            with open('config.txt', 'w') as file:
                file.write("Configuration Analysis:\n")
                file.write(content + "\n")


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
