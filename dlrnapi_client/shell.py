# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import print_function
import argparse
import os
import sys

from pprint import pprint

import dlrnapi_client
from dlrnapi_client.rest import ApiException


def get_last_tested_repo(api_instance, options):
    params = dlrnapi_client.Params()  # Params | The JSON params to post
    params.max_age = options.max_age
    if options.success:
        params.success = str(options.success)
    params.job_id = options.job_id
    params.sequential_mode = str(options.sequential)
    params.previous_job_id = options.previous_job_id

    try:
        api_response = api_instance.api_last_tested_repo_get(params)
        return api_response
    except ApiException as e:
        raise e


def post_last_tested_repo(api_instance, options):
    params = dlrnapi_client.Params1()  # Params1 | The JSON params to post
    params.max_age = options.max_age
    params.reporting_job_id = options.reporting_job_id
    if options.success:
        params.success = str(options.success)
    params.job_id = options.job_id
    params.sequential_mode = str(options.sequential)
    params.previous_job_id = options.previous_job_id

    try:
        api_response = api_instance.api_last_tested_repo_post(params)
        return api_response
    except ApiException as e:
        raise e


def repo_status(api_instance, options):
    params = dlrnapi_client.Params2()  # Params2 | The JSON params to post
    params.commit_hash = options.commit_hash
    params.distro_hash = options.distro_hash
    if options.success:
        params.success = str(options.success)

    try:
        api_response = api_instance.api_repo_status_get(params)
        return api_response
    except ApiException as e:
        raise e


def repo_promote(api_instance, options):
    params = dlrnapi_client.Promotion()  # Promotion | The JSON params to post
    params.commit_hash = options.commit_hash
    params.distro_hash = options.distro_hash
    params.promote_name = options.promote_name
    try:
        api_response = api_instance.api_promote_post(params)
        return api_response
    except ApiException as e:
        raise e


def report_result(api_instance, options):
    params = dlrnapi_client.Params3()  # Params3 | The JSON params to post
    params.job_id = options.job_id
    params.commit_hash = options.commit_hash
    params.distro_hash = options.distro_hash
    params.success = str(options.success)
    params.url = options.info_url
    params.timestamp = options.timestamp
    params.notes = options.notes

    try:
        api_response = api_instance.api_report_result_post(params)
        return api_response
    except ApiException as e:
        raise e


def import_commit(api_instance, options):
    params = dlrnapi_client.ModelImport()  # ModelImport | JSON params to post
    params.repo_url = options.repo_url

    try:
        api_response = api_instance.api_remote_import_post(params)
        return api_response
    except ApiException as e:
        raise e


command_funcs = {
    'repo-get': get_last_tested_repo,
    'repo-use': post_last_tested_repo,
    'repo-status': repo_status,
    'report-result': report_result,
    'repo-promote': repo_promote,
    'commit-import': import_commit,
}


