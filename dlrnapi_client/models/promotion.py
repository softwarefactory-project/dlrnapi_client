# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems


class Promotion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, commit_hash=None, distro_hash=None, promote_name=None,
                 timestamp=None):
        """Promotion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'commit_hash': 'str',
            'distro_hash': 'str',
            'promote_name': 'str',
            'timestamp': 'int'
        }

        self.attribute_map = {
            'commit_hash': 'commit_hash',
            'distro_hash': 'distro_hash',
            'promote_name': 'promote_name',
            'timestamp': 'timestamp'
        }

        self._commit_hash = commit_hash
        self._distro_hash = distro_hash
        self._promote_name = promote_name
        self._timestamp = timestamp

    @property
    def commit_hash(self):
        """Gets the commit_hash of this Promotion.

        commit_hash of promoted repo

        :return: The commit_hash of this Promotion.
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """Sets the commit_hash of this Promotion.

        commit_hash of promoted repo

        :param commit_hash: The commit_hash of this Promotion.
        :type: str
        """

        self._commit_hash = commit_hash

    @property
    def distro_hash(self):
        """Gets the distro_hash of this Promotion.

        distro_hash of promoted repo

        :return: The distro_hash of this Promotion.
        :rtype: str
        """
        return self._distro_hash

    @distro_hash.setter
    def distro_hash(self, distro_hash):
        """Sets the distro_hash of this Promotion.

        distro_hash of promoted repo

        :param distro_hash: The distro_hash of this Promotion.
        :type: str
        """

        self._distro_hash = distro_hash

    @property
    def promote_name(self):
        """Gets the promote_name of this Promotion.

        name used for the promotion

        :return: The promote_name of this Promotion.
        :rtype: str
        """
        return self._promote_name

    @promote_name.setter
    def promote_name(self, promote_name):
        """Sets the promote_name of this Promotion.

        name used for the promotion

        :param promote_name: The promote_name of this Promotion.
        :type: str
        """

        self._promote_name = promote_name

    @property
    def timestamp(self):
        """Gets the timestamp of this Repo.

        Timestamp for this CI Vote (taken from the DLRN system time)

        :return: The timestamp of this Repo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Repo.

        Timestamp for this CI Vote (taken from the DLRN system time)

        :param timestamp: The timestamp of this Repo.
        :type: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, Promotion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal """
        return not self == other
