from dlrnapi_client.models.base import BaseApiModel


class RecheckRequest(BaseApiModel):
    def __init__(self, package_name=None):
        """RecheckRequest - a model defines params for recheck-request action

        :param str package_name: Package to recheck
        """
        self.var_types = {
            'package_name': 'str',
        }

        self._package_name = package_name

    @property
    def package_name(self):
        """Gets the package_name of this RecheckRequest.

        package_name to recheck.

        :return: The package_name of this RecheckRequest.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this RecheckRequest.

        package_name to recheck.

        :param package_name: The package_name of this RecheckRequest.
        :type: str
        """
        if package_name is None:
            raise ValueError("Invalid value for `package_name`, must not be"
                             " `None`")

        self._package_name = package_name


class Recheck(BaseApiModel):
    def __init__(self, result=None):
        """Recheck - a model defines params for recheck-request action response

        :param str result: Result of the command
        """
        self.var_types = {
            'result': 'str',
        }

        self.result = result
