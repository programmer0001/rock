from http.server import BaseHTTPRequestHandler as hand
from http.server import HTTPServer as hs                # import modules

PORT = 4000                                             # listening port

class myHandler(hand):
    def do_GET(self):
	self.path = "index.html"                        # path to necessary file

	f = open(self.path)                             # opening and reading file
	ff = f.read()

	self.send_response(200)                         # answer for browser
	self.send_header('Content-type','text/html')    # info about file
	self.end_headers()
	self.wfile.write(ff.encode())                   # send file


def run():
    server = hs(('', PORT), myHandler)                  # handling request
    print('Started server on port: ', PORT)             # message about server's work
    server.serve_forever()                              # non-stop working

run()
