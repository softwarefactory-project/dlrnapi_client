from dlrnapi_client.models.base import BaseApiModel


class Params2(BaseApiModel):
    def __init__(self, commit_hash=None, distro_hash=None, extended_hash=None,
                 success=None):
        """Params2 - a model defined to get all the CI reports
        for a specific repository

        :param str commit_hash: Hash of the source commit
        :param str distro_hash: Hash of the distro commit
        :param str extended_hash: Hash of the extended commit
        :param bool success: find repos with a successful/unsuccessful vote
        """
        self.var_types = {
            'commit_hash': 'str',
            'distro_hash': 'str',
            'extended_hash': 'str',
            'success': 'bool'
        }

        self._commit_hash = commit_hash
        self._distro_hash = distro_hash
        self.extended_hash = extended_hash
        self.success = success

    @property
    def commit_hash(self):
        """Gets the commit_hash of this Params2.

        commit_hash of the repo to fetch information for.

        :return: The commit_hash of this Params2.
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """Sets the commit_hash of this Params2.

        commit_hash of the repo to fetch information for.

        :param commit_hash: The commit_hash of this Params2.
        :type: str
        """
        if commit_hash is None:
            raise ValueError("Invalid value for `commit_hash`, must not be"
                             " `None`")

        self._commit_hash = commit_hash

    @property
    def distro_hash(self):
        """Gets the distro_hash of this Params2.

        distro_hash of the repo to fetch information for.

        :return: The distro_hash of this Params2.
        :rtype: str
        """
        return self._distro_hash

    @distro_hash.setter
    def distro_hash(self, distro_hash):
        """Sets the distro_hash of this Params2.

        distro_hash of the repo to fetch information for.

        :param distro_hash: The distro_hash of this Params2.
        :type: str
        """
        if distro_hash is None:
            raise ValueError("Invalid value for `distro_hash`, must not be"
                             " `None`")

        self._distro_hash = distro_hash
