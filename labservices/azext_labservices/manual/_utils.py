# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import requests
from azure.cli.core.util import should_disable_connection_verify
from knack.log import get_logger
from knack.util import CLIError

logger = get_logger(__name__)


def get_github_release(repo='az-labservices', org='colbylwilliams', version=None, prerelease=False):

    if version and prerelease:
        raise CLIError(
            'usage error: can only use one of --version/-v | --pre')

    url = f'https://api.github.com/repos/{org}/{repo}/releases'

    if prerelease:
        version_res = requests.get(url, verify=not should_disable_connection_verify())
        version_json = version_res.json()

        version_prerelease = next((v for v in version_json if v['prerelease']), None)
        if not version_prerelease:
            raise CLIError(f'--pre no prerelease versions found for {org}/{repo}')

        return version_prerelease

    url += (f'/tags/{version}' if version else '/latest')

    version_res = requests.get(url, verify=not should_disable_connection_verify())

    if version_res.status_code == 404:
        raise CLIError(
            f'No release version exists for {org}/{repo}. '
            'Specify a specific prerelease version with --version '
            'or use latest prerelease with --pre')

    return version_res.json()


def github_release_version_exists(version, repo='az-labservices', org='colbylwilliams'):

    version_url = f'https://api.github.com/repos/{org}/{repo}/releases/tags/{version}'
    version_res = requests.get(version_url, verify=not should_disable_connection_verify())

    return version_res.status_code < 400


# def list_subscriptions(cmd, all=False, refresh=False, tenant_id=None, name_prefix=None):  # pylint: disable=redefined-builtin
#     """List the imported subscriptions."""
#     from azure.cli.core.api import load_subscriptions

#     subscriptions = load_subscriptions(cmd.cli_ctx, all_clouds=all, refresh=refresh)
#     if not subscriptions:
#         logger.warning('Please run "az login" to access your accounts.')
#     for sub in subscriptions:
#         sub['cloudName'] = sub.pop('environmentName', None)
#     if not all:
#         enabled_ones = [s for s in subscriptions if s.get('state') == 'Enabled']
#         if len(enabled_ones) != len(subscriptions):
#             logger.warning("A few accounts are skipped as they don't have 'Enabled' state. "
#                            "Use '--all' to display them.")
#             subscriptions = enabled_ones

#     if tenant_id:
#         subscriptions = [sub for sub in subscriptions if sub['tenantId'] == tenant_id]

#     if name_prefix:
#         subscriptions = [sub for sub in subscriptions if sub['name'].startswith(name_prefix)]

#     return subscriptions
