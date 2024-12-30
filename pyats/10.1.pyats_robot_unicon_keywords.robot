*** Settings ***
# Importing test libraries, resource files and variable files.
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot
Library        genie.libs.robot.GenieRobotApis
Library        unicon.robot.UniconRobot

*** Variables ***
# Defining variables that can be used elsewhere in the test data.
# Can also be passed in as arguments at runtime
# Must have a testbed.yaml file available in the same directory
# Used to define the testbed devices to connect to
${testbed}         testbed.yaml

*** Test Cases ***
# Creating test cases from available keywords.
Connect to device
    # Specify testbed file to use
    use testbed "${testbed}"
    # Remove default connection commands
    set unicon setting "INIT_CONFIG_COMMANDS" "" on device "R1"
    connect to device "R1"
    connect to device "R2"

Execute command
    execute "show run | include logging host" on device "R1"
    configure "logging host 10.1.1.1" on device "R1"

Execute command in parallel on multiple devices
    execute "show run | include logging host" in parallel on devices "R1;R2"

Disconnect from device
    disconnect from device "R1"


# pyats run robot 10.1.pyats_robot_unicon_keywords.robot
