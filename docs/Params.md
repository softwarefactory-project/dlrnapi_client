# Params

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_age** | **int** | Maximum age (in hours) for the repo to be considered. Any repo tested or being tested after \&quot;now - max_age\&quot; will be taken into account. If set to 0, all repos will be considered.  | 
**success** | **bool** | If set to a value, find repos with a successful/unsuccessful vote (as specified). If not set, any tested repo will be considered.  | [optional] 
**job_id** | **str** | Name of the CI that sent the vote. If not set, no filter will be set on CI.  | [optional] 
**sequential_mode** | **bool** | Use the sequential mode algorithm. In this case, return the last tested repo within that timeframe for the CI job described by previous_job_id. Defaults to false.  | [optional] 
**previous_job_id** | **str** | If sequential_mode is set to true, look for jobs tested by the CI identified by previous_job_id.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


