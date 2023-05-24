# Usage

## Parameters

```bash
usage: dlrnapi [-h] --url URL [--auth-method AUTH_METHOD] [--username USERNAME] [--password PASSWORD] [--server-principal SERVER_PRINCIPAL]
               {repo-get,repo-use,repo-status,agg-status,report-result,repo-promote,repo-promote-batch,promotion-get,commit-import,build-metrics}

optional arguments:
  -h, --help            show this help message and exit
  --url URL             URL to use
  --auth-method AUTH_METHOD
                        auth-method to be used, defaults to "DLRNAPI_AUTHMETHOD" environment variable if set
                        basicAuth otherwise
  --username USERNAME, -u USERNAME
                        username for basicAuth, defaults to "DLRNAPI_USERNAME" environment variable if set
  --password PASSWORD, -p PASSWORD
                        password for basicAuth, defaults to "DLRNAPI_PASSWORD" environment variable if set
  --server-principal SERVER_PRINCIPAL, -s SERVER_PRINCIPAL
                        server_principal for kerberosAuth, defaults to "DLRNAPI_PRINCIPAL" environment
                        variable if set. Mandatory if kerberosAuth method selected.
  --force-auth          force to use authentication in GET methods. Those methods by default are not protected.
                        Useful in DLRN deployments with GET endpoints protected.

subcommands:
  available subcommands

  {repo-get,repo-use,repo-status,agg-status,report-result,repo-promote,repo-promote-batch,promotion-get,commit-import,build-metrics}
    repo-get            Get last tested repo
    repo-use            Get the last tested repo since a specific time (optionally for a CI job), and add an "in progress" entry in the CI job table for this.
    repo-status         Get all the CI reports for a specific repository.
    agg-status          Get all the CI reports for a specific aggregated repository.
    report-result       Report the result of a CI job
    repo-promote        Promote a repository
    repo-promote-batch  Promote multiple repositories at the same time, as an atomic operation.
    promotion-get       Get information about promotions
    commit-import       Import a commit built by another instance
    build-metrics       Fetch build metrics in a time period

```
The **url** parameter is mandatory in all cases. **username** and **password**
are required for the _repo-use_, _report-result_, _repo-promote_,
_repo-promote-batch_ and _commit-import_ subcommands.

For detailed usage information on each subcommand, run:

```bash
$ dlrnapi <subcommand> -h
```
