# pip install robotframework pyats genie
#robot 3.2.profiling_with_robot.robot

*** Settings ***
# Importing test libraries, resource files, and variable files.
Library    pyats.robot.pyATSRobot
Library    genie.libs.robot.GenieRobot

*** Variables ***
${testbed}    testbed.yaml

*** Test Cases ***
Initialize
    # Initializes the pyATS/Genie Testbed
    use genie testbed "${testbed}"

    # Connect to 'R1' device
    connect to device "R1"

Learn OSPF
    # Learn OSPF feature from 'cat8k-rt1' device and assign to 'output' variable
    ${output}=    learn "ospf" on device "R1"
