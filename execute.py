import requests

def runRequest(endpoint):
    url = endpoint.url
    header = endpoint.header
    method = endpoint.method
    body = endpoint.body
    if not method:
        response = requests.get(url, headers=header, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    elif method=="GET":
        response = requests.get(url, headers=header, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    elif method=="POST":
        response = requests.post(url, headers=header, json=body, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    elif method=="PATCH":
        response = requests.patch(url, headers=header, json=body, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    elif method=="DELETE":
        response = requests.delete(url, headers=header, json=body, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    elif method=="PUT":
        response = requests.put(url, headers = header, json=body, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    elif method=="HEAD":
        response = requests.head(url, headers = header, json=body, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    elif method=="OPTIONS":
        response = requests.options(url, headers = header, json=body, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    elif method=="CONNECT":
        response = requests.connect(url, headers = header, json=body, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    elif method=="TRACE":
        response = requests.trace(url, headers = header, json=body, timeout=0.5)
        latency = response.elapsed.total_seconds() * 1000
    return response.status_code, latency