from urllib.parse import urlparse
import threading
import requests
        

class Domains:
    def __init__(self):
        self.endpoints = {}
        self.health = {}
        self.num_checks = {}
        self.lock = threading.Lock()
    
    def addEndpoint(self, endpoint):
        parsed_url = urlparse(endpoint.url)
        domain = parsed_url.netloc
        if domain in self.endpoints:    
            self.endpoints[domain].append(endpoint)
        else:
            self.endpoints[domain] = [endpoint]
        if domain not in self.health:
            self.health[domain] = 0
            self.num_checks[domain] = 0
        
    def printStatus(self):
        with self.lock:
            for domain in self.endpoints:
                health_percent = int((self.health[domain]/self.num_checks[domain])*100)
                print(domain + " has " + str(health_percent) + "% availability percentage")
    
    def checkHealth(self):
        threads = []
        for domain in self.endpoints:
            for endpoint in self.endpoints[domain]:
                thread = threading.Thread(target=self.check, args=(domain, endpoint,))
                threads.append(thread)
                thread.start()
        
        for thread in threads:
            thread.join()

    def check(self, domain, endpoint):
        with self.lock:
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
                print(type(body))
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
            if response.status_code>=200 and response.status_code<=299 and latency<500:
                self.health[domain]+=1
            self.num_checks[domain]+=1


class Endpoint:
    def __init__(self, name, url, method, header, body):
        self.name = name
        self.availability = 0
        self.url = url
        self.method = method
        self.header = header
        self.body = body
    
    