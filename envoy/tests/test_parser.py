from datadog_checks.envoy.parser import reassemble_addresses


def test_reassemble_addresses():
    seq = ['0', '0', '0', '0_80', 'ingress_http']
    assert reassemble_addresses(seq) == ['0.0.0.0:80', 'ingress_http']


def test_reassemble_addresses_empty():
    assert reassemble_addresses([]) == []
