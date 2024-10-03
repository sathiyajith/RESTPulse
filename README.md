# RESTPulse

## About
This is an automated HTTP REST API Health checker tool designed as part of Fetch SRE challenge.

## Features
- This tool supports multithreading, so that the endpoints are checked every 15 seconds parallelly, even if the yaml file is very big.
- This tool has timeout enabled with 500 milliseconds as threshold to handle unbounded waiting cases.

## How this tool can be improved
- Number of http requests can be reduced, the healthier api's next check can be delayed.
- CONNECT and TRACE HTTP methods are not supported.


## Setup
Install Python and Pip
pip install requests==2.29.0
pip install PyYAML==6.0

## Command
python api_tester.py --filepath FILEPATH


