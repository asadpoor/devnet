*** Settings ***
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot
Library        genie.libs.robot.GenieRobotApis
Library        unicon.robot.UniconRobot

*** Variables ***
${testbed}         testbed.yaml

*** Test Cases ***
Connect to device
    use testbed "${testbed}"
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
