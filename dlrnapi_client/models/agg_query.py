from dlrnapi_client.models.base import BaseApiModel


class AggQuery(BaseApiModel):
    def __init__(self, aggregate_hash=None, success=None):
        """Aggquery - a model defined to request data from
        aggregate repositories

        :param str aggregate_hash: Hash of the aggregated repo to fetch
        information for
        """
        self.var_types = {
            'aggregate_hash': 'str',
            'success': 'bool'
        }

        self.aggregate_hash = aggregate_hash
        self.success = success
