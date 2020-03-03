# dlrnapi_client.DefaultApi

All URIs are relative to <http://127.0.0.1:5000>

Method |HTTP request |Description
------------- | ------------- | -------------
[**api_last_tested_repo_get**](DefaultApi.md#api_last_tested_repo_get) |**GET** /api/last_tested_repo |
[**api_last_tested_repo_post**](DefaultApi.md#api_last_tested_repo_post)|**POST** /api/last_tested_repo |
[**api_promote_post**](DefaultApi.md#api_promote_post) | **POST** /api/promote |
[**api_promote_batch_post**](DefaultApi.md#api_promote_batch_post) | **POST** /api/promote-batch |
[**api_promotions_get**](DefaultApi.md#api_promotions_get) | **GET** /api/promotions |
[**api_build_metrics_get**](DefaultApi.md#api_build_metrics_get)|**GET** /api/metrics/builds|
[**api_remote_import_post**](DefaultApi.md#api_remote_import_post) |**POST** /api/remote/import |
[**api_repo_status_get**](DefaultApi.md#api_repo_status_get)|**GET** /api/repo_status |
[**api_agg_status_get**](DefaultApi.md#api_agg_status_get)|**GET** /api/agg_status |
[**api_report_result_post**](DefaultApi.md#api_report_result_post)|**POST** /api/report_result|


# **api_last_tested_repo_get**
> Repo api_last_tested_repo_get(params)

Get the last tested repo since a specific time.  If a ``job_id`` is specified, the order of precedence for the repo returned is:

-   The last tested repo within that timeframe for that CI job.
-   The last tested repo within that timeframe for any CI job, so we can have
    several CIs converge on a single repo.
-   The last \"consistent\" repo, if no repo has been tested in the timeframe.  

If ``sequential_mode`` is set to true, a different algorithm is used. Another parameter ``previous_job_id`` needs to be specified, and the order of precedence
for the repo returned is:

-   The last tested repo within that timeframe for the CI job described by
    ``previous_job_id``.
-   If no repo for ``previous_job_id`` is found, an error will be returned  

The sequential mode is meant to be used by CI pipelines, where a CI (n) job
needs to use the same repo tested by CI (n-1).

### Example
```python
from __future__ import print_statement
import time
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dlrnapi_client.DefaultApi()
params = dlrnapi_client.Params() # Params | The JSON params to post

try:
    api_response = api_instance.api_last_tested_repo_get(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_last_tested_repo_get: %s\n" % e)
```

### Parameters

Name |Type |Description  |Notes
------------- | ------------- | ------------- | -------------
**params**|[**Params**](Params.md)|The JSON params to post|

### Return type

[**Repo**](Repo.md)

### Authorization

No authorization required

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_last_tested_repo_post**
> Repo api_last_tested_repo_post(params)

Get the last tested repo since a specific time (optionally for a CI job), and add an \"in progress\" entry in the CI job table for this.  If a job_id is specified, the order of precedence for the repo returned is:

-   The last tested repo within that timeframe for that CI job.
-   The last tested repo within that timeframe for any CI job, so we can have  
    several CIs converge on a single repo.
-   The last \"consistent\" repo, if no repo has been tested in the timeframe.

If ``sequential_mode`` is set to true, a different algorithm is used. Another parameter ``previous_job_id`` needs to be specified, and the order of precedence
for the repo returned is:

-   The last tested repo within that timeframe for the CI job described by  
    ``previous_job_id``.
-   If no repo for ``previous_job_id`` is found, an error will be returned.

The sequential mode is meant to be used by CI pipelines, where a CI (n) job needs to use the same repo tested by CI (n-1).

### Example
```python
from __future__ import print_statement
import time
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
dlrnapi_client.configuration.username = 'YOUR_USERNAME'
dlrnapi_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = dlrnapi_client.DefaultApi()
params = dlrnapi_client.Params1() # Params1 | The JSON params to post

try:
    api_response = api_instance.api_last_tested_repo_post(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_last_tested_repo_post: %s\n" % e)
```

### Parameters

Name |Type |Description  |Notes
------------- | ------------- | ------------- | -------------
**params**|[**Params1**](Params1.md)|The JSON params to post|

### Return type

[**Repo**](Repo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_promote_post**
> Promotion api_promote_post(params=params)

Promote a repository. This can be implemented as a local symlink creation in the
DLRN worker, or any other form in the future.  Note the API will refuse to
promote using promote_name=\"consistent\" or \"current\", since those are
reserved keywords for DLRN.

### Example
```python
from __future__ import print_statement
import time
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
dlrnapi_client.configuration.username = 'YOUR_USERNAME'
dlrnapi_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = dlrnapi_client.DefaultApi()
params = dlrnapi_client.Promotion()  # Promotion | The JSON params to post

try:
    api_response = api_instance.api_promote_post(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_promote_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**params**|[**Promotion**](Promotion.md)|The JSON params to post|\[optional\]

### Return type

[**Promotion**](Promotion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_promote_batch_post**
> Promotion api_promote_batch_post(params=params)

Promote several repositories as an atomic operation. Note the API will refuse
to promote using promote_name=\"consistent\" or \"current\", since those are
reserved keywords for DLRN.

### Example
```python
from __future__ import print_statement
import time
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
dlrnapi_client.configuration.username = 'YOUR_USERNAME'
dlrnapi_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = dlrnapi_client.DefaultApi()

params = list()
hash_pairs = options.hash_pairs.split(',')
for pair in hash_pairs:
    commit_hash = pair.split('_')[0]
    distro_hash = pair.split('_')[1]
    param = dlrnapi_client.Promotion()
    param.commit_hash = commit_hash
    param.distro_hash = distro_hash
    param.promote_name = options.promote_name
    params.append(param)
try:
    api_response = api_instance.api_promote_batch_post(params)
    pprint(api_response)
except ApiException as e:
    raise e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**params**|[list(**Promotion**)](Promotion.md)|The JSON params to post|\[optional\]

### Return type

[**Promotion**](Promotion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_promotions_get**
> list[Promotion] api_promotions_get(params)



Get all the promotions, optionally for a specific repository or promotion name. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
params = swagger_client.Params5() # Params5 | The JSON params to post

try: 
    api_response = api_instance.api_promotions_get(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_promotions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**Params5**](Params5.md)| The JSON params to post | 

### Return type

[**list[Promotion]**](Promotion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **api_build_metrics_get**
> Metrics api_build_metrics_get(params)


Get the build metrics for a time period, optionally for a specific package name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
params = swagger_client.MetricRequest() # MetricRequest | The JSON params to post

try:
    api_response = api_instance.api_build_metrics_get(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_build_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**MetricRequest**](MetricRequest.md)| The JSON params to post |

### Return type

[**Metrics**](Metrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **api_remote_import_post**
> ModelImport api_remote_import_post(params=params)

Import a commit built by another instance. This API call mimics the behavior of the ``dlrn-remote`` command, with the only exception of not being able to specify a custom rdoinfo location.       

### Example
```python
from __future__ import print_statement
import time
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
dlrnapi_client.configuration.username = 'YOUR_USERNAME'
dlrnapi_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = dlrnapi_client.DefaultApi()
params = dlrnapi_client.ModelImport() # ModelImport | The JSON params to post (optional)

try:
    api_response = api_instance.api_remote_import_post(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_remote_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**params**|[**ModelImport**](ModelImport.md)|The JSON params to post|\[optional\]

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_repo_status_get**
> list\[CIVote\] api_repo_status_get(params=params)

Get all the CI reports for a specific repository.

### Example
```python
from __future__ import print_statement
import time
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dlrnapi_client.DefaultApi()
params = dlrnapi_client.Params2() # Params2 | The JSON params to post (optional)

try:
    api_response = api_instance.api_repo_status_get(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_repo_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**params**|[**Params2**](Params2.md)|The JSON params to post|\[optional\]

### Return type

[**list[CIVote]**](CIVote.md)

### Authorization

No authorization required

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_agg_status_get**
> list\[CIAggVote\] api_agg_status_get(params=params)

Get all the CI reports for a specific repo aggregate.

### Example
```python
from __future__ import print_statement
import time
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dlrnapi_client.DefaultApi()
params = dlrnapi_client.AggQuery()  # AggQuery | The JSON params to post

try:
    api_response = api_instance.api_agg_status_get(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_agg_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**params**|[**AggQuery**](AggQuery.md)|The JSON params to post|\[optional\]

### Return type

[**list[CIAggVote]**](CIAggVote.md)

### Authorization

No authorization required

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_report_result_post**
> CIVote api_report_result_post(params=params)

Report the result of a CI job.

### Example
```python
from __future__ import print_statement
import time
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
dlrnapi_client.configuration.username = 'YOUR_USERNAME'
dlrnapi_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = dlrnapi_client.DefaultApi()
params = dlrnapi_client.Params3() # Params3 | The JSON params to post (optional)

try:
    api_response = api_instance.api_report_result_post(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_report_result_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**params**|[**Params3**](Params3.md)|The JSON params to post|\[optional\]

### Return type

[**CIVote**](CIVote.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
