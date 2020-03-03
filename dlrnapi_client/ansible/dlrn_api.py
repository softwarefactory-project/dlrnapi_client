#!/usr/bin/python
#   Copyright Red Hat, Inc. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

from ansible.module_utils.basic import AnsibleModule
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from dlrnapi_client.shell import command_funcs

DOCUMENTATION = '''
---
module: dlrn_api
short_description: Ansible module to manage the DLRN API
version_added: "1.0"
author: "jpena <jpena@redhat.com>"
description:
    - Ansible module to manage the DLRN API
options:
    action:
        description:
            - Action to take
        choices: [repo-get, repo-use, repo-status, report-result, repo-promote,
                  repo-promote-batch, commit-import, promotion-get,
                  build-metrics, agg-status]
        required: true
    host:
        description:
            - URL for the DLRN API host
        required: true
    user:
        description:
            - Username for operations requiring authentication. Mandatory if
              action is repo-use, report-result, repo-promote or commit-import
    password:
        description:
            - Password for operations requiring authentication. Mandatory if
              action is repo-use, report-result, repo-promote or commit-import
    reporting_job_id:
        description:
            - If action is repo-use, name of the CI that will add the
              "in progress" entry in the CI job table.
    max_age:
        description:
            - If action is repo-get or repo-use, maximum age in hours for the
              repo to be considered.
        default: 0
    success:
        description:
            - If action is repo-get or repo-use, find repos with a
              successful/unsuccessful vote (as specified). If not set,
              any tested repo will be considered.
            - If action is report-result, was the CI execution successful?
    job_id:
        description:
            - If action is repo-get or repo-use, name of the CI that sent the
              vote. If not set, no filter will be set on CI.
            - If action is report-result, name of the CI sending the vote
    sequential_mode:
        description:
            - If action is repo-get or repo-use, use the sequential mode
              algorithm. In this case, return the last tested repo within that
              timeframe for the CI job described by previous_job_id.
        default: False
    previous_job_id:
        description:
            - If sequential_mode is set to true, look for jobs tested by
              the CI identified by previous_job_id.
    commit_hash:
        description:
            - If action is repo-status, commit_hash of the repo to fetch
              information for.
            - If action is report-result, commit_hash of tested repo.
            - If action is repo-promote, commit_hash of the repo to be
              promoted.
            - If action is promotion-get, filter results for this commit hash.
    distro_hash:
        description:
            - If action is repo-status, distro_hash of the repo to fetch
              information for.
            - If action is report-result, distro_hash of tested repo.
            - If action is repo-promote, distro_hash of the repo to be
              promoted.
            - If action is promotion-get, filter results for this distro hash.
    agg_hash:
        description:
            - If action is report-result, hash of the aggregated repo to
              report a result on.
            - If action is promotion-get or agg-status, filter on the votes or
              promotions related to this aggregated repo hash.
    info_url:
        description:
            - If action is report-result, URL where to find additional
              information from the CI execution.
    timestamp:
        description:
            - If action is report-result, timestamp (in seconds since the
              epoch) for the CI execution
    notes:
        description:
            - If action is report-result, additional notes.
    promote_name:
        description:
            - If action is repo-promote, name to be used for the promotion.
            - If action is promotion-get, filter results by this promotion
              name.
    repo_url:
        description:
            - If action is commit-import, base repository URL for imported
              remote repo
    start_date:
        description:
            - If action is build-metrics, start date to consider for the
              metrics, in YYYY-mm-dd format.
    end_date:
        description:
            - If action is build-metrics, end date to consider for the
              metrics, in YYYY-mm-dd format.
    package_name:
        description:
            - If action is build-metrics, filter results for this package.
    component:
        description:
            - If action is repo-get, repo-use or promotion-get, filter on
              this component.
    hash_pairs:
        description:
            - If action is repo-promote-batch, this is a list of commit_hash
              and distro_hash pairs to be promoted using promote_name.
requirements:
    - "python >= 2.7"
    - "python-dlrnapi_client"
'''

