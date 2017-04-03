# Usage

## Parameters

```bash
usage: dlrnapi [-h] --url URL [--username USERNAME] [--password PASSWORD]
               {repo-get,repo-use,repo-status,report-result,repo-promote,commit-import}
               ...

optional arguments:
  -h, --help            show this help message and exit
  --url URL             URL to use
  --username USERNAME, -u USERNAME
                        username for authentication
  --password PASSWORD, -p PASSWORD
                        password for authentication

subcommands:
  available subcommands

  {repo-get,repo-use,repo-status,report-result,repo-promote,commit-import}
    repo-get            Get last tested repo
    repo-use            Get the last tested repo since a specific time
                        (optionally for a CI job), and add an "in progress"
                        entry in the CI job table for this.
    repo-status         Get all the CI reports for a specific repository.
    report-result       Report the result of a CI job
    repo-promote        Promote a repository
    commit-import       Import a commit built by another instance
```
The **url** parameter is mandatory in all cases. **username** and **password**
are required for the _repo-use_, _report-result_, _repo-promote_ and
_commit-import_ subcommands.

For detailed usage information on each subcommand, run:

```bash
$ dlrnapi <subcommand> -h
```
