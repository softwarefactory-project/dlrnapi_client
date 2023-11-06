from dlrnapi_client.models.base import BaseApiModel


class Repo(BaseApiModel):
    def __init__(self, commit_hash=None, distro_hash=None, extended_hash=None,
                 success=None, job_id=None, in_progress=None, timestamp=None,
                 user=None, component=None):
        """Repo - a model defined to wrap the returned repo by DLRN

        :param str commit_hash: commit_hash of the repo to be promoted
        :param str distro_hash: distro_hash of the repo to be promoted
        :param str extended_hash: extended_hash of the repo to be promoted
        :param bool success: find repos with a successful/unsuccessful vote
        :param str job_id: name of the CI that sent the vote
        :param bool in_progress: True if the CI job is still running
        :param int timestamp: Timestamp of the vote
        :param str user: User sending the vote
        :param str component: Component for the commit
        """
        self.var_types = {
            'commit_hash': 'str',
            'distro_hash': 'str',
            'extended_hash': 'str',
            'success': 'bool',
            'job_id': 'str',
            'in_progress': 'bool',
            'timestamp': 'int',
            'user': 'str',
            'component': 'str'
        }

        self.commit_hash = commit_hash
        self.distro_hash = distro_hash
        self.extended_hash = extended_hash
        self.success = success
        self.job_id = job_id
        self.in_progress = in_progress
        self.timestamp = timestamp
        self.user = user
        self.component = component
