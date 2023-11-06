from dlrnapi_client.models.base import BaseApiModel


class CIVote(BaseApiModel):
    def __init__(self, job_id=None, commit_hash=None, distro_hash=None,
                 extended_hash=None, aggregate_hash=None, url=None,
                 timestamp=None, in_progress=None, success=None, notes=None,
                 component=None):
        """CIVote - a model defined to wrap the response vote from
        non-aggregate repositories

        :param str job_id: Name of the CI sending the vote
        :param str commit_hash: Hash of the source commit
        :param str distro_hash: Hash of the distro commit
        :param str extended_hash: Hash of the extended commit
        :param str aggregate_hash: Aggregate hash that was promoted
        :param str url: Url of the CI
        :param int timestamp: Vote's timestamp
        :param bool in_progress: True if CI still running
        :param bool success: True if CI success
        :param str notes: Additional notes, free-form
        :param str component: Component for the package
        """
        self.var_types = {
            'job_id': 'str',
            'commit_hash': 'str',
            'distro_hash': 'str',
            'extended_hash': 'str',
            'aggregate_hash': 'str',
            'url': 'str',
            'timestamp': 'int',
            'in_progress': 'bool',
            'success': 'bool',
            'notes': 'str',
            'component': 'str'
        }

        self.job_id = job_id
        self.commit_hash = commit_hash
        self.distro_hash = distro_hash
        self.extended_hash = extended_hash
        self.aggregate_hash = aggregate_hash
        self.url = url
        self.timestamp = timestamp
        self.in_progress = in_progress
        self.success = success
        self.notes = notes
        self.component = component
