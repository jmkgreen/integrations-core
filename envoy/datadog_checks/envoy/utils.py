from collections import defaultdict

METRIC_PREFIX = 'envoy.'


def tree():
    return defaultdict(tree)


def make_metric_tree(metrics):
    metric_tree = tree()

    for metric in metrics:
        parts = metric.split('.')
        mapping = metric_tree

        # We'll create keys as they are referenced. See:
        # https://en.wikipedia.org/wiki/Autovivification
        for part in parts:
            mapping = mapping[part]

    return metric_tree
