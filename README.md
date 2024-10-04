# RESTPulse

## About
An automated HTTP REST API Health checker tool designed as part of the Fetch SRE challenge. This tool built in python, helps in assessing the health of server's HTTP REST API endpoints and keeps a realtime record of its availability. 

## Features
- This tool supports multithreading, by checking the health of API endpoints every 15 seconds parallelly, even if the yaml file is very big.
- This tool is unit tested using PyTest module with upto 500 threads running parallelly. 
- This tool has timeout enabled with 500 milliseconds as threshold to handle indefinite wait cases.

## Design
- The time buffer for successive requests is only 15 seconds, during which we need to complete health checks for all endpoints. 
- In the worst-case scenario, where each request takes approximately 500 ms (0.5 seconds) to respond, performing checks sequentially would limit us to 30 checks (15/0.5).
- To overcome this limitation, I have implemented multithreading, allowing all threads to run simultaneously without waiting for the previous request's response.

## Unit Test
- Since we cannot emulate a server that provides various responses under multiple conditions, I performed unit testing using Python's PyTest package with four distinct tests.  
- The initialization test ensures that the domains are correctly parsed from the endpoints and that an entry for each domain is created in the dictionary.
- The synchronization test module is similar to load test where I send 500 requests and check for synchronization.
- I found a mock server called httpbin.org, which returns specific error codes and timeouts based on the parameters passed in the request. It helps in simulating various scenarios. The error codes test ensures proper handling of various response status codes.
- The timeouts module ensures graceful handling of timeouts when the response is delayed more than 500 ms.

## Future works
- The number of HTTP requests can be reduced by delaying the next check for healthier APIs.
- The current implementation creates a new set of threads every 15 seconds and destroys them after collecting the availability of all endpoints. Instead, we could reuse the same set of threads to invoke the target function every 15 seconds. However, this approach is only efficient for very large YAML files and not for smaller ones, as the threads consume resources by sleeping for the entire 15 seconds.

## Setup 
Install Python and Pip

pip install requests==2.29.0

pip install PyYAML==6.0

pip install pytest==7.4.0

## Command
python api_tester.py --filepath FILEPATH
