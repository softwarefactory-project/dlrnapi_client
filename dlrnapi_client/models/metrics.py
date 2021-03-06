# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems


class MetricsRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, start_date=None, end_date=None, package_name=None):
        """MetricsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'str',
            'end_date': 'str',
            'package_name': 'str',
        }

        self.attribute_map = {
            'start_date': 'start_date',
            'end_date': 'end_date',
            'package_name': 'package_name',
        }

        self._start_date = start_date
        self._end_date = end_date
        self._package_name = package_name

    @property
    def start_date(self):
        """Gets the start_date of this Metrics Request.

        start_date of the period to consider, in YYYY-MM-DD format.

        :return: The start_date of this Metrics Request.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the commit_hash of this Promotion Query.

        start_date of the period to consider, in YYYY-MM-DD format.

        :param start_date: The start_date of this Metrics Request.
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Metrics Request.

        end_date of the period to consider, in YYYY-MM-DD format.

        :return: The end_date of this Metrics Request.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the commit_hash of this Promotion Query.

        end_date of the period to consider, in YYYY-MM-DD format.

        :param end_date: The end_date of this Metrics Request.
        :type: str
        """

        self._end_date = end_date

    @property
    def package_name(self):
        """Gets the package_name of this Metrics Request.

        package_name to filter the query.

        :return: package_name to filter the query.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the commit_hash of this Promotion Query.

        package_name to filter the query.

        :param package_name: package_name to filter the query.
        :type: str
        """

        self._package_name = package_name

    def to_dict(self):
        """Returns the model properties as a dict """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model """
        return pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint` """
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal """
        if not isinstance(other, MetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal """
        return not self == other


class Metrics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, succeeded=None, failed=None, total=None):
        """Metrics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'succeeded': 'int',
            'failed': 'int',
            'total': 'int',
        }

        self.attribute_map = {
            'succeeded': 'succeeded',
            'failed': 'failed',
            'total': 'total',
        }

        self._succeeded = succeeded
        self._failed = failed
        self._total = total

    @property
    def succeeded(self):
        """Gets the succeeded of this Metrics.

        Number of commits built successfully.

        :return: The number of commits built successfully.
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this Metrics.

        Number of commits built successfully.

        :param succeeded: The number of commits built successfully.
        :type: int
        """

        self._succeeded = succeeded

    @property
    def failed(self):
        """Gets the failed of this Metrics.

        Number of commits that failed to build.

        :return: The number of commits that failed to build.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this Metrics.

        Number of commits that failed to build.

        :param failed: The number of commits that failed to build.
        :type: int
        """

        self._failed = failed

    @property
    def total(self):
        """Gets the total of this Metrics.

        Number of commits processed in the period.

        :return: The total number of commits processed in the period.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Metrics.

        Number of commits processed in the period.

        :param total: The total number of commits processed in the period.
        :type: int
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model """
        return pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint` """
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal """
        if not isinstance(other, Metrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal """
        return not self == other
