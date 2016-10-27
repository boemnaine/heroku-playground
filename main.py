#!/usr/bin/python
import time
import os
import BaseHTTPServer
from pprint import pprint

HOST_NAME = '0.0.0.0'
PORT_NUMBER = int(os.environ.get('PORT', "8000"))


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
        
                s.wfile.write("<html><head>")
                s.wfile.write(s.get_meta_tag(charset="UTF-8"))
                s.wfile.write(s.get_meta_tag(content="Hello World!", property="og:title"))
                s.wfile.write(s.get_meta_tag(content="Sample Site", property="og:site_name"))
                s.wfile.write(s.get_meta_tag(content="Description", property="og:description"))
                s.wfile.write(s.get_meta_tag(content="https://ngnx-.herokuapp.com/", property="og:url"))
                s.wfile.write(s.get_meta_tag(content="https://s-media-cache-ak0.pinimg.com/originals/eb/4a/4d/eb4a4d61d98913135097fc05bf2b5435.jpg", property="og:image"))
                s.wfile.write("<title>Title</title></head>")

                s.wfile.write("<body><p>hello</p>")
                s.wfile.write("<p>%s: You accessed path: %s</p>" % (method, s.path))
                s.wfile.write("</body></html>")     

        def get_meta_tag(s, **kwargs):
                s = "<meta "
                for key, value in kwargs.items():
                        s += '{0}="{1}" '.format(key, value)
                s += ">\n"
                return s

        def print_request(s):
                print "GET", s.client_address[0], ":", s.client_address[1], " ", s.path, " "


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
