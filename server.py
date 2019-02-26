from http.server import BaseHTTPRequestHandler as hand
from http.server import HTTPServer as hs            # import modules
from os import curdir, sep

PORT_NUMBER = 8080                                  # listening port

class myHandler(hand):                              # class for handling requests
	def do_GET(self):
		self.path = "index.html"                    # path to necessary file

		f = open(self.path)                         # opening and reading file
		ff = f.read()

		self.send_response(200)                     # answer for browser
		self.send_header('Content-type','text/html')# info about file
		self.end_headers()
		self.wfile.write(ff.encode())               # send file


def run():
	server = hs(('', PORT_NUMBER), myHandler)       # handling request
	print('Started server on port: ', PORT_NUMBER)  # message about server's work
	server.serve_forever()                          # non-stop working

run()
