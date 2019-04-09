#!/usr/bin/env python

import threading
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from subprocess import Popen, PIPE
import sys

DEFAULT_IP = '127.0.0.1'
DEFAULT_PORT = 8080
DEFAULT_EXIT = '/shutdown'
DEFAULT_FILE = './index.html'

class MyHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def send_ok_headers(self):
        self.send_response(200)                        
        self.send_header('Content-type','text-html')  
        self.end_headers() 
        
    def send_bye_message(self):
        self.wfile.write(bytes('bye','UTF-8'))
        
    def do_GET(self):
        if self.path == DEFAULT_EXIT:
            MyHandler.send_ok_headers(self)
            MyHandler.send_bye_message(self)
            self.server.running = False
        else:
            try:                
                f = open(DEFAULT_FILE, 'rb') #open requested file  
                MyHandler.send_ok_headers(self)
                self.wfile.write(bytes(f.read()))
                f.close()  
                return  

            except FileNotFoundError:  
                self.send_error(404, 'file not found')

class MainServer:
    def __init__(self, port = DEFAULT_PORT):
        try:
            self._server = HTTPServer((DEFAULT_IP, DEFAULT_PORT), MyHandler)
            self._thread = threading.Thread(target=self.run)
            self._thread.deamon = True 
        except OSError:
            sys.stderr.write('server may already be running')
            sys.exit(2)

    def run(self):
        self._server.running = True
        while self._server.running:
            self._server.handle_request()

    def start(self):
        self._thread.start()        

    def shut_down(self):
        self._thread.close()        

def main():
    if os.getpgrp() == os.tcgetpgrp(sys.stdout.fileno()):        
        print('running in foreground')
        # restarting as background process        
        p = Popen(['python', sys.argv[0], '&', '\n'], stdin=PIPE, shell=False)
            
    else:        
        print('running in background.')
        m = MainServer()
        m.start()

    return

if __name__ == '__main__':
    main()
