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
    'cluster_manager.cds.config_reload': {
        'tags': (),
        'method': 'count',
    },
    'cluster_manager.cds.update_attempt': {
        'tags': (),
        'method': 'count',
    },
    'cluster_manager.cds.update_success': {
        'tags': (),
        'method': 'count',
    },
    'cluster_manager.cds.update_failure': {
        'tags': (),
        'method': 'count',
    },
    'cluster_manager.cds.version': {
        'tags': (),
        'method': 'gauge',
    },
    'http.no_route': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'http.no_cluster': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'http.rq_redirect': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'http.rq_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'vhost.vcluster.upstream_rq_1xx': {
        'tags': ('virtual_host_name', 'virtual_cluster_name', ),
        'method': 'count',
    },
    'vhost.vcluster.upstream_rq_2xx': {
        'tags': ('virtual_host_name', 'virtual_cluster_name', ),
        'method': 'count',
    },
    'vhost.vcluster.upstream_rq_3xx': {
        'tags': ('virtual_host_name', 'virtual_cluster_name', ),
        'method': 'count',
    },
    'vhost.vcluster.upstream_rq_4xx': {
        'tags': ('virtual_host_name', 'virtual_cluster_name', ),
        'method': 'count',
    },
    'vhost.vcluster.upstream_rq_5xx': {
        'tags': ('virtual_host_name', 'virtual_cluster_name', ),
        'method': 'count',
    },
    'vhost.vcluster.upstream_rq_time': {
        'tags': ('virtual_host_name', 'virtual_cluster_name', ),
        'method': 'histogram',
    },
    'cluster.ratelimit.ok': {
        'tags': ('route_target_cluster', ),
        'method': 'count',
    },
    'cluster.ratelimit.error': {
        'tags': ('route_target_cluster', ),
        'method': 'count',
    },
    'cluster.ratelimit.over_limit': {
        'tags': ('route_target_cluster', ),
        'method': 'count',
    },
    'http.ip_tagging.hit': {
        'tags': ('stat_prefix', 'tag_name', ),
        'method': 'count',
    },
    'http.ip_tagging.no_hit': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'http.ip_tagging.total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'cluster.grpc.success': {
        'tags': ('route_target_cluster', 'grpc_service', 'grpc_method', ),
        'method': 'count',
    },
    'cluster.grpc.failure': {
        'tags': ('route_target_cluster', 'grpc_service', 'grpc_method', ),
        'method': 'count',
    },
    'cluster.grpc.total': {
        'tags': ('route_target_cluster', 'grpc_service', 'grpc_method', ),
        'method': 'count',
    },
    '': {
        'tags': (),
        'method': '',
    },
}

METRIC_TREE = make_metric_tree(METRICS)
