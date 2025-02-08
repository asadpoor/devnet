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
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("pyats_openai_log.log", mode='w')
    ]
)

# Load API keys from environment
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Instantiate OpenAI client
client = OpenAI()

# ---------------
# AE Test Setup
# ---------------

class CommonSetup(aetest.CommonSetup):
    """Common Setup section"""
    
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all devices"""
        self.parameters['testbed'].connect()

    @aetest.subsection
    def loop_mark(self, testbed):
        """Mark test cases to loop over devices"""
        device_names = [device.name for device in testbed.devices.values()]
        aetest.loop.mark(Test_Logs_Analysis, device_name=device_names)

# ---------------
# Test Case #1
# ---------------
class Test_Logs_Analysis(aetest.Testcase):
    """Parse pyATS learn interface and test against thresholds"""

    @aetest.setup
    def setup(self, testbed, device_name):
        """Setup test case"""
        self.device = testbed.devices[device_name]

    @aetest.test
    def get_raw_logs(self):
        """Get raw logs"""
        parsed_version = self.device.parse("show logging")
        #log.info(f"Parsed logs: {parsed_version}")
        self.parsed_json = parsed_version.get('logs', [])

    @aetest.test
    def test_logs(self):
        """Analyze the last 10 lines of the logs"""
        if not self.parsed_json:
            log.error("No logs found to analyze.")
            return
        
        log_lines = "\n".join(self.parsed_json).strip().splitlines()
        last_10_lines = "\n".join(log_lines[-10:])

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful network assistant."},
                {"role": "user", "content": f"Analyze these Cisco logs:\n{last_10_lines}"}
            ]
        )

        if response.choices:
            content = response.choices[0].message.content
            log.info(f"Log Analysis:\n{content}")

            with open('syslogs.txt', 'a') as file:
                file.write("Log Analysis:\n")
                file.write(content + "\n")

# ---------------
# Cleanup
# ---------------
class CommonCleanup(aetest.CommonCleanup):
    """Cleanup after test"""
    
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        self.parameters['testbed'].disconnect()

# Run script
if __name__ == '__main__':
    aetest.main(testbed=testbed)
