# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

helps['labservices upgrade'] = """
type: command
short-summary: Upgrade labservices cli extension.
examples:
  - name: Upgrade labservices cli extension.
    text: az labservices upgrade
  - name: Upgrade labservices cli extension to the latest pre-release.
    text: az labservices upgrade --pre
"""
