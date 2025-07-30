*** Settings ***
Library    pyats.robot.pyATSRobot

*** Variables ***
${testbed}    testbed.yaml

*** Test Cases ***
Run My pyATS AEtest
    use testbed "${testbed}"
    connect to device "R1"
    run testcase "aetest_test_a_single_device.TestcaseOne"
    disconnect from device "R1"
