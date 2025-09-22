# pip install pyats genie.libs
# pip install openai
# export OPENAI_API_KEY="your_api_key_here"


import os
import json
import logging
import pytest
from genie.testbed import load
from openai import OpenAI

# Setup logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# OpenAI API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise RuntimeError("Please set the OPENAI_API_KEY environment variable.")

# Instantiate OpenAI client
client = OpenAI(api_key=openai_api_key)

# Load your pyATS testbed YAML
TESTBED_FILE = "testbed.yaml"  # Change this to your testbed file
testbed = load(TESTBED_FILE)

# Connect to all devices
log.info("Connecting to devices...")
testbed.connect()

def save_json(data, filename="interface_data.json"):
    """Save JSON data to a file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def analyze_interface_with_ai(interface_state):
    """Send interface JSON to OpenAI GPT for health analysis."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful network assistant who will analyze Cisco 'show ip interface brief' JSON and report its health."
            },
            {
                "role": "user",
                "content": f"Please analyze this JSON and tell me if the interfaces are healthy or have issues:\n{json.dumps(interface_state)}"
            }
        ]
    )
    ai_output = response.choices[0].message.content
    return ai_output

# Main test
for device_name, device in testbed.devices.items():
    log.info(f"Parsing 'show ip interface brief' on device: {device_name}")
    try:
        # Parse command instead of learn
        parsed_json = device.parse("show ip interface brief")
        save_json(parsed_json, f"{device_name}_show_ip_int_brief.json")

        # Analyze the whole parsed result at once
        log.info(f"Analyzing interfaces on {device_name}...")
        ai_result = analyze_interface_with_ai(parsed_json)
        log.info(f"AI analysis for {device_name}:\n{ai_result}\n")

    except Exception as e:
        log.error(f"Error on device {device_name}: {e}")

# Disconnect devices after testing
log.info("Disconnecting devices...")
testbed.disconnect()

log.info("Test complete.")

