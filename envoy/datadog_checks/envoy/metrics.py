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
    'http.dynamodb.operation.upstream_rq_total': {
        'tags': ('stat_prefix', 'operation_name', ),
        'method': 'count',
    },
    'http.dynamodb.operation.upstream_rq_time': {
        'tags': ('stat_prefix', 'operation_name', ),
        'method': 'histogram',
    },
    'http.dynamodb.table.upstream_rq_total': {
        'tags': ('stat_prefix', 'table_name', ),
        'method': 'count',
    },
    'http.dynamodb.table.upstream_rq_time': {
        'tags': ('stat_prefix', 'table_name', ),
        'method': 'histogram',
    },
    'http.dynamodb.error': {
        'tags': ('stat_prefix', 'table_name', 'error_type', ),
        'method': 'count',
    },
    'http.dynamodb.error.BatchFailureUnprocessedKeys': {
        'tags': ('stat_prefix', 'table_name', ),
        'method': 'count',
    },
    'http.buffer.rq_timeout': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'http.rds.config_reload': {
        'tags': ('stat_prefix', 'route_config_name', ),
        'method': 'count',
    },
    'http.rds.update_attempt': {
        'tags': ('stat_prefix', 'route_config_name', ),
        'method': 'count',
    },
    'http.rds.update_success': {
        'tags': ('stat_prefix', 'route_config_name', ),
        'method': 'count',
    },
    'http.rds.update_failure': {
        'tags': ('stat_prefix', 'route_config_name', ),
        'method': 'count',
    },
    'http.rds.version': {
        'tags': ('stat_prefix', 'route_config_name', ),
        'method': 'gauge',
    },
    'tcp.downstream_cx_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'tcp.downstream_cx_no_route': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'tcp.downstream_cx_tx_bytes_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'tcp.downstream_cx_tx_bytes_buffered': {
        'tags': ('stat_prefix', ),
        'method': 'gauge',
    },
    'tcp.downstream_flow_control_paused_reading_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'tcp.downstream_flow_control_resumed_reading_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'auth.clientssl.update_success': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'auth.clientssl.update_failure': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'auth.clientssl.auth_no_ssl': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'auth.clientssl.auth_ip_white_list': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'auth.clientssl.auth_digest_match': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'auth.clientssl.auth_digest_no_match': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'auth.clientssl.total_principals': {
        'tags': ('stat_prefix', ),
        'method': 'gauge',
    },
    '': {
        'tags': (),
        'method': '',
    },
}

METRIC_TREE = make_metric_tree(METRICS)
