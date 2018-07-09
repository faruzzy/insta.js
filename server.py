from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import urllib2
from urllib2 import urlopen, URLError, HTTPError
import uuid

def dlfile(url):
    response = urllib2.urlopen(url)
    filename = str(uuid.uuid4()) + ".jpg"
    fh = open(filename, "w")
    fh.write(response.read())
    fh.close()

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        myurl = self.path
        #splits to colon
        myurl2 = myurl.split(':')
        str = ""
        for x in range(1, len(myurl2)):
            str = str + myurl2[x]
        #print(str)
        #splits to bracket
        myurl3 = str.split('}')
        dlfile(myurl3[0].replace("https//","https://"))
        #dlfile(myurl3[0])

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #dlfile(post_data)
        print post_data

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()