"""
Automation Easy Testing (AEtest): a framework designed to standardize the definition and execution of network test cases.
https://pubhub.devnetcloud.com/media/pyats/docs/aetest/index.html
"""

# Import necessary modules
from pyats import aetest  # AEtest framework is part of pyATS
from genie.testbed import load  # For loading testbed files

# Common Setup section: Sets up the environment for all test cases
class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_testbed(self):
        """
        Connect to the devices in the testbed.
        This is where you load and connect to the devices using the testbed file.
        """
        # Replace with actual testbed file path
        self.testbed = load('path_to_testbed.yaml')
        # Connect to all devices in the testbed
        self.testbed.connect()  # Establish connections

    @aetest.subsection
    def prepare_testcases(self):
        """
        Prepare for test cases.
        Configure test parameters, set up the environment, etc.
        """
        pass  # Placeholder for preparation steps

# Testcase 1: Example of a test case with setup, two tests, and cleanup
class TestcaseOne(aetest.Testcase):

    @aetest.setup
    def setup(self):
        """
        Setup for TestcaseOne.
        Perform any necessary setup steps before the tests.
        """
        pass  # Placeholder for setup steps

    @aetest.test
    def test_one(self):
        """
        First test in TestcaseOne.
        This is where the first test logic will be executed.
        Each test in this test case is executed sequentially.
        """
        pass  # Placeholder for first test logic

    @aetest.test
    def test_two(self):
        """
        Second test in TestcaseOne.
        This is where the second test logic will be executed.
        """
        pass  # Placeholder for second test logic

    @aetest.cleanup
    def cleanup(self):
        """
        Cleanup after TestcaseOne execution.
        Perform any necessary cleanup tasks after the tests.
        """
        pass  # Placeholder for cleanup steps

# Testcase 2: Another test case example with setup, test, and cleanup
class TestcaseTwo(aetest.Testcase):

    @aetest.setup
    def setup(self):
        """
        Setup for TestcaseTwo.
        Prepare any resources required for the test.
        """
        pass  # Placeholder for setup steps

    @aetest.test
    def execute_test(self):
        """
        Main test logic for TestcaseTwo.
        This is where the test is performed.
        """
        pass  # Placeholder for test logic

    @aetest.cleanup
    def cleanup(self):
        """
        Cleanup after TestcaseTwo execution.
        Ensure resources are cleaned up after the test.
        """
        pass  # Placeholder for cleanup steps

# Common Cleanup section: Disconnect from the testbed after all tests
class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_testbed(self):
        """
        Disconnect from the devices.
        This is where you disconnect all the devices in the testbed.
        """
        self.testbed.disconnect()  # Close connections

# Main section to run the script
if __name__ == '__main__':
    aetest.main()  # Trigger AEtest main function to execute the test cases
