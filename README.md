# RESTPulse

## About
An automated HTTP REST API Health checker tool designed as part of Fetch SRE challenge. This tool built in python, helps in assessing the health of server's HTTP REST API endpoints and keeps a realtime record of its availability. 

## Features
- This tool supports multithreading, so that the endpoints are checked every 15 seconds parallelly, even if the yaml file is very big.
- This tool is unit tested using PyTest module with upto 500 threads running parallelly. 
- This tool has timeout enabled with 500 milliseconds as threshold to handle indefinite wait cases.

## Unit Test
- Since we cannot emulate a server that provides various responses and under different conditions, I performed unit testing using Python's PyTest package with 4 different tests. 
- The first test checks for proper initialization.
- The second test is kind of like load test where I send 500 requests and check for synchronization.
- The third test ensures handling of different status codes.
- The fourth test ensures handling of timeouts.

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
