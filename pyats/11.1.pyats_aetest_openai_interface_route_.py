import os
import json
import logging
from pyats import aetest
from openai import OpenAI
from rich.console import Console
from dotenv import load_dotenv
from pyats.topology import loader

# -------------------------
# Load testbed configuration from YAML
# This file defines all network devices and connection details
# -------------------------
testbed = loader.load("testbed.yaml")

# -------------------------
# Configure logging
# Logs are written both to console and a log file (pyats_openai.log)
# -------------------------
log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("pyats_openai.log", mode='w')
    ]
)

# -------------------------
# Load OpenAI API key from environment variables
# Create OpenAI client for API calls
# -------------------------
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

# Rich console provides nice formatting for outputs
console = Console()


# ===================================================
# AEtest Setup Section
# ===================================================
class common_setup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self):
        # Connect to all devices defined in the testbed
        testbed.connect()

    @aetest.subsection
    def loop_mark(self, testbed):
        # Mark the Show_Device_Analysis testcase to run for each device
        aetest.loop.mark(Show_Device_Analysis, device_name=testbed.devices)


# ===================================================
# AEtest Testcase Section
# ===================================================
class Show_Device_Analysis(aetest.Testcase):

    @aetest.test
    def setup(self, testbed, device_name):
        # Get reference to the current device
        self.device = testbed.devices[device_name]

    @aetest.test
    def get_device_data(self):
        # Collect structured interface information
        self.interfaces = self.device.learn("interface")
        self.interfaces_json = json.dumps(self.interfaces.info, indent=2)

        # Parse the routing table
        self.ip_routes = self.device.parse("show ip route")
        self.ip_routes_json = json.dumps(self.ip_routes, indent=2)

    @aetest.test
    def analyze_with_ai(self):
        # Build the AI prompt with routing and interface data
        prompt = (
            f"You are a Cisco network assistant. Analyze the following device data.\n\n"
            f"Routing Table (JSON):\n{self.ip_routes_json}\n\n"
            f"Interface Data (JSON):\n{self.interfaces_json}\n\n"
            "Please provide a summary that includes:\n"
            "- Default routes and important networks\n"
            "- Interface statuses (up/down), IP addresses, and errors\n"
            "- Any inconsistencies between routing and interface configurations\n"
            "- Recommendations for potential issues or misconfigurations"
        )

        # Send request to OpenAI for analysis
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Cisco network assistant that summarizes routing tables and interface data."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract AI output safely
        ai_analysis = response.choices[0].message.content if response.choices else "No analysis returned."

        # Log analysis and also print it nicely to the console
        log.info(f"AI Analysis for device [{self.device.name}]:\n{ai_analysis}")
        console.rule(f"AI Analysis for {self.device.name}")
        console.print(ai_analysis)
        console.rule()


# ===================================================
# AEtest Cleanup Section
# ===================================================
class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        # Disconnect from all devices in the testbed
        testbed.disconnect()


# ===================================================
# Script entry point
# ===================================================
if __name__ == '__main__':
    # Run aetest with the loaded testbed
    aetest.main(testbed=testbed)
