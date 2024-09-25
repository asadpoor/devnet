import time
import difflib
from pyats import aetest
from pyats.topology import loader
from genie.utils.diff import Diff

testbed = loader.load('testbed.yaml')

class common_setup(aetest.CommonSetup):
    """Common Setup Section"""
    
    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect()

    @aetest.subsection
    def loop_mark(self):
        aetest.loop.mark(MyTestcase, device_name=testbed.devices.keys())

class MyTestcase(aetest.Testcase):
    """A sample differential"""
    
    @aetest.test
    def setup(self, device_name):
        self.device = testbed.devices[device_name]

    @aetest.test
    def capture_show_run(self):
        self.show_run = self.device.execute("show run")

    @aetest.test
    def make_change(self):
        self.device.configure('''
            interface loopback100
            description "This is a new loopback interface"
            ip address 10.10.100.100 255.255.255.0
            no shut
        ''')

    @aetest.test
    def recapture_show_run(self):
        self.new_show_run = self.device.execute("show run")

    @aetest.test
    def perform_show_run_diff(self):
        pre_change = self.show_run
        post_change = self.new_show_run
        diff = difflib.ndiff(pre_change.splitlines(), post_change.splitlines())
        show_run_diff_output = '\n'.join([line for line in diff if line.startswith('-') or line.startswith('+')])
        with open('show_run_diff.txt', 'w') as f:
            f.write(show_run_diff_output)

class common_cleanup(aetest.CommonCleanup):
    """Common Cleanup Section"""
    
    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    # Run the test
    aetest.main()
