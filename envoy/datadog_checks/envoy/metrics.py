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
    'ratelimit.total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'ratelimit.error': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'ratelimit.over_limit': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'ratelimit.ok': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'ratelimit.cx_closed': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'ratelimit.active': {
        'tags': ('stat_prefix', ),
        'method': 'gauge',
    },
    'redis.downstream_cx_active': {
        'tags': ('stat_prefix', ),
        'method': 'gauge',
    },
    'redis.downstream_cx_protocol_error': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'redis.downstream_cx_rx_bytes_buffered': {
        'tags': ('stat_prefix', ),
        'method': 'gauge',
    },
    'redis.downstream_cx_rx_bytes_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'redis.downstream_cx_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'redis.downstream_cx_tx_bytes_buffered': {
        'tags': ('stat_prefix', ),
        'method': 'gauge',
    },
    'redis.downstream_cx_tx_bytes_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'redis.downstream_cx_drain_close': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'redis.downstream_rq_active': {
        'tags': ('stat_prefix', ),
        'method': 'gauge',
    },
    'redis.downstream_rq_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'redis.splitter.invalid_request': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'redis.splitter.unsupported_command': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'redis.command.total': {
        'tags': ('stat_prefix', 'command', ),
        'method': 'count',
    },
    'mongo.decoding_error': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.delay_injected': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_get_more': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_insert': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_kill_cursors': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_query': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_query_tailable_cursor': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_query_no_cursor_timeout': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_query_await_data': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_query_exhaust': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_query_no_max_time': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_query_scatter_get': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_query_multi_get': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_query_active': {
        'tags': ('stat_prefix', ),
        'method': 'gauge',
    },
    'mongo.op_reply': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_reply_cursor_not_found': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_reply_query_failure': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.op_reply_valid_cursor': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.cx_destroy_local_with_active_rq': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.cx_destroy_remote_with_active_rq': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.cx_drain_close': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'mongo.cmd.total': {
        'tags': ('stat_prefix', 'cmd', ),
        'method': 'count',
    },
    'mongo.cmd.reply_num_docs': {
        'tags': ('stat_prefix', 'cmd', ),
        'method': 'histogram',
    },
    'mongo.cmd.reply_size': {
        'tags': ('stat_prefix', 'cmd', ),
        'method': 'histogram',
    },
    'mongo.cmd.reply_time_ms': {
        'tags': ('stat_prefix', 'cmd', ),
        'method': 'histogram',
    },
    'mongo.collection.query.total': {
        'tags': ('stat_prefix', 'collection', ),
        'method': 'count',
    },
    'mongo.collection.query.scatter_get': {
        'tags': ('stat_prefix', 'collection', ),
        'method': 'count',
    },
    'mongo.collection.query.multi_get': {
        'tags': ('stat_prefix', 'collection', ),
        'method': 'count',
    },
    'mongo.collection.query.reply_num_docs': {
        'tags': ('stat_prefix', 'collection', ),
        'method': 'histogram',
    },
    'mongo.collection.query.reply_size': {
        'tags': ('stat_prefix', 'collection', ),
        'method': 'histogram',
    },
    'mongo.collection.query.reply_time_ms': {
        'tags': ('stat_prefix', 'collection', ),
        'method': 'histogram',
    },
    'mongo.collection.callsite.query.total': {
        'tags': ('stat_prefix', 'collection', 'callsite', ),
        'method': 'count',
    },
    'mongo.collection.callsite.query.scatter_get': {
        'tags': ('stat_prefix', 'collection', 'callsite', ),
        'method': 'count',
    },
    'mongo.collection.callsite.query.multi_get': {
        'tags': ('stat_prefix', 'collection', 'callsite', ),
        'method': 'count',
    },
    'mongo.collection.callsite.query.reply_num_docs': {
        'tags': ('stat_prefix', 'collection', 'callsite', ),
        'method': 'histogram',
    },
    'mongo.collection.callsite.query.reply_size': {
        'tags': ('stat_prefix', 'collection', 'callsite', ),
        'method': 'histogram',
    },
    'mongo.collection.callsite.query.reply_time_ms': {
        'tags': ('stat_prefix', 'collection', 'callsite', ),
        'method': 'histogram',
    },
    '': {
        'tags': (),
        'method': '',
    },
}

METRIC_TREE = make_metric_tree(METRICS)
