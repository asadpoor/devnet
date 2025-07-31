*** Settings ***
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot
Library        unicon.robot.UniconRobot

*** Variables ***
${testbed}         testbed.yaml

*** Test Cases ***
Connect to Devices
    use genie testbed "${testbed}"
    connect to devices "R1;R2"

Parse Show Version
    ${output}=    parse "show version" on device "R1"
    Log    ${output}
    Set Suite Variable    ${parsed_output}    ${output}

Verify Version Info
    ${result}=    dq query    data=${parsed_output}    filters=contains('version').get_values('version')('version')
    Log    Version extracted: ${result}

Learn BGP on R1
    ${bgp_data}=    learn "bgp" on device "R1"
    Log    ${bgp_data}

Verify BGP Neighbor Count
    verify count "1" "bgp neighbors" on device "R1"

Verify BGP Routes Count
    verify count "0" "bgp routes" on device "R1"

Disconnect from Devices
    disconnect from device "R1"
    disconnect from device "R2"

# pyats run robot 10.2.pyats_robot_genie_keywords.robot
