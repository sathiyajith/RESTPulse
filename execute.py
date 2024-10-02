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
    #print(response.status_code)
    return response.status_code, latency