def main():
    parser = argparse.ArgumentParser(prog='dlrnapi')

    parser.add_argument('--url',
                        required=True,
                        help='URL to use')
    parser.add_argument('--username', '-u',
                        help='username for authentication, defaults to '
                             '"DLRNAPI_USERNAME" environment variable if set',
                        default=os.getenv('DLRNAPI_USERNAME', None)
                        )
    parser.add_argument('--password', '-p',
                        help='password for authentication, defaults to '
                             '"DLRNAPI_PASSWORD" environment variable is set',
                        default=os.getenv('DLRNAPI_PASSWORD', None)
                        )

    subparsers = parser.add_subparsers(dest='command',
                                       title='subcommands',
                                       description='available subcommands')
    # Subcommand get-repo
    parser_last = subparsers.add_parser('repo-get',
                                        help='Get last tested repo')
    parser_last.add_argument('--max-age', type=int, default=0,
                             help='max_age')
    parser_last.add_argument('--success', type=str, default=None,
                             help='Find repos with a successful/unsuccessful '
                                  'vote, if specified')
    parser_last.add_argument('--job-id', type=str, default=None,
                             help='Name of the CI that sent the vote. If not '
                                  'set, no filter will be set on CI')
    parser_last.add_argument('--sequential-mode', dest='sequential',
                             action='store_true',
                             help='Use the sequential mode algorithm. In this '
                                  'case, return the last tested repo within '
                                  'that timeframe for the CI job described by '
                                  '--previous-job-id')
    parser_last.set_defaults(sequential=False)

    parser_last.add_argument('--previous-job-id', type=str, default=None,
                             help='If --sequential-mode is set, look for jobs'
                                  ' tested by this CI')

    # Subcommand use-repo
    parser_use_last = subparsers.add_parser('repo-use',
                                            help='Get the last tested repo '
                                                 'since a specific time '
                                                 '(optionally for a CI job), '
                                                 'and add an "in progress" '
                                                 'entry in the CI job table '
                                                 'for this.')
    parser_use_last.add_argument('--max-age', type=int, default=0,
                                 help='max_age')
    parser_use_last.add_argument('--reporting-job-id', type=str, required=True,
                                 help=' Name of the CI that will add the "in '
                                      'progress" entry in the CI job table.')
    parser_use_last.add_argument('--success', type=str, default=None,
                                 help='Find repos with a successful/'
                                      'unsuccessful vote, if specified')
    parser_use_last.add_argument('--job-id', type=str, default=None,
                                 help='Name of the CI that sent the vote. If '
                                      'not set, no filter will be set on CI')
    parser_use_last.add_argument('--sequential-mode', dest='sequential',
                                 action='store_true',
                                 help='Use the sequential mode algorithm. In '
                                      'this case, return the last tested repo '
                                      'within that timeframe for the CI job '
                                      'described by --previous-job-id')
    parser_use_last.set_defaults(sequential=False)
    parser_use_last.add_argument('--previous-job-id', type=str, default=None,
                                 help='If --sequential-mode is true, look for '
                                      'jobs tested by this CI')

    # Subcommand repo-status
    parser_st = subparsers.add_parser('repo-status',
                                      help='Get all the CI reports for a '
                                           'specific repository.')
    parser_st.add_argument('--commit-hash', type=str, required=True,
                           help='commit_hash of the repo to fetch '
                                'information for.')
    parser_st.add_argument('--distro-hash', type=str, required=True,
                           help='distro_hash of the repo to fetch '
                                'information for.')
    parser_st.add_argument('--success', type=str, default=None,
                           help='If set to a value, only return the CI '
                                'reports with the specified vote. If not'
                                ' set, return all CI reports.')

    # Subcommand report-result
    parser_rep = subparsers.add_parser('report-result',
                                       help='Report the result of a CI job')
    parser_rep.add_argument('--job-id', type=str, required=True,
                            help='Name of the CI sending the vote')
    parser_rep.add_argument('--commit-hash', type=str, required=True,
                            help='commit_hash of tested repo')
    parser_rep.add_argument('--distro-hash', type=str, required=True,
                            help='distro_hash of tested repo')
    parser_rep.add_argument('--info-url', type=str, required=True,
                            help='URL where to find additional information '
                                 'from the CI execution')
    parser_rep.add_argument('--timestamp', type=str, required=True,
                            help='Timestamp (in seconds since the epoch)')
    parser_rep.add_argument('--success', type=str, required=True,
                            help='Was the CI execution successful?')
    parser_rep.add_argument('--notes', type=str,
                            help='Additional notes')

    # Subcommand promote
    parser_prom = subparsers.add_parser('repo-promote',
                                        help='Promote a repository')
    parser_prom.add_argument('--commit-hash', type=str, required=True,
                             help='commit_hash of the repo to be promoted')
    parser_prom.add_argument('--distro-hash', type=str, required=True,
                             help='distro_hash of the repo to be promoted')
    parser_prom.add_argument('--promote-name', type=str, required=True,
                             help='Name to be used for the promotion')

    # Subcommand commit-import
    parser_imp = subparsers.add_parser('commit-import',
                                       help='Import a commit built by another'
                                            ' instance')
    parser_imp.add_argument('--repo-url', type=str, required=True,
                            help='Base repository URL for the remote repo '
                                 'to import')

    options, args = parser.parse_known_args(sys.argv[1:])

    # create an instance of the API class
    api_client = dlrnapi_client.ApiClient(host=options.url)
    dlrnapi_client.configuration.username = options.username
    dlrnapi_client.configuration.password = options.password
    api_instance = dlrnapi_client.DefaultApi(api_client=api_client)

    try:
        api_response = command_funcs[options.command](api_instance, options)
        pprint(api_response)
    except Exception as e:
        raise e
