# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

from .generated.action import *  # noqa: F403

try:
    from .manual.action import *  # noqa: F403
except ImportError as e:
    if e.name.endswith('manual.action'):
        pass
    else:
        raise e
