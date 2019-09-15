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
    m = hashlib.md5()
    buffersize = 2**20
    with open(filename, "rb") as f:        
        buffer = f.read(buffersize)
        while buffer:
            m.update(buffer)
            buffer = f.read(buffersize)            
    print(m.hexdigest())
        
try:
    inputfile, size = get_parameters(parsed_arguments())
    do_hash(inputfile, size)
except Exception as caught:
    print(type(caught).__name__, caught.args)

