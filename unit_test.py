import pytest
from parser import parseYaml
from domains import Domains, Endpoint
import threading

@pytest.fixture
# Parses and returns the list of domains without any checks
def domains():
    filepath = "./inputs/sample_input_2.yaml"
    domains = parseYaml(filepath)
    assert len(domains.endpoints.keys())>0
    return domains

# Tests initialization of dictionaries
def test_initialization(domains):
    assert len(domains.health.keys())>0
    assert len(domains.num_checks.keys())>0
    assert len(domains.num_checks.keys())==len(domains.health.keys())


# Tests synchronization by creating 500 threads and concurrently accessing the shared variables
# Once all the threads call the target function, the dictionary values are checked for consistency.
def test_synchronization(domains):
    threads = []
    for domain in domains.endpoints:
        for _ in range(500):
            for endpoint in domains.endpoints[domain]:
                thread = threading.Thread(target=domains.runRequest, args=(domain, endpoint,))
                threads.append(thread)
                thread.start()
    for thread in threads:
        thread.join()
    for domain in domains.endpoints:
        assert domains.health[domain]==1000
        assert domains.num_checks[domain]==1000

# For each 100 range of error codes, it test an endpoint to make sure all the ranges are covered.
def test_error_codes():
    filepath = "./inputs/sample_input_4.yaml"
    sample_domain = "httpbin.org"
    domains = parseYaml(filepath)
    domains.checkHealth()
    assert domains.health[sample_domain]==1
    assert domains.num_checks[sample_domain]==8

# Tests whether the tool can handle timeouts and infinite waits.
def test_timeouts():
    filepath = "./inputs/sample_input_3.yaml"
    sample_domain = "httpbin.org"
    domains = parseYaml(filepath)
    domains.checkHealth()
    assert domains.health[sample_domain]==0
    assert domains.num_checks[sample_domain]==3