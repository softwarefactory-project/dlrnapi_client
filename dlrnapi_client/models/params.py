from dlrnapi_client.models.base import BaseApiModel


class Params(BaseApiModel):
    def __init__(self, max_age=None, success=None, job_id=None,
                 sequential_mode=None, previous_job_id=None, component=None):
        """Params - a model defined to request the last tested repo

        :param int max_age: Maximum age in hours, used as base for the search
        :param bool success: find repos with a successful/unsuccessful vote
        :param str job_id: name of the CI that sent the vote
        :param bool sequential_mode: if set to true, change the search algorithm
                                     to only use previous_job_id as CI name to
                                     search for. Defaults to false
        :param str previous_job_id: CI name to search for, if sequential_mode is
                                    True
        :param str component: Only search for repos related to this component
        """
        self.var_types = {
            'max_age': 'int',
            'success': 'bool',
            'job_id': 'str',
            'sequential_mode': 'bool',
            'previous_job_id': 'str',
            'component': 'str'
        }
        self._max_age = max_age
        self.success = success
        self.job_id = job_id
        self.sequential_mode = sequential_mode
        self.previous_job_id = previous_job_id
        self.component = component

    @property
    def max_age(self):
        """Gets the max_age of this Params.

        Maximum age (in hours) for the repo to be considered.
        Any repo tested or being tested after \"now - max_age\" will be taken
        into account. If set to 0, all repos will be considered.

        :return: The max_age of this Params.
        :rtype: int
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        """Sets the max_age of this Params.

        Maximum age (in hours) for the repo to be considered.
        Any repo tested or being tested after \"now - max_age\" will be taken
        into account. If set to 0, all repos will be considered.

        :param max_age: The max_age of this Params.
        :type: int
        """
        if max_age is None:
            raise ValueError("Invalid value for `max_age`, must not be `None`")
        if max_age is not None and max_age < 0:
            raise ValueError("Invalid value for `max_age`, must be a value"
                             " greater than or equal to `0`")

        self._max_age = max_age
