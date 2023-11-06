from dlrnapi_client.models.base import BaseApiModel


class ModelImport(BaseApiModel):
    def __init__(self, repo_url=None):
        """ModelImport - a model defined to import a commit built from
        a different DLRN instance to the target instance

        :param str repo_url: Repository URL to import from

        """
        self.var_types = {
            'repo_url': 'str'
        }

        self.repo_url = repo_url
