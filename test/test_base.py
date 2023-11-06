# coding: utf-8
import unittest

from dlrnapi_client.models.base import BaseApiModel
from dlrnapi_client.models.metrics import Metrics


class BaseApiModelChild(BaseApiModel):
    """BaseApiModelTest used to test the inherited to_dict method """
    metrics_var = Metrics(succeeded=1, failed=2, total=3)
    var_types = {
        'str_var': 'str',
        'int_var': 'int',
        'bool_var': 'bool',
        'list_var': 'list',
        'dict_var': 'dict',
        'object_var': Metrics
    }
    str_var = "String_test"
    int_var = 10
    bool_var = False
    object_var = metrics_var
    list_var = [1, "2", metrics_var]
    dict_var = {
        'item_1': 'value_item_1',
        'item_2': 2,
        'item_3': metrics_var
        }


class TestBaseApiModel(unittest.TestCase):
    """BaseApiModel unit test stubs """

    def setUp(self):
        self.model = BaseApiModelChild()

    def testToDict(self):
        """Test to_dict method from BaseApiModel """
        expected = {'bool_var': False,
                    'dict_var': {'item_1': 'value_item_1',
                                 'item_2': 2,
                                 'item_3': {'failed': 2, 'succeeded': 1,
                                            'total': 3}},
                    'int_var': 10,
                    'list_var': [1, '2', {'failed': 2, 'succeeded': 1,
                                          'total': 3}],
                    'object_var': {'failed': 2, 'succeeded': 1, 'total': 3},
                    'str_var': 'String_test'}
        self.assertEqual(self.model.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
