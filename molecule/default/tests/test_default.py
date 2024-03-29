import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_kubectl_config_exists(host):
    f = host.file('/root/.zshrc.d/50-kubectl')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
