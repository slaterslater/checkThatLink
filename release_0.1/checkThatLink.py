#!/usr/bin/env python3

import argparse
from src.checkFile import checkFile

if __name__ =="__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument(
        'file',
        help="file that contains links to check"
    )
    argParser.add_argument(
        '-v','--version',
        action='version',
        version='%(prog)s 0.1'
    )
    argParser.add_argument(
        '-s', '--secureHttp', 
        dest='secureHttp',
        action='store_true',
        help="flag to check if https works on http links",
        required=False
    )
    argParser.add_argument(
        '-j', '--json',
        dest='json', 
        action='store_true',
        help="display output as JSON",
        required=False
    )
    argParser.add_argument(
        '-a', '--all',  
        action='store_true',
        help="Flag to display all links (defualt behaviour)",
        required=False
    )
    argParser.add_argument(
        '-g', '--good',  
        action='store_true',
        help="Flag to display only good links",
        required=False
    )
    argParser.add_argument(
        '-b', '--bad',  
        action='store_true',
        help="Flag to display only bad links",
        required=False
    )
    args = argParser.parse_args()

    checkFile(args) 
