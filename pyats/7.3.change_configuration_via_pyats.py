from genie.testbed import load

# Load your testbed YAML file
testbed = load('testbed.yaml')

# Get the device from the testbed
device = testbed.devices['R1']

# Connect to the device
print(f"Connecting to device {device.name}...")
device.connect(log_stdout=False)
print(f"Successfully connected to {device.name}.")

# Configuration commands to send
config_commands = """
interface GigabitEthernet3
 description Configured by pyATS
 ip address 192.168.168.1 255.255.255.0
 shutdown
"""

print(f"Starting configuration on device {device.name}...")

try:
    device.configure(config_commands)
    print(f"Configuration applied successfully on {device.name}.")
except SubCommandFailure as e:
    print(f"Configuration failed on {device.name}: {e}")

# Disconnect from the device
device.disconnect()
print(f"Disconnected from {device.name}.")
