# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dlrnapi_client
from dlrnapi_client.apis.default_api import DefaultApi


class MockApiClient(object):
    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_type=None, auth_settings=None, callback=None,
                 _return_http_data_only=None, collection_formats=None,
                 _preload_content=True,
                 _request_timeout=None):
        return resource_path, method

    def select_header_accept(self, accepts):
        return 'application/json'

    def select_header_content_type(self, content_types):
        return 'application/json'


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs """

    def setUp(self):
        self.api = DefaultApi()
        self.api_client = MockApiClient()

    def tearDown(self):
        pass

    def test_api_last_tested_repo_get(self):
        """Test case for api_last_tested_repo_get """
        default_api = DefaultApi(api_client=self.api_client)
        params = dlrnapi_client.Params()
        path, method = default_api.api_last_tested_repo_get(params)
        self.assertEqual(path, '/api/last_tested_repo')
        self.assertEqual(method, 'GET')

    def test_api_last_tested_repo_post(self):
        """Test case for api_last_tested_repo_post """
        default_api = DefaultApi(api_client=self.api_client)
        params = dlrnapi_client.Params1()
        path, method = default_api.api_last_tested_repo_post(params)
        self.assertEqual(path, '/api/last_tested_repo')
        self.assertEqual(method, 'POST')

    def test_api_promote_post(self):
        """Test case for api_promote_post """
        default_api = DefaultApi(api_client=self.api_client)
        params = dlrnapi_client.Promotion()
        path, method = default_api.api_promote_post(params)
        self.assertEqual(path, '/api/promote')
        self.assertEqual(method, 'POST')

    def test_api_promotions_get(self):
        """Test case for api_promotions_get """
        default_api = DefaultApi(api_client=self.api_client)
        params = dlrnapi_client.Promotion()
        path, method = default_api.api_promotions_get(params)
        self.assertEqual(path, '/api/promotions')
        self.assertEqual(method, 'GET')

    def test_api_remote_import_post(self):
        """Test case for api_remote_import_post """
        default_api = DefaultApi(api_client=self.api_client)
        params = dlrnapi_client.ModelImport()
        path, method = default_api.api_remote_import_post(params)
        self.assertEqual(path, '/api/remote/import')
        self.assertEqual(method, 'POST')

    def test_api_repo_status_get(self):
        """Test case for api_repo_status_get """
        default_api = DefaultApi(api_client=self.api_client)
        params = dlrnapi_client.Params2()
        path, method = default_api.api_repo_status_get(params)
        self.assertEqual(path, '/api/repo_status')
        self.assertEqual(method, 'GET')

    def test_api_report_result_post(self):
        """Test case for api_report_result_post """
        default_api = DefaultApi(api_client=self.api_client)
        params = dlrnapi_client.Params3()
        path, method = default_api.api_report_result_post(params)
        self.assertEqual(path, '/api/report_result')
        self.assertEqual(method, 'POST')


if __name__ == '__main__':
    unittest.main()
