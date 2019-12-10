# coding: utf-8

"""
    DLRN API Ansible Module Test
"""


from __future__ import absolute_import
import dlrnapi_client
import os


def test_ansible():
    p = os.path.join(os.path.dirname(dlrnapi_client.__file__), "ansible")
    # os.environ['ANSIBLE_LIBRARY'] = p

    x = os.system(
        "ANSIBLE_LIBRARY=%s "
        "ansible -vv -i localhost, --connection=local localhost -m dlrn_api "
        "-a 'action=repo-get "
        "host=https://trunk.rdoproject.org/api-centos-master-uc'" % p)
    assert x == 0