EXAMPLES = '''
# Get the last repo tested by any CI
- dlrn_api:
    action: repo-get
    host: http://dlrn.example.com:5000
  register: result

# Get the last repo tested by any CI in the last 4 hours
- dlrn_api:
    action: repo-get
    host: http://dlrn.example.com:5000
    max_age: 4
  register: result

# Get the last repo, successfully tested by the foo-ci CI, in the last 24 hours
- dlrn_api:
    action: repo-get
    host: http://dlrn.example.com:5000
    max_age: 24
    job_id: foo-ci
    success: true
  register: result

# Get and start using the last repo, that failed testing by the foo-ci CI, in
# the last 6 hours, and mark it as being used by the bar-ci CI
- dlrn_api:
    action: repo-use
    host: http://dlrn.example.com:5000
    user: myuser
    password: mypasswd
    max_age: 6
    reporting_job_id: bar-ci
    job_id: foo-ci
    success: false
  register: result

# Get the CI reports for a specific commit
- dlrn_api:
    action: repo-status
    host: http://dlrn.example.com:5000
    commit_hash: 3a9326f251b9a4162eb0dfa9f1c924ef47c2c55a
    distro_hash: 024e24f0cf4366c2290c22f24e42de714d1addd1
  register: result

# Get the promotions for a specific job
- dlrn_api:
    action: promotion-get
    host: http://dlrn.example.com:5000
    promote_name: foo-ci
  register: result

# Report result on a CI job ran by foo-ci
- dlrn_api:
    action: report-result
    host: http://dlrn.example.com:5000
    user: myuser
    password: mypasswd
    job_id: foo-ci
    commit_hash: 3a9326f251b9a4162eb0dfa9f1c924ef47c2c55a
    distro_hash: 024e24f0cf4366c2290c22f24e42de714d1addd1
    info_url: http://ci.example.com/job_id?1
    timestamp: 1431949433
    success: true
    notes: blablabla

# Promote a repository
- dlrn_api:
    action: repo-promote
    host: http://dlrn.example.com:5000
    user: myuser
    password: mypasswd
    commit_hash: 3a9326f251b9a4162eb0dfa9f1c924ef47c2c55a
    distro_hash: 024e24f0cf4366c2290c22f24e42de714d1addd1
    promote_name: current-passed-ci

# Do a batch promotion
- dlrn_api:
    action: repo-promote-batch
    host: http://dlrn.example.com:5000
    user: myuser
    password: mypasswd
    hash_pairs:
        - commit_hash: 3a9326f251b9a4162eb0dfa9f1c924ef47c2c55a
          distro_hash: 024e24f0cf4366c2290c22f24e42de714d1addd1
        - commit_hash: 3a9326f251b9a4162eb0dfa9f1c924ef47c2c533
          distro_hash: 024e24f0cf4366c2290c22f24e42de714d1addae
    promote_name: current-passed-ci

# Import a remote commit
- dlrn_api:
    action: commit-import
    host: http://dlrn.example.com:5000
    user: myuser
    password: mypasswd
    repo_url: http://builder.example.com/3a9326f251b9a4162eb0_024e24f0
'''
auth_required_actions = ['repo-use', 'report-result', 'repo-promote',
                         'repo-promote-batch', 'commit-import']


