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
        aetest.loop.mark(Test_Cisco_IOS_XE_Interfaces, device_name=testbed.devices)

# ---------------
# Test Case #1
# ---------------
class Test_Cisco_IOS_XE_Interfaces(aetest.Testcase):
    """Parse pyATS learn interface and test against thresholds"""

    @aetest.test
    def setup(self, testbed, device_name):
        """Testcase Setup section"""
        # Set current device in loop as self.device
        self.device = testbed.devices[device_name]

    @aetest.test
    def get_parsed_version(self):
        parsed_version = self.device.learn("interface")
        # Get the JSON payload
        self.parsed_json = parsed_version.info

    @aetest.test
    def create_file(self):
        """Create .JSON file"""
        with open(f'{self.device.alias}_Learn_Interface.json', 'w') as f:
            f.write(json.dumps(self.parsed_json, indent=4, sort_keys=True))

    @aetest.test
    def test_interface_health(self):
        """Test for interface health"""

        # Specify the filename where the results will be stored
        output_filename = "AI_interfaces.txt"

        for intf, value in self.parsed_json.items():
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                #model="gpt-3.5-turbo",
                #model="gpt-4",
                #model="gpt-4-turbo",
                messages=[ 
                    {"role": "system", "content": "You are a helpful network assistant who will help the user determine the health of a Cisco interface with the help of the interface state as JSON."},
                    {"role": "user", "content": f"Please use this JSON and help me understand the state of this interface. Are there any issues or is the interface healthy? Interface { intf } state: { value }"}
                ]
            )

            choices = response.choices
            if choices:
                choice = choices[0]
                content = choice.message.content
                openai_output = f"OPENAI RESPONSE for Interface {intf}:\n{content}"
                
                # Log the OpenAI response with clear labeling
                log.info(f"OPENAI RESPONSE for Interface {intf}:")
                log.info(content)  # This logs the actual response
                print(openai_output)  # Display the response on the console as well

                # Write the AI response to the file
                with open(output_filename, 'a') as file:
                    file.write(openai_output)  # Append to the file

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        testbed.disconnect()

# For running as its own executable
if __name__ == '__main__':
    aetest.main(testbed=testbed)
