import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_binary(host):
    cmd = host.run('/usr/local/bin/stack --version')

    assert cmd.rc == 0
    assert '1.7.1' in cmd.stdout
