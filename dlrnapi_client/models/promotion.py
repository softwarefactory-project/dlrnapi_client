from dlrnapi_client.models.base import BaseApiModel


class Promotion(BaseApiModel):
    def __init__(self, commit_hash=None, distro_hash=None, extended_hash=None,
                 aggregate_hash=None, promote_name=None, timestamp=None,
                 user=None, repo_hash=None, repo_url=None, component=None):
        """Promotion - a model defined to promote one or multiple repositories.

        :param str commit_hash: commit_hash of the repo to be promoted
        :param str distro_hash: distro_hash of the repo to be promoted
        :param str extended_hash: extended_hash of the repo to be promoted
        :param str aggregate_hash: Aggregate hash that was promoted
        :param str promote_name: Name to be used for the promotion
        :param int timestamp: Promotion timestamp
        :param str user: Current user
        :param str repo_hash: 'commit_hash+distro_hash or '
                              'commit_hash+distro_hash+extended_hash of '
                              'the repos to be promoted
        :param str repo_url: Base url and hash dir created by DLRN
        :param str component: Component for the commit
        """
        self.var_types = {
            'commit_hash': 'str',
            'distro_hash': 'str',
            'extended_hash': 'str',
            'aggregate_hash': 'str',
            'promote_name': 'str',
            'timestamp': 'int',
            'user': 'str',
            'repo_hash': 'str',
            'repo_url': 'str',
            'component': 'str',
        }

        self.commit_hash = commit_hash
        self.distro_hash = distro_hash
        self.extended_hash = extended_hash
        self.aggregate_hash = aggregate_hash
        self.promote_name = promote_name
        self.timestamp = timestamp
        self.user = user
        self.repo_hash = repo_hash
        self.repo_url = repo_url
        self.component = component
