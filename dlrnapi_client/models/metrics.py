from dlrnapi_client.models.base import BaseApiModel


class MetricsRequest(BaseApiModel):
    def __init__(self, start_date=None, end_date=None, package_name=None):
        """MetricsRequest - a model defined to request data related with
        successful and/or fail builds

        :param str start_date: Start date for period
        :param str end_date: End date for period
        :param str package_name (optional): Return metrics for package_name
        """

        self.var_types = {
            'start_date': 'str',
            'end_date': 'str',
            'package_name': 'str',
        }

        self.start_date = start_date
        self.end_date = end_date
        self.package_name = package_name


class Metrics(BaseApiModel):
    def __init__(self, succeeded=None, failed=None, total=None):
        """Metrics - a model defined to wrap successful and/or fail builds from
        metrics DLRN endpoint

        :param str succeeded: Successful commits
        :param str failed: Failed commits
        :param str total (optional): Total of commits
        """
        self.var_types = {
            'succeeded': 'int',
            'failed': 'int',
            'total': 'int',
        }

        self.succeeded = succeeded
        self.failed = failed
        self.total = total
