*** Settings ***

Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot
Library        genie.libs.robot.GenieRobotApis
Library        unicon.robot.UniconRobot

*** Test Cases ***

Connect to device
    use testbed "testbed.yaml"
    connect to all devices

Execute NTP Commands
    configure "ntp server 77.77.77.77" on devices "R1"

Verify NTP is synchronized on device "R1"

Disconnect from device
    disconnect from all devices

# pyats run robot ntp.robot --testbed-file testbed.yaml
