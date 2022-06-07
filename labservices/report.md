# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az labservices|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az labservices` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az labservices image|Images|[commands](#CommandsInImages)|
|az labservices lab|Labs|[commands](#CommandsInLabs)|
|az labservices labplan|LabPlans|[commands](#CommandsInLabPlans)|
|az labservices operationresult|OperationResults|[commands](#CommandsInOperationResults)|
|az labservices schedule|Schedules|[commands](#CommandsInSchedules)|
|az labservices sku|Skus|[commands](#CommandsInSkus)|
|az labservices usage|Usages|[commands](#CommandsInUsages)|
|az labservices user|Users|[commands](#CommandsInUsers)|
|az labservices virtualmachine|VirtualMachines|[commands](#CommandsInVirtualMachines)|

## COMMANDS
### <a name="CommandsInImages">Commands in `az labservices image` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az labservices image list](#ImagesListByLabPlan)|ListByLabPlan|[Parameters](#ParametersImagesListByLabPlan)|[Example](#ExamplesImagesListByLabPlan)|
|[az labservices image show](#ImagesGet)|Get|[Parameters](#ParametersImagesGet)|[Example](#ExamplesImagesGet)|
|[az labservices image create](#ImagesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersImagesCreateOrUpdate#Create)|[Example](#ExamplesImagesCreateOrUpdate#Create)|
|[az labservices image update](#ImagesUpdate)|Update|[Parameters](#ParametersImagesUpdate)|[Example](#ExamplesImagesUpdate)|

### <a name="CommandsInLabs">Commands in `az labservices lab` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az labservices lab list](#LabsListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersLabsListByResourceGroup)|[Example](#ExamplesLabsListByResourceGroup)|
|[az labservices lab list](#LabsListBySubscription)|ListBySubscription|[Parameters](#ParametersLabsListBySubscription)|[Example](#ExamplesLabsListBySubscription)|
|[az labservices lab show](#LabsGet)|Get|[Parameters](#ParametersLabsGet)|[Example](#ExamplesLabsGet)|
|[az labservices lab create](#LabsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersLabsCreateOrUpdate#Create)|[Example](#ExamplesLabsCreateOrUpdate#Create)|
|[az labservices lab update](#LabsUpdate)|Update|[Parameters](#ParametersLabsUpdate)|[Example](#ExamplesLabsUpdate)|
|[az labservices lab delete](#LabsDelete)|Delete|[Parameters](#ParametersLabsDelete)|[Example](#ExamplesLabsDelete)|
|[az labservices lab publish](#LabsPublish)|Publish|[Parameters](#ParametersLabsPublish)|[Example](#ExamplesLabsPublish)|
|[az labservices lab sync-group](#LabsSyncGroup)|SyncGroup|[Parameters](#ParametersLabsSyncGroup)|[Example](#ExamplesLabsSyncGroup)|

### <a name="CommandsInLabPlans">Commands in `az labservices labplan` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az labservices labplan list](#LabPlansListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersLabPlansListByResourceGroup)|[Example](#ExamplesLabPlansListByResourceGroup)|
|[az labservices labplan list](#LabPlansListBySubscription)|ListBySubscription|[Parameters](#ParametersLabPlansListBySubscription)|[Example](#ExamplesLabPlansListBySubscription)|
|[az labservices labplan show](#LabPlansGet)|Get|[Parameters](#ParametersLabPlansGet)|[Example](#ExamplesLabPlansGet)|
|[az labservices labplan create](#LabPlansCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersLabPlansCreateOrUpdate#Create)|[Example](#ExamplesLabPlansCreateOrUpdate#Create)|
|[az labservices labplan update](#LabPlansUpdate)|Update|[Parameters](#ParametersLabPlansUpdate)|[Example](#ExamplesLabPlansUpdate)|
|[az labservices labplan delete](#LabPlansDelete)|Delete|[Parameters](#ParametersLabPlansDelete)|[Example](#ExamplesLabPlansDelete)|
|[az labservices labplan save-image](#LabPlansSaveImage)|SaveImage|[Parameters](#ParametersLabPlansSaveImage)|[Example](#ExamplesLabPlansSaveImage)|

### <a name="CommandsInOperationResults">Commands in `az labservices operationresult` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az labservices operationresult show](#OperationResultsGet)|Get|[Parameters](#ParametersOperationResultsGet)|[Example](#ExamplesOperationResultsGet)|

### <a name="CommandsInSchedules">Commands in `az labservices schedule` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az labservices schedule list](#SchedulesListByLab)|ListByLab|[Parameters](#ParametersSchedulesListByLab)|[Example](#ExamplesSchedulesListByLab)|
|[az labservices schedule show](#SchedulesGet)|Get|[Parameters](#ParametersSchedulesGet)|[Example](#ExamplesSchedulesGet)|
|[az labservices schedule create](#SchedulesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersSchedulesCreateOrUpdate#Create)|[Example](#ExamplesSchedulesCreateOrUpdate#Create)|
|[az labservices schedule update](#SchedulesUpdate)|Update|[Parameters](#ParametersSchedulesUpdate)|[Example](#ExamplesSchedulesUpdate)|
|[az labservices schedule delete](#SchedulesDelete)|Delete|[Parameters](#ParametersSchedulesDelete)|[Example](#ExamplesSchedulesDelete)|

### <a name="CommandsInSkus">Commands in `az labservices sku` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az labservices sku list](#SkusList)|List|[Parameters](#ParametersSkusList)|[Example](#ExamplesSkusList)|

### <a name="CommandsInUsages">Commands in `az labservices usage` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az labservices usage list](#UsagesListByLocation)|ListByLocation|[Parameters](#ParametersUsagesListByLocation)|[Example](#ExamplesUsagesListByLocation)|

### <a name="CommandsInUsers">Commands in `az labservices user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az labservices user list](#UsersListByLab)|ListByLab|[Parameters](#ParametersUsersListByLab)|[Example](#ExamplesUsersListByLab)|
|[az labservices user show](#UsersGet)|Get|[Parameters](#ParametersUsersGet)|[Example](#ExamplesUsersGet)|
|[az labservices user create](#UsersCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersUsersCreateOrUpdate#Create)|[Example](#ExamplesUsersCreateOrUpdate#Create)|
|[az labservices user update](#UsersUpdate)|Update|[Parameters](#ParametersUsersUpdate)|[Example](#ExamplesUsersUpdate)|
|[az labservices user delete](#UsersDelete)|Delete|[Parameters](#ParametersUsersDelete)|[Example](#ExamplesUsersDelete)|
|[az labservices user invite](#UsersInvite)|Invite|[Parameters](#ParametersUsersInvite)|[Example](#ExamplesUsersInvite)|

### <a name="CommandsInVirtualMachines">Commands in `az labservices virtualmachine` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az labservices virtualmachine list](#VirtualMachinesListByLab)|ListByLab|[Parameters](#ParametersVirtualMachinesListByLab)|[Example](#ExamplesVirtualMachinesListByLab)|
|[az labservices virtualmachine show](#VirtualMachinesGet)|Get|[Parameters](#ParametersVirtualMachinesGet)|[Example](#ExamplesVirtualMachinesGet)|
|[az labservices virtualmachine redeploy](#VirtualMachinesRedeploy)|Redeploy|[Parameters](#ParametersVirtualMachinesRedeploy)|[Example](#ExamplesVirtualMachinesRedeploy)|
|[az labservices virtualmachine reimage](#VirtualMachinesReimage)|Reimage|[Parameters](#ParametersVirtualMachinesReimage)|[Example](#ExamplesVirtualMachinesReimage)|
|[az labservices virtualmachine reset-password](#VirtualMachinesResetPassword)|ResetPassword|[Parameters](#ParametersVirtualMachinesResetPassword)|[Example](#ExamplesVirtualMachinesResetPassword)|
|[az labservices virtualmachine start](#VirtualMachinesStart)|Start|[Parameters](#ParametersVirtualMachinesStart)|[Example](#ExamplesVirtualMachinesStart)|
|[az labservices virtualmachine stop](#VirtualMachinesStop)|Stop|[Parameters](#ParametersVirtualMachinesStop)|[Example](#ExamplesVirtualMachinesStop)|


## COMMAND DETAILS
### group `az labservices image`
#### <a name="ImagesListByLabPlan">Command `az labservices image list`</a>

##### <a name="ExamplesImagesListByLabPlan">Example</a>
```
az labservices image list --lab-plan-name "testlabplan" --resource-group "testrg123"
```
##### <a name="ParametersImagesListByLabPlan">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-plan-name**|string|The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.|lab_plan_name|labPlanName|
|**--filter**|string|The filter to apply to the operation.|filter|$filter|

#### <a name="ImagesGet">Command `az labservices image show`</a>

##### <a name="ExamplesImagesGet">Example</a>
```
az labservices image show --name "image1" --lab-plan-name "testlabplan" --resource-group "testrg123"
```
##### <a name="ParametersImagesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-plan-name**|string|The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.|lab_plan_name|labPlanName|
|**--image-name**|string|The image name.|image_name|imageName|

#### <a name="ImagesCreateOrUpdate#Create">Command `az labservices image create`</a>

##### <a name="ExamplesImagesCreateOrUpdate#Create">Example</a>
```
az labservices image create --enabled-state "Enabled" --name "image1" --lab-plan-name "testlabplan" --resource-group \
"testrg123"
```
##### <a name="ParametersImagesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-plan-name**|string|The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.|lab_plan_name|labPlanName|
|**--image-name**|string|The image name.|image_name|imageName|
|**--enabled-state**|sealed-choice|Is the image enabled|enabled_state|enabledState|
|**--available-regions**|array|The available regions of the image in the shared gallery.|available_regions|availableRegions|

#### <a name="ImagesUpdate">Command `az labservices image update`</a>

##### <a name="ExamplesImagesUpdate">Example</a>
```
az labservices image update --enabled-state "Enabled" --name "image1" --lab-plan-name "testlabplan" --resource-group \
"testrg123"
```
##### <a name="ParametersImagesUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-plan-name**|string|The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.|lab_plan_name|labPlanName|
|**--image-name**|string|The image name.|image_name|imageName|
|**--enabled-state**|sealed-choice|Is the image enabled|enabled_state|enabledState|

### group `az labservices lab`
#### <a name="LabsListByResourceGroup">Command `az labservices lab list`</a>

##### <a name="ExamplesLabsListByResourceGroup">Example</a>
```
az labservices lab list --resource-group "testrg123"
```
##### <a name="ParametersLabsListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|

#### <a name="LabsListBySubscription">Command `az labservices lab list`</a>

##### <a name="ExamplesLabsListBySubscription">Example</a>
```
az labservices lab list
```
##### <a name="ParametersLabsListBySubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--filter**|string|The filter to apply to the operation.|filter|$filter|

#### <a name="LabsGet">Command `az labservices lab show`</a>

##### <a name="ExamplesLabsGet">Example</a>
```
az labservices lab show --name "testlab" --resource-group "testrg123"
```
##### <a name="ParametersLabsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|

#### <a name="LabsCreateOrUpdate#Create">Command `az labservices lab create`</a>

##### <a name="ExamplesLabsCreateOrUpdate#Create">Example</a>
```
az labservices lab create --location "westus" --description "This is a test lab." --auto-shutdown-profile \
disconnect-delay="00:05" idle-delay="01:00" no-connect-delay="01:00" shutdown-on-disconnect="Enabled" \
shutdown-on-idle="UserAbsence" shutdown-when-not-connected="Enabled" --connection-profile client-rdp-access="Public" \
client-ssh-access="Public" web-rdp-access="None" web-ssh-access="None" --lab-plan-id "/subscriptions/34adfa4f-cedf-4dc0\
-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.LabServices/labPlans/testlabplan" --network-profile \
subnet-id="/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.Network/vir\
tualNetworks/test-vnet/subnets/default" --open-access "Disabled" --title "Test Lab" --additional-capabilities \
install-gpu-drivers="Disabled" --admin-user username="test-user" --create-option "TemplateVM" --image-reference \
offer="WindowsServer" publisher="Microsoft" sku="2019-Datacenter" version="2019.0.20190410" --sku name="Medium" \
--usage-quota "10:00" --use-shared-password "Disabled" --name "testlab" --resource-group "testrg123"
```
##### <a name="ParametersLabsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--location**|string|The geo-location where the resource lives|location|location|
|**--tags**|dictionary|Resource tags.|tags|tags|
|**--auto-shutdown-profile**|object|The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.|auto_shutdown_profile|autoShutdownProfile|
|**--connection-profile**|object|The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.|connection_profile|connectionProfile|
|**--roster-profile**|object|The lab user list management profile.|roster_profile|rosterProfile|
|**--lab-plan-id**|string|The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..|lab_plan_id|labPlanId|
|**--title**|string|The title of the lab.|title|title|
|**--description**|string|The description of the lab.|description|description|
|**--network-profile**|object|The network profile for the lab, typically applied via a lab plan. This profile cannot be modified once a lab has been created.|network_profile|networkProfile|
|**--open-access**|sealed-choice|Whether any user or only specified users can register to a lab.|open_access|openAccess|
|**--create-option**|sealed-choice|Indicates what lab virtual machines are created from.|create_option|createOption|
|**--image-reference**|object|The image configuration for lab virtual machines.|image_reference|imageReference|
|**--sku**|object|The SKU for the lab. Defines the type of virtual machines used in the lab.|sku|sku|
|**--additional-capabilities**|object|Additional VM capabilities.|additional_capabilities|additionalCapabilities|
|**--usage-quota**|duration|The initial quota alloted to each lab user. Must be a time span between 0 and 9999 hours.|usage_quota|usageQuota|
|**--use-shared-password**|sealed-choice|Enabling this option will use the same password for all user VMs.|use_shared_password|useSharedPassword|
|**--admin-user**|object|Credentials for the admin user on the VM.|admin_user|adminUser|
|**--non-admin-user**|object|Credentials for the non-admin user on the VM, if one exists.|non_admin_user|nonAdminUser|

#### <a name="LabsUpdate">Command `az labservices lab update`</a>

##### <a name="ExamplesLabsUpdate">Example</a>
```
az labservices lab update --open-access "Enabled" --name "testlab" --resource-group "testrg123"
```
##### <a name="ParametersLabsUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--tags**|array|Resource tags.|tags|tags|
|**--auto-shutdown-profile**|object|The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.|auto_shutdown_profile|autoShutdownProfile|
|**--connection-profile**|object|The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.|connection_profile|connectionProfile|
|**--roster-profile**|object|The lab user list management profile.|roster_profile|rosterProfile|
|**--lab-plan-id**|string|The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..|lab_plan_id|labPlanId|
|**--title**|string|The title of the lab.|title|title|
|**--description**|string|The description of the lab.|description|description|
|**--open-access**|sealed-choice|Whether any user or only specified users can register to a lab.|open_access|openAccess|
|**--create-option**|sealed-choice|Indicates what lab virtual machines are created from.|create_option|createOption|
|**--image-reference**|object|The image configuration for lab virtual machines.|image_reference|imageReference|
|**--sku**|object|The SKU for the lab. Defines the type of virtual machines used in the lab.|sku|sku|
|**--additional-capabilities**|object|Additional VM capabilities.|additional_capabilities|additionalCapabilities|
|**--usage-quota**|duration|The initial quota alloted to each lab user. Must be a time span between 0 and 9999 hours.|usage_quota|usageQuota|
|**--use-shared-password**|sealed-choice|Enabling this option will use the same password for all user VMs.|use_shared_password|useSharedPassword|
|**--admin-user**|object|Credentials for the admin user on the VM.|admin_user|adminUser|
|**--non-admin-user**|object|Credentials for the non-admin user on the VM, if one exists.|non_admin_user|nonAdminUser|

#### <a name="LabsDelete">Command `az labservices lab delete`</a>

##### <a name="ExamplesLabsDelete">Example</a>
```
az labservices lab delete --name "testlab" --resource-group "testrg123"
```
##### <a name="ParametersLabsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|

#### <a name="LabsPublish">Command `az labservices lab publish`</a>

##### <a name="ExamplesLabsPublish">Example</a>
```
az labservices lab publish --name "testlab" --resource-group "testrg123"
```
##### <a name="ParametersLabsPublish">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|

#### <a name="LabsSyncGroup">Command `az labservices lab sync-group`</a>

##### <a name="ExamplesLabsSyncGroup">Example</a>
```
az labservices lab sync-group --name "testlab" --resource-group "testrg123"
```
##### <a name="ParametersLabsSyncGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|

### group `az labservices labplan`
#### <a name="LabPlansListByResourceGroup">Command `az labservices labplan list`</a>

##### <a name="ExamplesLabPlansListByResourceGroup">Example</a>
```
az labservices labplan list --resource-group "testrg123"
```
##### <a name="ParametersLabPlansListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|

#### <a name="LabPlansListBySubscription">Command `az labservices labplan list`</a>

##### <a name="ExamplesLabPlansListBySubscription">Example</a>
```
az labservices labplan list
```
##### <a name="ParametersLabPlansListBySubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--filter**|string|The filter to apply to the operation.|filter|$filter|

#### <a name="LabPlansGet">Command `az labservices labplan show`</a>

##### <a name="ExamplesLabPlansGet">Example</a>
```
az labservices labplan show --name "testlabplan" --resource-group "testrg123"
```
##### <a name="ParametersLabPlansGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-plan-name**|string|The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.|lab_plan_name|labPlanName|

#### <a name="LabPlansCreateOrUpdate#Create">Command `az labservices labplan create`</a>

##### <a name="ExamplesLabPlansCreateOrUpdate#Create">Example</a>
```
az labservices labplan create --location "westus" --default-auto-shutdown-profile disconnect-delay="00:05" \
idle-delay="01:00" no-connect-delay="01:00" shutdown-on-disconnect="Enabled" shutdown-on-idle="UserAbsence" \
shutdown-when-not-connected="Enabled" --default-connection-profile client-rdp-access="Public" \
client-ssh-access="Public" web-rdp-access="None" web-ssh-access="None" --subnet-id "/subscriptions/34adfa4f-cedf-4dc0-b\
a29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/default" \
--shared-gallery-id "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.C\
ompute/galleries/testsig" --support-info email="help@contoso.com" instructions="Contact support for help." \
phone="+1-202-555-0123" url="help.contoso.com" --name "testlabplan" --resource-group "testrg123"
```
##### <a name="ParametersLabPlansCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-plan-name**|string|The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.|lab_plan_name|labPlanName|
|**--location**|string|The geo-location where the resource lives|location|location|
|**--tags**|dictionary|Resource tags.|tags|tags|
|**--default-connection-profile**|object|The default lab connection profile. This can be changed on a lab resource and only provides a default profile.|default_connection_profile|defaultConnectionProfile|
|**--default-auto-shutdown-profile**|object|The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.|default_auto_shutdown_profile|defaultAutoShutdownProfile|
|**--allowed-regions**|array|The allowed regions for the lab creator to use when creating labs using this lab plan.|allowed_regions|allowedRegions|
|**--shared-gallery-id**|string|Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.|shared_gallery_id|sharedGalleryId|
|**--support-info**|object|Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.|support_info|supportInfo|
|**--linked-lms-instance**|string|Base Url of the lms instance this lab plan can link lab rosters against.|linked_lms_instance|linkedLmsInstance|
|**--subnet-id**|string|The external subnet resource id|subnet_id|subnetId|

#### <a name="LabPlansUpdate">Command `az labservices labplan update`</a>

##### <a name="ExamplesLabPlansUpdate">Example</a>
```
az labservices labplan update --default-connection-profile client-rdp-access="Public" client-ssh-access="Public" \
web-rdp-access="None" web-ssh-access="None" --name "testlabplan" --resource-group "testrg123"
```
##### <a name="ParametersLabPlansUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-plan-name**|string|The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.|lab_plan_name|labPlanName|
|**--tags**|array|Resource tags.|tags|tags|
|**--default-connection-profile**|object|The default lab connection profile. This can be changed on a lab resource and only provides a default profile.|default_connection_profile|defaultConnectionProfile|
|**--default-auto-shutdown-profile**|object|The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.|default_auto_shutdown_profile|defaultAutoShutdownProfile|
|**--allowed-regions**|array|The allowed regions for the lab creator to use when creating labs using this lab plan.|allowed_regions|allowedRegions|
|**--shared-gallery-id**|string|Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.|shared_gallery_id|sharedGalleryId|
|**--support-info**|object|Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.|support_info|supportInfo|
|**--linked-lms-instance**|string|Base Url of the lms instance this lab plan can link lab rosters against.|linked_lms_instance|linkedLmsInstance|
|**--subnet-id**|string|The external subnet resource id|subnet_id|subnetId|

#### <a name="LabPlansDelete">Command `az labservices labplan delete`</a>

##### <a name="ExamplesLabPlansDelete">Example</a>
```
az labservices labplan delete --name "testlabplan" --resource-group "testrg123"
```
##### <a name="ParametersLabPlansDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-plan-name**|string|The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.|lab_plan_name|labPlanName|

#### <a name="LabPlansSaveImage">Command `az labservices labplan save-image`</a>

##### <a name="ExamplesLabPlansSaveImage">Example</a>
```
az labservices labplan save-image --name "Test Image" --lab-virtual-machine-id "/subscriptions/34adfa4f-cedf-4dc0-ba29-\
b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.LabServices/labs/testlab/virtualMachines/template" \
--lab-plan-name "testlabplan" --resource-group "testrg123"
```
##### <a name="ParametersLabPlansSaveImage">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-plan-name**|string|The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.|lab_plan_name|labPlanName|
|**--name**|string|The name for the image we create.|name|name|
|**--lab-virtual-machine-id**|string|The ID of the lab virtual machine you want to save an image from.|lab_virtual_machine_id|labVirtualMachineId|

### group `az labservices operationresult`
#### <a name="OperationResultsGet">Command `az labservices operationresult show`</a>

##### <a name="ExamplesOperationResultsGet">Example</a>
```
az labservices operationresult show --operation-result-id "a64149d8-84cb-4566-ab8e-b4ee1a074174"
```
##### <a name="ParametersOperationResultsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--operation-result-id**|string|The operation result ID / name.|operation_result_id|operationResultId|

### group `az labservices schedule`
#### <a name="SchedulesListByLab">Command `az labservices schedule list`</a>

##### <a name="ExamplesSchedulesListByLab">Example</a>
```
az labservices schedule list --lab-name "testlab" --resource-group "testrg123"
```
##### <a name="ParametersSchedulesListByLab">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--filter**|string|The filter to apply to the operation.|filter|$filter|

#### <a name="SchedulesGet">Command `az labservices schedule show`</a>

##### <a name="ExamplesSchedulesGet">Example</a>
```
az labservices schedule show --lab-name "testlab" --resource-group "testrg123" --name "schedule1"
```
##### <a name="ParametersSchedulesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--schedule-name**|string|The name of the schedule that uniquely identifies it within containing lab. Used in resource URIs.|schedule_name|scheduleName|

#### <a name="SchedulesCreateOrUpdate#Create">Command `az labservices schedule create`</a>

##### <a name="ExamplesSchedulesCreateOrUpdate#Create">Example</a>
```
az labservices schedule create --notes "Schedule 1 for students" --recurrence-pattern expiration-date="2020-08-14" \
frequency="Daily" interval=2 --start-at "2020-05-26T12:00:00Z" --stop-at "2020-05-26T18:00:00Z" --time-zone-id \
"America/Los_Angeles" --lab-name "testlab" --resource-group "testrg123" --name "schedule1"
```
##### <a name="ParametersSchedulesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--schedule-name**|string|The name of the schedule that uniquely identifies it within containing lab. Used in resource URIs.|schedule_name|scheduleName|
|**--start-at**|date-time|When lab user virtual machines will be started. Timestamp offsets will be ignored and timeZoneId is used instead.|start_at|startAt|
|**--stop-at**|date-time|When lab user virtual machines will be stopped. Timestamp offsets will be ignored and timeZoneId is used instead.|stop_at|stopAt|
|**--recurrence-pattern**|object|The recurrence pattern of the scheduled actions.|recurrence_pattern|recurrencePattern|
|**--time-zone-id**|string|The IANA timezone id for the schedule.|time_zone_id|timeZoneId|
|**--notes**|string|Notes for this schedule.|notes|notes|

#### <a name="SchedulesUpdate">Command `az labservices schedule update`</a>

##### <a name="ExamplesSchedulesUpdate">Example</a>
```
az labservices schedule update --recurrence-pattern expiration-date="2020-08-14" frequency="Daily" interval=2 \
--lab-name "testlab" --resource-group "testrg123" --name "schedule1"
```
##### <a name="ParametersSchedulesUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--schedule-name**|string|The name of the schedule that uniquely identifies it within containing lab. Used in resource URIs.|schedule_name|scheduleName|
|**--start-at**|date-time|When lab user virtual machines will be started. Timestamp offsets will be ignored and timeZoneId is used instead.|start_at|startAt|
|**--stop-at**|date-time|When lab user virtual machines will be stopped. Timestamp offsets will be ignored and timeZoneId is used instead.|stop_at|stopAt|
|**--recurrence-pattern**|object|The recurrence pattern of the scheduled actions.|recurrence_pattern|recurrencePattern|
|**--time-zone-id**|string|The IANA timezone id for the schedule.|time_zone_id|timeZoneId|
|**--notes**|string|Notes for this schedule.|notes|notes|

#### <a name="SchedulesDelete">Command `az labservices schedule delete`</a>

##### <a name="ExamplesSchedulesDelete">Example</a>
```
az labservices schedule delete --lab-name "testlab" --resource-group "testrg123" --name "schedule1"
```
##### <a name="ParametersSchedulesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--schedule-name**|string|The name of the schedule that uniquely identifies it within containing lab. Used in resource URIs.|schedule_name|scheduleName|

### group `az labservices sku`
#### <a name="SkusList">Command `az labservices sku list`</a>

##### <a name="ExamplesSkusList">Example</a>
```
az labservices sku list
```
##### <a name="ParametersSkusList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--filter**|string|The filter to apply to the operation.|filter|$filter|

### group `az labservices usage`
#### <a name="UsagesListByLocation">Command `az labservices usage list`</a>

##### <a name="ExamplesUsagesListByLocation">Example</a>
```
az labservices usage list --location "westus2"
```
##### <a name="ParametersUsagesListByLocation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The location name.|location|location|
|**--filter**|string|The filter to apply to the operation.|filter|$filter|

### group `az labservices user`
#### <a name="UsersListByLab">Command `az labservices user list`</a>

##### <a name="ExamplesUsersListByLab">Example</a>
```
az labservices user list --lab-name "testlab" --resource-group "testrg123"
```
##### <a name="ParametersUsersListByLab">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--filter**|string|The filter to apply to the operation.|filter|$filter|

#### <a name="UsersGet">Command `az labservices user show`</a>

##### <a name="ExamplesUsersGet">Example</a>
```
az labservices user show --lab-name "testlab" --resource-group "testrg123" --name "testuser"
```
##### <a name="ParametersUsersGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--user-name**|string|The name of the user that uniquely identifies it within containing lab. Used in resource URIs.|user_name|userName|

#### <a name="UsersCreateOrUpdate#Create">Command `az labservices user create`</a>

##### <a name="ExamplesUsersCreateOrUpdate#Create">Example</a>
```
az labservices user create --additional-usage-quota "20:00" --email "testuser@contoso.com" --lab-name "testlab" \
--resource-group "testrg123" --name "testuser"
```
##### <a name="ParametersUsersCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--user-name**|string|The name of the user that uniquely identifies it within containing lab. Used in resource URIs.|user_name|userName|
|**--additional-usage-quota**|duration|The amount of usage quota time the user gets in addition to the lab usage quota.|additional_usage_quota|additionalUsageQuota|
|**--email**|string|Email address of the user.|email|email|

#### <a name="UsersUpdate">Command `az labservices user update`</a>

##### <a name="ExamplesUsersUpdate">Example</a>
```
az labservices user update --additional-usage-quota "20:00" --lab-name "testlab" --resource-group "testrg123" --name \
"testuser"
```
##### <a name="ParametersUsersUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--user-name**|string|The name of the user that uniquely identifies it within containing lab. Used in resource URIs.|user_name|userName|
|**--additional-usage-quota**|duration|The amount of usage quota time the user gets in addition to the lab usage quota.|additional_usage_quota|additionalUsageQuota|

#### <a name="UsersDelete">Command `az labservices user delete`</a>

##### <a name="ExamplesUsersDelete">Example</a>
```
az labservices user delete --lab-name "testlab" --resource-group "testrg123" --name "testuser"
```
##### <a name="ParametersUsersDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--user-name**|string|The name of the user that uniquely identifies it within containing lab. Used in resource URIs.|user_name|userName|

#### <a name="UsersInvite">Command `az labservices user invite`</a>

##### <a name="ExamplesUsersInvite">Example</a>
```
az labservices user invite --text "Invitation to lab testlab" --lab-name "testlab" --resource-group "testrg123" --name \
"testuser"
```
##### <a name="ParametersUsersInvite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--user-name**|string|The name of the user that uniquely identifies it within containing lab. Used in resource URIs.|user_name|userName|
|**--text**|string|Custom text for the invite email.|text|text|

### group `az labservices virtualmachine`
#### <a name="VirtualMachinesListByLab">Command `az labservices virtualmachine list`</a>

##### <a name="ExamplesVirtualMachinesListByLab">Example</a>
```
az labservices virtualmachine list --lab-name "testlab" --resource-group "testrg123"
```
##### <a name="ParametersVirtualMachinesListByLab">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--filter**|string|The filter to apply to the operation.|filter|$filter|

#### <a name="VirtualMachinesGet">Command `az labservices virtualmachine show`</a>

##### <a name="ExamplesVirtualMachinesGet">Example</a>
```
az labservices virtualmachine show --lab-name "testlab" --resource-group "testrg123" --name "template"
```
##### <a name="ParametersVirtualMachinesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--virtual-machine-name**|string|The ID of the virtual machine that uniquely identifies it within the containing lab. Used in resource URIs.|virtual_machine_name|virtualMachineName|

#### <a name="VirtualMachinesRedeploy">Command `az labservices virtualmachine redeploy`</a>

##### <a name="ExamplesVirtualMachinesRedeploy">Example</a>
```
az labservices virtualmachine redeploy --lab-name "testlab" --resource-group "testrg123" --name "template"
```
##### <a name="ParametersVirtualMachinesRedeploy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--virtual-machine-name**|string|The ID of the virtual machine that uniquely identifies it within the containing lab. Used in resource URIs.|virtual_machine_name|virtualMachineName|

#### <a name="VirtualMachinesReimage">Command `az labservices virtualmachine reimage`</a>

##### <a name="ExamplesVirtualMachinesReimage">Example</a>
```
az labservices virtualmachine reimage --lab-name "testlab" --resource-group "testrg123" --name "template"
```
##### <a name="ParametersVirtualMachinesReimage">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--virtual-machine-name**|string|The ID of the virtual machine that uniquely identifies it within the containing lab. Used in resource URIs.|virtual_machine_name|virtualMachineName|

#### <a name="VirtualMachinesResetPassword">Command `az labservices virtualmachine reset-password`</a>

##### <a name="ExamplesVirtualMachinesResetPassword">Example</a>
```
az labservices virtualmachine reset-password --password "example-password" --username "example-username" --lab-name \
"testlab" --resource-group "testrg123" --name "template"
```
##### <a name="ParametersVirtualMachinesResetPassword">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--virtual-machine-name**|string|The ID of the virtual machine that uniquely identifies it within the containing lab. Used in resource URIs.|virtual_machine_name|virtualMachineName|
|**--username**|string|The user whose password is being reset|username|username|
|**--password**|string|The password|password|password|

#### <a name="VirtualMachinesStart">Command `az labservices virtualmachine start`</a>

##### <a name="ExamplesVirtualMachinesStart">Example</a>
```
az labservices virtualmachine start --lab-name "testlab" --resource-group "testrg123" --name "template"
```
##### <a name="ParametersVirtualMachinesStart">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--virtual-machine-name**|string|The ID of the virtual machine that uniquely identifies it within the containing lab. Used in resource URIs.|virtual_machine_name|virtualMachineName|

#### <a name="VirtualMachinesStop">Command `az labservices virtualmachine stop`</a>

##### <a name="ExamplesVirtualMachinesStop">Example</a>
```
az labservices virtualmachine stop --lab-name "testlab" --resource-group "testrg123" --name "template"
```
##### <a name="ParametersVirtualMachinesStop">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--lab-name**|string|The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.|lab_name|labName|
|**--virtual-machine-name**|string|The ID of the virtual machine that uniquely identifies it within the containing lab. Used in resource URIs.|virtual_machine_name|virtualMachineName|
