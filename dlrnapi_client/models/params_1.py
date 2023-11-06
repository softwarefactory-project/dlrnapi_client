from dlrnapi_client.models.base import BaseApiModel


class Params1(BaseApiModel):
    def __init__(self, max_age=None, reporting_job_id=None, success=None,
                 job_id=None, sequential_mode=None, previous_job_id=None,
                 component=None):
        """Params1 - a model defined to get the last tested repo and add an
        "in progress" entry in the CI job table

        :param int max_age: Maximum age in hours, used as base for the search
        :param str reporting_job_id: name of the CI that will test this repo
        :param bool success: find repos with a successful/unsuccessful vote
        :param str job_id: name of the CI that sent the vote
        :param bool sequential_mode: if set to true, change the search algorithm
                                     to only use previous_job_id as CI name to
                                     search for. Defaults to false
        :param str previous_job_id: CI name to search for, if sequential_mode is
                                    True
        :param str component: 'Only search for repos related to this component
        """
        self.var_types = {
            'max_age': 'int',
            'reporting_job_id': 'str',
            'success': 'bool',
            'job_id': 'str',
            'sequential_mode': 'bool',
            'previous_job_id': 'str',
            'component': 'str'
        }

        self._max_age = max_age
        self.reporting_job_id = reporting_job_id
        self.success = success
        self.job_id = job_id
        self.sequential_mode = sequential_mode
        self.previous_job_id = previous_job_id
        self.component = component

    @property
    def max_age(self):
        """Gets the max_age of this Params1.

        Maximum age (in hours) for the repo to be considered.
        Any repo tested or being tested after \"now - max_age\" will be taken
        into account. If set to 0, all repos will be considered.

        :return: The max_age of this Params1.
        :rtype: int
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        """Sets the max_age of this Params1.

        Maximum age (in hours) for the repo to be considered.
        Any repo tested or being tested after \"now - max_age\" will be taken
        into account. If set to 0, all repos will be considered.

        :param max_age: The max_age of this Params1.
        :type: int
        """
        if max_age is None:
            raise ValueError("Invalid value for `max_age`, must not be `None`")
        if max_age is not None and max_age < 0:
            raise ValueError("Invalid value for `max_age`, must be a value "
                             "greater than or equal to `0`")

        self._max_age = max_age
