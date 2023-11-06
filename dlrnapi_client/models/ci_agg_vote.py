from dlrnapi_client.models.base import BaseApiModel


class CIAggVote(BaseApiModel):
    def __init__(self, job_id=None, commit_hash=None, distro_hash=None,
                 aggregate_hash=None, url=None, timestamp=None,
                 in_progress=None, success=None, notes=None, component=None):
        """CIAggVote - a model defined to wrap the response vote from
        aggregate repositories

        :param str job_id: Name of the CI sending the vote
        :param str aggregate_hash: Hash of the aggregated repo
        :param str url: Url of the CI
        :param int timestamp: Vote's timestamp
        :param bool in_progress: True if CI still running
        :param bool success: True if CI success
        :param str notes: Additional notes, free-form

        """
        self.var_types = {
            'job_id': 'str',
            'aggregate_hash': 'str',
            'url': 'str',
            'timestamp': 'int',
            'in_progress': 'bool',
            'success': 'bool',
            'notes': 'str',
        }

        self.job_id = job_id
        self.aggregate_hash = aggregate_hash
        self.url = url
        self.timestamp = timestamp
        self.in_progress = in_progress
        self.success = success
        self.notes = notes
