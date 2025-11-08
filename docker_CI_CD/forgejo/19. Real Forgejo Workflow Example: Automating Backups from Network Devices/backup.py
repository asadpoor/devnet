#!/usr/bin/env python3

import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

# Read credentials from environment
DEVICE_USERNAME = os.getenv("DEVICE_USERNAME")
DEVICE_PASSWORD = os.getenv("DEVICE_PASSWORD")

if not DEVICE_USERNAME or not DEVICE_PASSWORD:
    raise ValueError(
        "Environment variables DEVICE_USERNAME and DEVICE_PASSWORD must be set!"
    )

# Initialize Nornir
nr = InitNornir(config_file="config.yaml")

# Optionally, override host credentials dynamically
for host in nr.inventory.hosts.values():
    host.username = DEVICE_USERNAME
    host.password = DEVICE_PASSWORD

BACKUP_DIR = "./backup"
os.makedirs(BACKUP_DIR, exist_ok=True)

def backup_config(task):
    result = task.run(task=send_command, command="show running-config")
    filename = os.path.join(BACKUP_DIR, f"{task.host.name}.cfg")
    with open(filename, "w") as f:
        f.write(result.result)
    task.log(f"Backup saved to {filename}")

results = nr.run(task=backup_config)
print_result(results)
