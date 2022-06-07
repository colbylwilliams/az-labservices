# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_labservices.manual._validators import \
    labservices_source_version_validator


def load_arguments(self, _):

    with self.argument_context('labservices upgrade') as c:
        c.argument('version', options_list=['--version', '-v'], help='Version (tag). Default: latest stable.',
                   validator=labservices_source_version_validator)
        c.argument('prerelease', options_list=['--pre'], action='store_true',
                   help='Upgrade to the latest prerelease version.')
