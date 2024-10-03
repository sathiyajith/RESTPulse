import pytest
from parser import parseYaml
import threading

@pytest.fixture
#This function just parses and returns list of domains without any check
def domains():
    filepath = "./inputs/sample_input_2.yaml"
    domains = parseYaml(filepath)
    assert len(domains.endpoints.keys())>0
    return domains

#This function tests initialization of dictionaries
def test_initialization(domains):
    assert len(domains.health.keys())>0
    assert len(domains.num_checks.keys())>0
    assert len(domains.num_checks.keys())==len(domains.health.keys())


# This function tests synchronization by creating 500 threads and concurrently accessing the shared variables
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
    
