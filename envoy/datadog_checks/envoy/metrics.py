from .utils import make_metric_tree

METRICS = {
    'runtime.load_error': {
        'tags': (),
        'method': 'count',
    },
    'runtime.override_dir_not_exists': {
        'tags': (),
        'method': 'count',
    },
    'runtime.override_dir_exists': {
        'tags': (),
        'method': 'count',
    },
    'runtime.load_success': {
        'tags': (),
        'method': 'count',
    },
    'runtime.num_keys': {
        'tags': (),
        'method': 'gauge',
    },
    '': {
        'tags': (),
        'method': '',
    },
}

METRIC_TREE = make_metric_tree(METRICS)
