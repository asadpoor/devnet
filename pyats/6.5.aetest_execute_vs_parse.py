from pyats import aetest
from pyats.topology import loader
import json  # Import json for formatting output

# Load the testbed file
testbed = loader.load('testbed.yaml')

class MyCommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect()

class MyTestcase(aetest.Testcase):
    @aetest.setup
    def setup(self):
        self.devices = testbed.devices
        self.ping_result = {}
        
        # Execute ping command for each device
        for device_name, device in self.devices.items():
            self.ping_result[device_name] = device.execute("ping 8.8.8.8")

    @aetest.test
    def test_ping(self):
        ping_errors = []
        for device_name, result in self.ping_result.items():
            print(f"{device_name} ping result: {result}")  # Print the result for debugging

            # Check for success rate in the ping results
            if "Success rate is 0 percent" in result or "Error" in result or "Timeout" in result:
                ping_errors.append({
                    'device': device_name,
                    'result': result
                })

        if ping_errors:
            self.failed(f"Ping test failed for the following devices: {json.dumps(ping_errors, indent=2)}")
        else:
            self.passed("Ping test passed for all devices.")

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    aetest.main()
