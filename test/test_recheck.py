# coding: utf-8
from __future__ import absolute_import

import unittest

from dlrnapi_client.models.recheck_request import RecheckRequest
from dlrnapi_client.models.recheck_request import RecheckResponse


class TestRecheckRequest(unittest.TestCase):
    """RecheckRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRecheckRequest(self):
        """Test RecheckRequest """
        model = RecheckRequest()
        model.package_name = "Test"
        expected = {'package_name': "Test"}
        self.assertEqual(model.to_dict(), expected)

    def testRecheckRequestException(self):
        """Test RecheckRequest ValueError exception"""
        model = RecheckRequest()
        with self.assertRaises(ValueError) as exc:
            model.package_name = None
        self.assertEqual(str(exc.exception), "Invalid value for `package_name`,"
                                             " must not be `None`")


class TestRecheckResponse(unittest.TestCase):
    """RecheckResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRecheckResponse(self):
        """Test RecheckResponse """
        model = RecheckResponse()
        expected = {'result': None}
        self.assertEqual(model.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
