from execute import runRequest
from urllib.parse import urlparse
        

class Domains:
    def __init__(self):
        self.endpoints = {}
        self.health = {}
        self.num_checks = {}
    
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
        for domain in self.endpoints:
            health_percent = int((self.health[domain]/self.num_checks[domain])*100)
            print(domain + " has " + str(health_percent) + "% availability percentage")
    
    def checkHealth(self):
        for domain in self.endpoints:
            for endpoint in self.endpoints[domain]:
                response, latency = runRequest(endpoint)
                if response>=200 and response<=299 and latency<500:
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
    
    