# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from azext_labservices.generated._client_factory import cf_usage
from azext_labservices.generated.commands import labservices_usage
from azext_labservices.manual._transformers import transform_usage_table


def load_command_table(self, _):

    with self.command_group('labservices') as g:
        g.custom_command('upgrade', 'labservices_upgrade')

    # override the default table output for usage
    with self.command_group('labservices usage', labservices_usage, client_factory=cf_usage) as g:
        g.custom_command('list', 'labservices_usage_list', table_transformer=transform_usage_table)
