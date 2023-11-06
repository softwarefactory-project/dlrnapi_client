from dlrnapi_client.models.base import BaseApiModel


class Params3(BaseApiModel):
    def __init__(self, job_id=None, commit_hash=None, distro_hash=None,
                 extended_hash=None, aggregate_hash=None, url=None,
                 timestamp=None, success=None, notes=None):
        """Params3 - a model defined to report the result of a CI job

        :param str job_id: Name of the CI sending the vote
        :param str commit_hash: Hash of the source commit
        :param str distro_hash: Hash of the distro commit
        :param str extended_hash: Hash of the extended commit
        :param str aggregate_hash: Aggregate hash that was promoted
        :param str url: Url of the CI
        :param int timestamp: Timestamp (in seconds since the epoch)
        :param bool success: True if CI success
        :param str notes: Additional notes, free-form
        """
        self.var_types = {
            'job_id': 'str',
            'commit_hash': 'str',
            'distro_hash': 'str',
            'extended_hash': 'str',
            'aggregate_hash': 'str',
            'url': 'str',
            'timestamp': 'int',
            'success': 'bool',
            'notes': 'str'
        }

        self._job_id = job_id
        self._success = success
        self.commit_hash = commit_hash
        self.distro_hash = distro_hash
        self.extended_hash = extended_hash
        self.aggregate_hash = aggregate_hash
        self.url = url
        self.timestamp = timestamp
        self.notes = notes

    @property
    def job_id(self):
        """Gets the job_id of this Params3.

        Name of the CI sending the vote.

        :return: The job_id of this Params3.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Params3.

        Name of the CI sending the vote.

        :param job_id: The job_id of this Params3.
        :type: str
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")

        self._job_id = job_id

    @property
    def success(self):
        """Gets the success of this Params3.

        Was the CI execution successful?

        :return: The success of this Params3.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this Params3.

        Was the CI execution successful?

        :param success: The success of this Params3.
        :type: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")

        self._success = success
