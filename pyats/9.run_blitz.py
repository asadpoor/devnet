import os
from genie.harness.main import gRun

def main(runtime):
    gRun(
        trigger_datafile='9.6.blitz_parse_1.yaml',
        testbed='testbed.yaml',
        trigger_uids=['Testcase1']
    )

# pyats run job 9.run_blitz.py
