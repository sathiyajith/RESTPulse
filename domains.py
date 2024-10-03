from urllib.parse import urlparse
import threading
import requests
import json
from requests.exceptions import ReadTimeout, ConnectionError

class Domains:

    # The Domains class contains:
    # A dictionary to store the list of endpoints,
    # A dictionary to store Number of requests sent for each domain 
    # A dictionary to store current availability of an domain.
    # The TIMEOUT_FLAG is used for acknowledging any timeout or connection errors or exceptions.
    def __init__(self):
        self.endpoints = {}
        self.health = {}
        self.num_checks = {}
        self.lock = threading.Lock()
        self.TIMEOUT_FLAG = False
    
    # Parsing the endpoint to get domain and initializing the dictionaries with domain entries
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
        
    # Calculates current availability percentage and prints this status for each domain
    def printStatus(self):
        with self.lock:
            for domain in self.endpoints:
                health_percent = int((self.health[domain]/self.num_checks[domain])*100)
                print(domain + " has " + str(health_percent) + "% availability percentage")
    
    # Starts a thread for each endpoint and calls runRequest(). Then thread.join() is called for synchronization. 
    def checkHealth(self):
        threads = []
        for domain in self.endpoints:
            for endpoint in self.endpoints[domain]:
                thread = threading.Thread(target=self.runRequest, args=(domain, endpoint,))
                threads.append(thread)
                thread.start()
        
        for thread in threads:
            thread.join()

    # runRequest sends an request to the corresponding endpoint and collects response
    # The request waits only for 500ms beyond which ReadTimeout exception is triggered.
    # This exception ensures that the client doesn't wait indefinitely for the response. 
    # Based on the latency and status code, the availability is incremented.  
    def runRequest(self, domain, endpoint):
        with self.lock:
            url = endpoint.url
            header = endpoint.header
            method = endpoint.method
            body = endpoint.body
            if endpoint.body:
                body = json.loads(endpoint.body)
            else:
                body = {}
            if not method or method=="GET":
                try:
                    response = requests.get(url, headers=header, timeout=0.5)
                    latency = response.elapsed.total_seconds() * 1000
                except (ReadTimeout, ConnectionError, Exception) as e:
                    self.TIMEOUT_FLAG = True
            elif method=="POST":
                try:
                    response = requests.post(url, headers=header, json=body, timeout=0.5)
                    latency = response.elapsed.total_seconds() * 1000
                except (ReadTimeout, ConnectionError, Exception) as e:
                    self.TIMEOUT_FLAG = True
            elif method=="PATCH":
                try:
                    response = requests.patch(url, headers=header, json=body, timeout=0.5)
                    latency = response.elapsed.total_seconds() * 1000
                except (ReadTimeout, ConnectionError, Exception) as e:
                    self.TIMEOUT_FLAG = True
            elif method=="DELETE":
                try:
                    response = requests.delete(url, headers=header, json=body, timeout=0.5)
                    latency = response.elapsed.total_seconds() * 1000
                except (ReadTimeout, ConnectionError, Exception) as e:
                    self.TIMEOUT_FLAG = True
            elif method=="PUT":
                try:
                    response = requests.put(url, headers = header, json=body, timeout=0.5)
                    latency = response.elapsed.total_seconds() * 1000
                except (ReadTimeout, ConnectionError, Exception) as e:
                    self.TIMEOUT_FLAG = True
            elif method=="HEAD":
                try:
                    response = requests.head(url, headers = header, json=body, timeout=0.5)
                    latency = response.elapsed.total_seconds() * 1000
                except (ReadTimeout, ConnectionError, Exception) as e:
                    self.TIMEOUT_FLAG = True
            elif method=="OPTIONS":
                try:
                    response = requests.options(url, headers = header, json=body, timeout=0.5)
                    latency = response.elapsed.total_seconds() * 1000
                except (ReadTimeout, ConnectionError, Exception) as e:
                    self.TIMEOUT_FLAG = True
            if not self.TIMEOUT_FLAG and response.status_code>=200 and response.status_code<=299 and latency<500:
                self.health[domain]+=1
            self.num_checks[domain]+=1


class Endpoint:

    # The endpoint consists of the elements present in the schema required for sending a HTTP request
    def __init__(self, name, url, method, header, body):
        self.name = name
        self.url = url
        self.method = method
        self.header = header
        self.body = body
    
    