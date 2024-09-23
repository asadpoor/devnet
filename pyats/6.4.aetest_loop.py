import time
import difflib
from pyats import aetest
from pyats.topology import loader
from genie.utils.diff import Diff

# Load the testbed file
testbed = loader.load('testbed.yaml')

class common_setup(aetest.CommonSetup):
    """Common Setup Section"""
    
    @aetest.subsection
    def connect_to_devices(self):
        # Connect to devices
        testbed.connect()

    @aetest.subsection
    def loop_mark(self):
        # Mark test case for loops in case there are more than 1 device in the testbed
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
    def capture_show_ip_interface(self):
        self.show_interfaces = self.device.parse("show interfaces")

    @aetest.test
    def capture_show_ip_interface_brief(self):
        self.show_ip_interface_brief = self.device.parse("show ip interface brief")

    @aetest.test
    def capture_show_ip_route(self):
        self.show_ip_route = self.device.parse("show ip route")

    @aetest.test
    def make_change(self):
        self.device.configure('''
            interface loopback100
            description "This is a new loopback"
            ip address 192.168.100.100 255.255.255.0
            no shut
        ''')

    @aetest.test
    def recapture_show_run(self):
        self.new_show_run = self.device.execute("show run")

    @aetest.test
    def recapture_show_ip_interface(self):
        self.new_show_interfaces = self.device.parse("show interfaces")

    @aetest.test
    def recapture_show_ip_interface_brief(self):
        self.new_show_ip_interface_brief = self.device.parse("show ip interface brief")

    @aetest.test
    def recapture_show_ip_route(self):
        time.sleep(10)
        self.new_show_ip_route = self.device.parse("show ip route")

    @aetest.test
    def perform_show_run_diff(self):
        pre_change = self.show_run
        post_change = self.new_show_run
        diff = difflib.ndiff(pre_change.splitlines(), post_change.splitlines())
        show_run_diff_output = '\n'.join([line for line in diff if line.startswith('-') or line.startswith('+')])
        with open('Show_Run_Diff.txt', 'w') as f:
            f.write(show_run_diff_output)

    @aetest.test
    def perform_show_interface_diff(self):
        interface_pre_change = self.show_interfaces
        interface_post_change = self.new_show_interfaces
        interface_diff = Diff(interface_pre_change, interface_post_change)
        interface_diff.findDiff()
        with open('Show_Interfaces_Diff.txt', 'w') as f:
            f.write(str(interface_diff))

    @aetest.test
    def perform_show_ip_interface_brief_diff(self):
        ip_interface_brief_pre_change = self.show_ip_interface_brief
        ip_interface_brief_post_change = self.new_show_ip_interface_brief
        ip_interface_brief_diff = Diff(ip_interface_brief_pre_change, ip_interface_brief_post_change)
        ip_interface_brief_diff.findDiff()
        with open('Show_IP_Interface_Brief_Diff.txt', 'w') as f:
            f.write(str(ip_interface_brief_diff))

    @aetest.test
    def perform_show_ip_route_diff(self):
        ip_route_pre_change = self.show_ip_route
        ip_route_post_change = self.new_show_ip_route
        ip_route_diff = Diff(ip_route_pre_change, ip_route_post_change)
        ip_route_diff.findDiff()
        with open('Show_IP_Route_Diff.txt', 'w') as f:
            f.write(str(ip_route_diff))

class common_cleanup(aetest.CommonCleanup):
    """Common Cleanup Section"""
    
    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    # Run the test
    aetest.main()
