import json
from genie.testbed import load
from pyats.async_ import pcall
from pyats import aetest
from unicon.core.errors import TimeoutError
from pyats.topology import loader

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all devices defined in the testbed file."""
        testbed.connect()

class PingTest(aetest.Testcase):
    @aetest.setup
    def setup(self, testbed):
        """Setup for PingTest. Load the testbed."""
        self.testbed = load(testbed)  # Ensure the testbed is loaded here

    @aetest.test
    def ping_test(self):
        """Perform a ping test to verify connectivity."""
        def ping_device(device):
            device.connect(log_stdout=False)
            # Execute ping command; adjust as necessary for your environment
            result = device.execute('ping 8.8.8.8')
            return result

        results = pcall(ping_device, device=self.testbed.devices.values())

        ping_errors = []
        for device, result in zip(self.testbed.devices.values(), results):
            if "Timeout Error" in result or "Error" in result:
                ping_errors.append({
                    'device': device.name,
                    'result': result
                })

        if ping_errors:
            self.failed(f"Ping test failed for the following devices: {json.dumps(ping_errors, indent=2)}")
        else:
            self.passed("Ping test passed for all devices.")

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        """Disconnect from all devices."""
        testbed.disconnect()

if __name__ == '__main__':
    # Load the testbed file and pass it explicitly to all sections
    testbed = load("testbed.yaml")
    aetest.main(testbed=testbed)
