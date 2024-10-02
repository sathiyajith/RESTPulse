import argparse
import os
from parser import parseYaml
import time
    

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Tests API health")
    arg_parser.add_argument("--filepath", help="Absolute file path", default="")
    args = arg_parser.parse_args()
    if args.filepath and os.path.exists(args.filepath) and os.path.isfile(args.filepath):
        if args.filepath.lower().endswith(('.yaml', '.yml')):
            domains = parseYaml(args.filepath)
            while True:
                domains.checkHealth()
                domains.printStatus()
                time.sleep(15)
        else:
            print("Please enter a valid YAML file's absolute path")
    else:
        print("Please enter a valid YAML file's absolute path")
    
