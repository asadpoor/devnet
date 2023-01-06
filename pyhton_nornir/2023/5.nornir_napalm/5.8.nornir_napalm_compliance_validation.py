from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_validate
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_napalm_compliance_validation_check(task):
    task.run(task=napalm_validate, src="ntp.yaml")

results = nr.run(task= nornir_napalm_compliance_validation_check)
print_result(results)
