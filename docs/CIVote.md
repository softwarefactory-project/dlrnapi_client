# CIVote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | name of the CI sending the vote | [optional] 
**commit_hash** | **str** | commit_hash of tested repo | [optional] 
**distro_hash** | **str** | distro_hash of tested repo | [optional] 
**url** | **str** | URL where to find additional information from the CI execution | [optional] 
**timestamp** | **int** | Timestamp (in seconds since the epoch) | [optional] 
**in_progress** | **bool** | is this CI job still in-progress? | [optional] 
**success** | **bool** | Was the CI execution successful? | [optional] 
**notes** | **str** | additional notes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