class DLRNAPIWrapper(object):
    """Wrapper class

    It is meant to provide the options dict, and a parameter verification
    method
    """
    def __init__(self, params):
        self.reporting_job_id = params.get('reporting_job_id')
        self.max_age = params.get('max_age')
        self.success = params.get('success')
        self.job_id = params.get('job_id')
        self.sequential = params.get('sequential_mode')
        self.previous_job_id = params.get('previous_job_id')
        self.commit_hash = params.get('commit_hash')
        self.distro_hash = params.get('distro_hash')
        self.info_url = params.get('info_url')
        self.timestamp = params.get('timestamp')
        self.notes = params.get('notes')
        self.promote_name = params.get('promote_name')
        self.repo_url = params.get('repo_url')
        self.component = params.get('component')
        self.agg_hash = params.get('agg_hash')
        self.hash_pairs = params.get('hash_pairs')

    def check_options(self, action, module):
        if action == 'repo-use':
            if self.reporting_job_id is None:
                module.fail_json(msg="Missing parameter reporting_job_id")
        elif action == 'report-result':
            if self.agg_hash is not None and\
               (self.commit_hash is not None or self.distro_hash is not None):
                module.fail_json(msg="agg_hash is incompatible with"
                                     "commit_hash and distro_hash")
            if self.agg_hash is None and self.commit_hash is None and\
               self.distro_hash is None:
                module.fail_json(msg="Must specify either agg_hash or"
                                     "commit_hash and distro_hash")
            if (self.commit_hash is not None and self.distro_hash is None):
                module.fail_json(msg="Missing parameter distro_hash")
            if (self.distro_hash is not None and self.commit_hash is None):
                module.fail_json(msg="Missing parameter commit_hash")
            if self.job_id is None:
                module.fail_json(msg="Missing parameter job_id")
            if self.info_url is None:
                module.fail_json(msg="Missing parameter info_url")
            if self.timestamp is None:
                module.fail_json(msg="Missing parameter timestamp")
            if self.success is None:
                module.fail_json(msg="Missing parameter success")
        elif action == 'repo-promote':
            if self.commit_hash is None:
                module.fail_json(msg="Missing parameter commit_hash")
            if self.distro_hash is None:
                module.fail_json(msg="Missing parameter distro_hash")
            if self.promote_name is None:
                module.fail_json(msg="Missing parameter promote_name")
        elif action == 'repo-promote-batch':
            if self.hash_pairs is None:
                module.fail_json(msg="Missing parameter hash_pairs")
            if self.promote_name is None:
                module.fail_json(msg="Missing parameter promote_name")
            # The hash_pairs format is different when passed to the client,
            # so convert it here
            hash_pairs = ''
            for pair in self.hash_pairs[:-1]:
                hash_pairs += '%s_%s,' % (pair['commit_hash'],
                                          pair['distro_hash'])
            hash_pairs += '%s_%s' % (self.hash_pairs[-1]['commit_hash'],
                                     self.hash_pairs[-1]['distro_hash'])
            self.hash_pairs = hash_pairs
        elif action == 'commit-import':
            if self.repo_url is None:
                module.fail_json(msg="Missing parameter repo_url")
        elif action == 'promotion-get':
            if (self.commit_hash is not None and self.distro_hash is None):
                module.fail_json(msg="Missing parameter distro_hash")
            if (self.distro_hash is not None and self.commit_hash is None):
                module.fail_json(msg="Missing parameter commit_hash")
        elif action == 'build-metrics':
            if self.start_date is None:
                module.fail_json(msg="Missing start_date")
            if self.end_date is None:
                module.fail_json(msg="Missing end_date")


def main():
    module = AnsibleModule(
        argument_spec=dict(
            action=dict(required=True,
                        choices=['repo-get', 'repo-use',
                                 'repo-status', 'report-result',
                                 'repo-promote', 'repo-promote-batch',
                                 'commit-import', 'promotion-get',
                                 'build-metrics', 'agg-status']),
            host=dict(required=True),
            user=dict(),
            password=dict(no_log=True),
            reporting_job_id=dict(),
            max_age=dict(default='0', type='int'),
            success=dict(type='bool'),
            job_id=dict(),
            sequential_mode=dict(type='bool', default=False),
            previous_job_id=dict(),
            commit_hash=dict(),
            distro_hash=dict(),
            info_url=dict(),
            timestamp=dict(),
            notes=dict(),
            promote_name=dict(),
            repo_url=dict(),
            start_date=dict(),
            end_date=dict(),
            package_name=dict(),
            component=dict(),
            agg_hash=dict(),
            hash_pairs=dict(type='list')
        )
    )

    action = module.params['action']
    username = module.params['user']
    password = module.params['password']
    if action in auth_required_actions and (username is None or
                                            password is None):
        module.fail_json(msg="Action %s requires authentication" % action)

    api_client = dlrnapi_client.ApiClient(host=module.params['host'])
    dlrnapi_client.configuration.username = username
    dlrnapi_client.configuration.password = password
    api_instance = dlrnapi_client.DefaultApi(api_client=api_client)

    options = DLRNAPIWrapper(module.params)
    options.check_options(action, module)

    try:
        output = command_funcs[action](api_instance, options)
        if type(output) == list:
            output_f = [x.to_dict() for x in output]
        else:
            output_f = output.to_dict()
        module.exit_json(changed=True, result=output_f)
    except ApiException as e:
        module.fail_json(msg="Exception when calling "
                             "%s: %s\n" % (command_funcs[action], e))


if __name__ == '__main__':
    main()
