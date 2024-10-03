import pytest
from parser import parseYaml
import threading

@pytest.fixture
def domains():
    filepath = "./inputs/sample_input_2.yaml"
    domains = parseYaml(filepath)
    assert len(domains.endpoints.keys())>0
    return domains

def test_initialization(domains):
    assert len(domains.health.keys())>0
    assert len(domains.num_checks.keys())>0
    assert len(domains.num_checks.keys())==len(domains.health.keys())


def test_synchronization(domains):
    threads = []
    for domain in domains.endpoints:
        for _ in range(100):
            for endpoint in domains.endpoints[domain]:
                thread = threading.Thread(target=domains.runRequest, args=(domain, endpoint,))
                threads.append(thread)
                thread.start()
    for thread in threads:
        thread.join()
    for domain in domains.endpoints:
        assert domains.health[domain]==100
    
