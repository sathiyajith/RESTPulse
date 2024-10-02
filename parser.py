import yaml
from domains import Endpoint, Domains

def parseYaml(filepath):
    with open(filepath, "r") as file:
        data = yaml.safe_load(file)
    domains = Domains()
    for endpoint in data:
        name = endpoint.get("name")
        url = endpoint.get("url")
        header = endpoint.get("headers")
        method = endpoint.get("method")
        body = endpoint.get("body")
        if name and url:
            if not method:
                method = "GET"
            endpoint = Endpoint(name, url, method, header, body)
            domains.addEndpoint(endpoint)
    return domains