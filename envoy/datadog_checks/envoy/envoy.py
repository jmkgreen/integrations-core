# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.checks import AgentCheck


class Envoy(AgentCheck):
    metric_prefix = 'envoy.'

    def check(self, instance):
        pass
