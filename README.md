# RESTPulse

## About
An automated HTTP REST API Health checker tool designed as part of the Fetch SRE challenge. This tool built in python, helps in assessing the health of server's HTTP REST API endpoints and keeps a realtime record of its availability. 

## Features
- This tool supports multithreading, by checking the health of API endpoints every 15 seconds parallelly, even if the yaml file is very big.
- This tool is unit tested using PyTest module with upto 500 threads running parallelly. 
- This tool has timeout enabled with 500 milliseconds as threshold to handle indefinite wait cases.

## Unit Test
- Since we cannot emulate a server that provides various responses under multiple conditions, I performed unit testing using Python's PyTest package with four distinct tests.  
- The initialization test ensures that the domains are correctly parsed from the endpoints and that an entry for each domain is created in the dictionary.
- The synchronization test module is similar to load test where I send 500 requests and check for synchronization.
- I found a mock server called httpbin.org, which returns specific error codes and timeouts based on the parameters passed in the request. It helps in simulating various scenarios. The error codes test ensures proper handling of various response status codes.
- The timeouts module ensures graceful handling of timeouts when the response is delayed more than 500 ms.

## Future works
- The number of HTTP requests can be reduced by delaying the next check for healthier APIs.
- This current implementation creates new set of threads every 15 seconds and destroys them after collecting the availability of all endpoints. Instead we can reuse the same set of threads to call the target function every 15 seconds. But this implementation is not efficient for smaller YAML files, since the thread utilizes resources by waiting for the entire 15 seconds.

## Setup 
Install Python and Pip
pip install requests==2.29.0
pip install PyYAML==6.0
pip install pytest==7.4.0

## Command
python api_tester.py --filepath FILEPATH
