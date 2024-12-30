*** Settings ***
# Importing test libraries, resource files and variable files.
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot
Library        genie.libs.robot.GenieRobotApis
Library        unicon.robot.UniconRobot

*** Variables ***
${testbed}         testbed.yaml
${PRE}             /home/majid/devnet/pyats/pre
${POST}            /home/majid/devnet/pyats/post
${F_NAME}          Danny
${L_NAME}          Wade

*** Test Cases ***
# Creating test cases from available keywords.
Connect to device
    # Specify testbed file to use
    use genie testbed "${testbed}"
    connect to devices "R1;R2"

Greeting 
    Log    Hello, ${F_NAME} ${L_NAME}

Profile bgp on All 
    Profile the system for "bgp" on devices "R1;R2" as "${PRE}"
    Log    Profile saved at ${PRE}
parser show version 
    ${output}=    parse "show version" on device "R1"
    Log    ${output}
    Set Suite Variable    ${parsed_output}    ${output}

Verify version
    ${result}=    dq query    data=${parsed_output}    filters=contains('version').get_values('version')('version')

Learn bgp 
    ${output}=    learn "bgp" on device "R1"

verify bgp neighbor count 
    verify count "1" "bgp neighbors" on device "R1"

verify bgp routes 
    verify count "0" "bgp routes" on device "R1"

#Execute command
#    configure "router bgp 65001" on device "R1"
#    configure "router bgp 65001\n network 10.10.10.10 mask 255.255.255.255" on device "R1"

Profile bgp on All and Compare
    Profile the system for "bgp" on devices "R1;R2" as "${POST}"
    Log    Profile saved at ${POST}
    Compare profile "${PRE}" with "${POST}" on devices "R1;R2"

Disconnect from device
    disconnect from device "R1"
    disconnect from device "R2"

# pyats run robot 10.2.pyats_robot_genie_keywords.robot
