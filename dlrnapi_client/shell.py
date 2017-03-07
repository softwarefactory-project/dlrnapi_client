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
import sys

from pprint import pprint

import dlrnapi_client
from dlrnapi_client.rest import ApiException


def get_last_tested_repo(api_instance, options):
    params = dlrnapi_client.Params()  # Params | The JSON params to post
    params.max_age = options.max_age

    try:
        api_response = api_instance.api_last_tested_repo_get(params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->api_last_tested_repo_get:"
              " %s\n" % e)

command_funcs = {
    'get_last_tested_repo': get_last_tested_repo
}


def main():
    parser = argparse.ArgumentParser(prog='dlrnapi')

    parser.add_argument('--url',
                        required=True,
                        help='URL to use')
    subparsers = parser.add_subparsers(dest='command')
    # Subcommand last_tested_repo
    parser_last = subparsers.add_parser('get_last_tested_repo',
                                        help='Get last tested repo')
    parser_last.add_argument('--max_age', type=int, default=0,
                             help='max_age')

    options, args = parser.parse_known_args(sys.argv[1:])
    # create an instance of the API class
    api_client = dlrnapi_client.ApiClient(host=options.url)
    api_instance = dlrnapi_client.DefaultApi(api_client=api_client)

    command_funcs[options.command](api_instance, options)
