from http.server import BaseHTTPRequestHandler as hand
from http.server import HTTPServer as hs                      # import modules
from os import environ

PORT = environ.get('PORT', "4002")                            # listening port

class myHandler(hand):                                        # class for handling requests
	def do_GET(self):
		self.send_response(200)                       # answer for browser
		self.send_header('Content-type','text/html')  # info about file
		self.end_headers()

		self.path = "/build/index.html"                      # path to necessary file
		f = open(self.path)                           # opening and reading file
		ff = f.read()
		self.wfile.write(ff.encode())                 # send file
		return

def run(server_class = hs, handler_class = myHandler):
	server_address = ('', int(PORT))
	httpd = server_class(server_address, handler_class)   # handling request
	print('Started server on port: ', PORT)               # message about server's work
	httpd.serve_forever()                                 # non-stop working

run()
