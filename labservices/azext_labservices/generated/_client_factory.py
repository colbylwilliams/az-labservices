# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_labservices_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.labservices import LabServicesClient
    return get_mgmt_service_client(cli_ctx,
                                   LabServicesClient)


def cf_image(cli_ctx, *_):
    return cf_labservices_cl(cli_ctx).images


def cf_labplan(cli_ctx, *_):
    return cf_labservices_cl(cli_ctx).labplans


def cf_lab(cli_ctx, *_):
    return cf_labservices_cl(cli_ctx).labs


def cf_operationresult(cli_ctx, *_):
    return cf_labservices_cl(cli_ctx).operationresults


def cf_schedule(cli_ctx, *_):
    return cf_labservices_cl(cli_ctx).schedules


def cf_user(cli_ctx, *_):
    return cf_labservices_cl(cli_ctx).users


def cf_virtualmachine(cli_ctx, *_):
    return cf_labservices_cl(cli_ctx).virtualmachines


def cf_usage(cli_ctx, *_):
    return cf_labservices_cl(cli_ctx).usages


def cf_sku(cli_ctx, *_):
    return cf_labservices_cl(cli_ctx).skus
