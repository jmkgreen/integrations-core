# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

import mock
import pytest

from datadog_checks.envoy import Envoy

metrics = [
    'envoy.',
]

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE_DIR = os.path.join(HERE, 'fixtures')


class TestEnvoy:
    CHECK_NAME = 'envoy'

    CONFIG = {
        'init_config': {
            '': '',
        },
        'instances': [
            {
                '': '',
            },
        ],
    }
