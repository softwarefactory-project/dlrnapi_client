# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from dlrnapi_client.models.promotion_query import PromotionQuery


class TestPromotionQuery(unittest.TestCase):
    """Promotion unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPromotionQuery(self):
        """Test PromotionQuery """
        model = PromotionQuery()
        expected = {'promote_name': None, 'commit_hash': None,
                    'distro_hash': None, 'offset': None}
        self.assertEqual(model.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
