from dlrnapi_client.models.base import BaseApiModel


class PromotionQuery(BaseApiModel):
    def __init__(self, commit_hash=None, distro_hash=None, extended_hash=None,
                 aggregate_hash=None, promote_name=None, offset=None,
                 limit=None, component=None):
        """PromotionQuery - a model defined to get information about promotions

        :param str commit_hash: Hash of the source commit
        :param str distro_hash: Hash of the distro commit
        :param str extended_hash: Hash of the extended commit
        :param str aggregate_hash: Aggregate hash that was promoted
        :param str promote_name: Filter results for this promotion name
        :param int offset: Show results after this offset
        :param int limit: Limit the results to the first limit items
        :param str component: Only search for promotions related to this
        component
        """
        self.var_types = {
            'commit_hash': 'str',
            'distro_hash': 'str',
            'extended_hash': 'str',
            'aggregate_hash': 'str',
            'promote_name': 'str',
            'offset': 'int',
            'limit': 'int',
            'component': 'str',
        }

        self.commit_hash = commit_hash
        self.distro_hash = distro_hash
        self.extended_hash = extended_hash
        self.aggregate_hash = aggregate_hash
        self.promote_name = promote_name
        self.offset = offset
        self.limit = limit
        self.component = component
