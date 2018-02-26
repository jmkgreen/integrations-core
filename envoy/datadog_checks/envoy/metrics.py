from .utils import make_metric_tree

METRICS = {
    '': {
        'tags': (),
        'method': '',
    },
}

METRIC_TREE = make_metric_tree(METRICS)
