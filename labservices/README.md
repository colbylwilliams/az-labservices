# Azure CLI labservices Extension #
This is the extension for labservices

### How to use ###
Install this extension using the below CLI command
```
az extension add --name labservices
```

### Included Features ###
#### labservices image ####
##### Create #####
```
az labservices image create --enabled-state "Enabled" --name "image1" --lab-plan-name "testlabplan" \
    --resource-group "testrg123" 
```
##### Show #####
```
az labservices image show --name "image1" --lab-plan-name "testlabplan" --resource-group "testrg123"
```
##### List #####
```
az labservices image list --lab-plan-name "testlabplan" --resource-group "testrg123"
```
##### Update #####
```
az labservices image update --enabled-state "Enabled" --name "image1" --lab-plan-name "testlabplan" \
    --resource-group "testrg123" 
```
#### labservices labplan ####
##### Create #####
```
az labservices labplan create --location "westus" \
    --default-auto-shutdown-profile disconnect-delay="00:05" idle-delay="01:00" no-connect-delay="01:00" shutdown-on-disconnect="Enabled" shutdown-on-idle="UserAbsence" shutdown-when-not-connected="Enabled" \
    --default-connection-profile client-rdp-access="Public" client-ssh-access="Public" web-rdp-access="None" web-ssh-access="None" \
    --subnet-id "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/default" \
    --shared-gallery-id "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.Compute/galleries/testsig" \
    --support-info email="help@contoso.com" instructions="Contact support for help." phone="+1-202-555-0123" url="help.contoso.com" \
    --name "testlabplan" --resource-group "testrg123" 

az labservices labplan wait --created --name "{myLabPlan}" --resource-group "{rg}"
```
##### Show #####
```
az labservices labplan show --name "testlabplan" --resource-group "testrg123"
```
##### List #####
```
az labservices labplan list --resource-group "testrg123"
```
##### Update #####
```
az labservices labplan update \
    --default-connection-profile client-rdp-access="Public" client-ssh-access="Public" web-rdp-access="None" web-ssh-access="None" \
    --name "testlabplan" --resource-group "testrg123" 
```
##### Save-image #####
```
az labservices labplan save-image --name "Test Image" \
    --lab-virtual-machine-id "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.LabServices/labs/testlab/virtualMachines/template" \
    --lab-plan-name "testlabplan" --resource-group "testrg123" 
```
##### Delete #####
```
az labservices labplan delete --name "testlabplan" --resource-group "testrg123"
```
#### labservices lab ####
##### Create #####
```
az labservices lab create --location "westus" --description "This is a test lab." \
    --auto-shutdown-profile disconnect-delay="00:05" idle-delay="01:00" no-connect-delay="01:00" shutdown-on-disconnect="Enabled" shutdown-on-idle="UserAbsence" shutdown-when-not-connected="Enabled" \
    --connection-profile client-rdp-access="Public" client-ssh-access="Public" web-rdp-access="None" web-ssh-access="None" \
    --lab-plan-id "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.LabServices/labPlans/testlabplan" \
    --network-profile subnet-id="/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/default" \
    --open-access "Disabled" --title "Test Lab" --additional-capabilities install-gpu-drivers="Disabled" \
    --admin-user username="test-user" --create-option "TemplateVM" \
    --image-reference offer="WindowsServer" publisher="Microsoft" sku="2019-Datacenter" version="2019.0.20190410" \
    --sku name="Medium" --usage-quota "10:00" --use-shared-password "Disabled" --name "testlab" \
    --resource-group "testrg123" 

az labservices lab wait --created --name "{myLab}" --resource-group "{rg}"
```
##### Show #####
```
az labservices lab show --name "testlab" --resource-group "testrg123"
```
##### List #####
```
az labservices lab list --resource-group "testrg123"
```
##### Update #####
```
az labservices lab update --open-access "Enabled" --name "testlab" --resource-group "testrg123"
```
##### Publish #####
```
az labservices lab publish --name "testlab" --resource-group "testrg123"
```
##### Sync-group #####
```
az labservices lab sync-group --name "testlab" --resource-group "testrg123"
```
##### Delete #####
```
az labservices lab delete --name "testlab" --resource-group "testrg123"
```
#### labservices operationresult ####
##### Show #####
```
az labservices operationresult show --operation-result-id "a64149d8-84cb-4566-ab8e-b4ee1a074174"
```
#### labservices schedule ####
##### Create #####
```
az labservices schedule create --notes "Schedule 1 for students" \
    --recurrence-pattern expiration-date="2020-08-14" frequency="Daily" interval=2 --start-at "2020-05-26T12:00:00Z" \
    --stop-at "2020-05-26T18:00:00Z" --time-zone-id "America/Los_Angeles" --lab-name "testlab" \
    --resource-group "testrg123" --name "schedule1" 
```
##### Show #####
```
az labservices schedule show --lab-name "testlab" --resource-group "testrg123" --name "schedule1"
```
##### List #####
```
az labservices schedule list --lab-name "testlab" --resource-group "testrg123"
```
##### Update #####
```
az labservices schedule update --recurrence-pattern expiration-date="2020-08-14" frequency="Daily" interval=2 \
    --lab-name "testlab" --resource-group "testrg123" --name "schedule1" 
```
##### Delete #####
```
az labservices schedule delete --lab-name "testlab" --resource-group "testrg123" --name "schedule1"
```
#### labservices user ####
##### Create #####
```
az labservices user create --additional-usage-quota "20:00" --email "testuser@contoso.com" --lab-name "testlab" \
    --resource-group "testrg123" --name "testuser" 

az labservices user wait --created --lab-name "{myLab}" --resource-group "{rg}" --name "{myUser}"
```
##### Show #####
```
az labservices user show --lab-name "testlab" --resource-group "testrg123" --name "testuser"
```
##### List #####
```
az labservices user list --lab-name "testlab" --resource-group "testrg123"
```
##### Update #####
```
az labservices user update --additional-usage-quota "20:00" --lab-name "testlab" --resource-group "testrg123" \
    --name "testuser" 
```
##### Invite #####
```
az labservices user invite --text "Invitation to lab testlab" --lab-name "testlab" --resource-group "testrg123" \
    --name "testuser" 
```
##### Delete #####
```
az labservices user delete --lab-name "testlab" --resource-group "testrg123" --name "testuser"
```
#### labservices virtualmachine ####
##### List #####
```
az labservices virtualmachine list --lab-name "testlab" --resource-group "testrg123"
```
##### Show #####
```
az labservices virtualmachine show --lab-name "testlab" --resource-group "testrg123" --name "template"
```
##### Redeploy #####
```
az labservices virtualmachine redeploy --lab-name "testlab" --resource-group "testrg123" --name "template"
```
##### Reimage #####
```
az labservices virtualmachine reimage --lab-name "testlab" --resource-group "testrg123" --name "template"
```
##### Reset-password #####
```
az labservices virtualmachine reset-password --password "example-password" --username "example-username" \
    --lab-name "testlab" --resource-group "testrg123" --name "template" 
```
##### Start #####
```
az labservices virtualmachine start --lab-name "testlab" --resource-group "testrg123" --name "template"
```
##### Stop #####
```
az labservices virtualmachine stop --lab-name "testlab" --resource-group "testrg123" --name "template"
```
#### labservices usage ####
##### List #####
```
az labservices usage list --location "westus2"
```
#### labservices sku ####
##### List #####
```
az labservices sku list
```