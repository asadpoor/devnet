#import json
import time
from genie.testbed import load
from pyats.async_ import pcall
from pyats import aetest
#from genie.conf import Genie

class VersionCheck(aetest.Testcase):
    @aetest.setup
    def setup(self, testbed):
        self.testbed = load(testbed)
        self.ios_xe_devices = [dev for dev in self.testbed.devices.values()]

    @aetest.test
    def check_version(self):
        version_mismatch = []

        def get_version(device):
            # Connect to the device
            device.connect()
            # Parse 'show version' output
            sh_ver = device.parse('show version')
            print(f"Parsed output for {device}:")
            print(sh_ver, "\n\n")

            # Disconnect from the device
            device.disconnect()
            return sh_ver  # Return the parsed output (not 'output' which was undefined)

        # Record the start time
        start_time = time.time()

        # Use pcall correctly by passing the devices as a positional argument
        results = pcall(get_version, device=self.ios_xe_devices)

        # Record the end time
        end_time = time.time()

        # Calculate and print the time taken for the execution
        print(f"Execution time: {end_time - start_time} seconds")

aetest.main(testbed="testbed.yaml")

