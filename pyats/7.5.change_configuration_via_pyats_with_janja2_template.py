import os
import yaml
from jinja2 import Environment, FileSystemLoader
from genie.testbed import load

# Load testbed
testbed = load('testbed.yaml')

# Set paths
template_path = 'templates'
data_path = 'data'
template_file = 'interface_config.j2'

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader(template_path))

# Load Jinja2 template
template = env.get_template(template_file)

# Iterate over devices in testbed
for device_name, device in testbed.devices.items():
    print(f"\n[INFO] Processing {device_name}")

    # Load corresponding YAML data file
    data_file = os.path.join(data_path, f"{device_name}.yaml")
    with open(data_file) as f:
        data = yaml.safe_load(f)

    # Render configuration from Jinja2 template
    config = template.render(data)
    print(f"[INFO] Rendered config:\n{config}")

    # Connect to the device
    device.connect(log_stdout=False)
    print(f"[INFO] Connected to {device_name}")

    # Send the rendered config
    device.configure(config)
    print(f"[INFO] Configuration sent to {device_name}")

    # Disconnect
    device.disconnect()
    print(f"[INFO] Disconnected from {device_name}")
