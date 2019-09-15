#!/usr/bin/env python

__author__ = "Alfred Aquino"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Alfred Aquino"
__email__ = "onequbit@yahoo.com"

import argparse, hashlib, io, os, sys

def parsed_arguments():
    parser = argparse.ArgumentParser(description='compute md5 hash of a file')
    parser.add_argument('-f', dest='infile', type=str, required=True, help="file to hash")
    return parser.parse_args()

def get_parameters(args):    
    inputfile = args.infile
    assert (os.path.isfile(inputfile) is True), f'unable to open "{inputfile}"'
    size = os.path.getsize(inputfile)    
    return inputfile, size

def do_hash(filename, size):
    sys.stdin = sys.stdin.detach()
    md5 = hashlib.md5()
    buffer = bytearray(size)
    memview = memoryview(buffer)
    with open(filename, 'rb', buffering=1) as f:        
        for block in iter(lambda: f.readinto(memview)):
            md5.update(memview[:block])        
    print(md5.hexdigest())
        
try:
    inputfile, size = get_parameters(parsed_arguments())
    do_hash(inputfile, size)
except Exception as caught:
    print(type(caught).__name__, caught.args)

