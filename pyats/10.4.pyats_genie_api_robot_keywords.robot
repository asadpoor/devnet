*** Settings ***
Library    ats.robot.pyATSRobot
#Library    unicon.robot.UniconRobot
Library    genie.libs.robot.GenieRobot
Library    genie.libs.robot.GenieRobotApis

*** Variables ***
${testbed}         testbed.yaml
${neighbor_ip}     1.1.1.1

*** Test Cases ***
Connect to Devices
    use genie testbed "${testbed}"
    connect to device "R2"

*** Test Cases ***
Verify Interfaces Names With Genie API
    Log To Console    \n=== Starting Interfaces Check ===
    ${interfaces}=    Get Interface Names    device=R2
    Set Suite Variable    ${interfaces}
    Log To Console    \nInterfaces:\n${interfaces}

Verify Interfaces Info With Genie API
    Log To Console    \n=== Starting Interfaces Info Check ===
    ${info}=    Get Interface Information    device=R2    interface_list=${interfaces}

    FOR    ${name}    ${data}    IN    &{info}
        Run Keyword If    '${data.oper_status}' != 'up' or '${data.line_protocol}' != 'up'    Fail    Interface ${name} is down (oper_status=${data.oper_status}, line_protocol=${data.line_protocol})
    END

    Log To Console    All interfaces are UP

Verify BGP Routes With Genie API
    Log To Console    \n=== Starting BGP Route Check ===
    ${routes}=    Get Bgp Best Routes    device=R2    neighbor_address=${neighbor_ip}
    Log To Console    \nBGP Best Routes for neighbor ${neighbor_ip}:\n${routes}

