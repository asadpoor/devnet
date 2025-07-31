*** Settings ***
Library        ats.robot.pyATSRobot
Library        unicon.robot.UniconRobot

*** Variables ***
${testbed}         testbed.yaml
${device}          R2

*** Test Cases ***
Configure And Verify Logging
    use testbed "${testbed}"
    connect to device "${device}"

    # ✅ Configure logging settings
    ${config}=    Create List
    ...    logging buffered notifications
    ...    no logging console
    configure "${config}" on device "${device}"

    # ✅ Verify the applied logging config
    ${output}=    execute "show run | include logging" on device "${device}"
    log    ${output}
    should contain    ${output}    logging buffered notifications
    should contain    ${output}    no logging console

    disconnect from device "${device}"
