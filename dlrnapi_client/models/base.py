from six import iteritems


class BaseApiModel(object):
    """BaseApiModel - a model defined to be inherited from other API Models

        It inherits explicitly from 'object' in order to make setters
        and getters work in python2 from inherited interfaces.
    """
    def to_dict(self):
        """Returns the model properties as a dict """
        result = {}

        for attr, _ in iteritems(self.var_types):
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
