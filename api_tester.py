import argparse
import os
from parser import parseYaml
import time
    

if __name__ == "__main__":
    # The arg_parser parses the command line arguments and checks if the provided filepath is valid and is an yaml file.
    arg_parser = argparse.ArgumentParser(description="Tests API health")
    arg_parser.add_argument("--filepath", help="Absolute file path", default="")
    args = arg_parser.parse_args()
    if args.filepath and os.path.exists(args.filepath) and os.path.isfile(args.filepath):
        if args.filepath.lower().endswith(('.yaml', '.yml')):
            # The parseYaml defined in parser.py parses the YAML file and returns the list of endpoints and domains
            domains = parseYaml(args.filepath)
            while True:
                # The domains health is checked and its status is printed every 15 seconds until the user presses CTRL+C
                domains.checkHealth()
                domains.printStatus()
                time.sleep(15)
        else:
            print("Please enter a valid YAML file's absolute path")
    else:
        print("Please enter a valid YAML file's absolute path")
    
