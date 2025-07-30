*** Settings ***
Library        ats.robot.pyATSRobot
Library        unicon.robot.UniconRobot

*** Variables ***
${testbed}         testbed.yaml

*** Test Cases ***
Verify Logging Config
    use testbed "${testbed}"
    connect to device "R1"
    ${output}=    execute "show run | include logging host" on device "R1"
    should contain    ${output}    logging host
    disconnect from device "R1"
