from datadog_checks.envoy.metrics import METRICS, METRIC_TREE
from datadog_checks.envoy.utils import make_metric_tree


def test_metric_tree():
    assert METRIC_TREE == make_metric_tree(METRICS)
