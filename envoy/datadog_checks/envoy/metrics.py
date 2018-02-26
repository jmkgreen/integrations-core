from .utils import make_metric_tree

METRICS = {
    '': {
        'method': '',
        'fields': (),
    },
}

METRIC_TREE = make_metric_tree(METRICS)
