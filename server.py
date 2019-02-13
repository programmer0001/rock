import http.server as h
import socketserver as s
from os import environ
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class HttpProcessor(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('content-type','text/html')
    self.end_headers()
    self.wfile.write("hello !")

PORT = environ.get('PORT', "8080")

serv = HTTPServer(int(PORT),HttpProcessor)
serv.serve_forever()
