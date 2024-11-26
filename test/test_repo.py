# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from dlrnapi_client.models.repo import Repo


class TestRepo(unittest.TestCase):
    """Repo unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRepo(self):
        """Test Repo """
        model = Repo()
        expected = {'job_id': None, 'success': None, 'timestamp': None,
                    'distro_hash': None, 'commit_hash': None,
                    'extended_hash': None, 'in_progress': None,
                    'user': None, 'component': None}
        self.assertEqual(model.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()