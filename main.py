#!/usr/bin/python
import time
import os
import BaseHTTPServer
from pprint import pprint

HOST_NAME = '0.0.0.0'
PORT_NUMBER = os.environ.get('PORT', 8000)


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_HEAD(s):
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
                s.print_request()

        def do_GET(s):
                s.handle_request("GET")
                s.print_request()
        
        def do_POST(s):
                s.handle_request("POST")
                s.print_request()

        def handle_request(s, method):
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
                s.wfile.write("<html><head><title>Title</title></head>")
                s.wfile.write("<body><p>hello</p>")
                s.wfile.write("<p>%s: You accessed path: %s</p>" % method, s.path)
                s.wfile.write("</body></html>")     

        def print_request(s):
                print "GET", s.client_address[0], ":", s.client_address[1], " ", s.path, " "
                pprint (vars(s.connection))
                """
                pprint (vars(s.request))
                pprint (vars(s))
                pprint (vars(s.connection))
                pprint (vars(s.headers))
                pprint (vars(s.request))
                pprint (vars(s.rfile))
                pprint (vars(s.server))
                pprint (vars(s.wfile))
                pprint (vars(s.fp))

                pprint (vars(s.request))
                """


if __name__ == '__main__':
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
        print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                pass
        httpd.server_close()
        print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)