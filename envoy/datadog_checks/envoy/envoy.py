# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.checks import AgentCheck

EVENT_TYPE = SOURCE_TYPE_NAME = 'envoy'


class Envoy(AgentCheck):
    metric_prefix = 'envoy.'

    def __init__(self, name, init_config, agent_config, instances):
        super(Envoy, self).__init__(self, name, init_config, agent_config, instances)

    def check(self, instance):
        pass
