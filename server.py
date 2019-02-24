from io import BufferedIOBase as iob
import http.server as h
import socketserver as s
from os import environ
from http.server import BaseHTTPRequestHandler,HTTPServer

ind = '''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div {
            font-size: 4em;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 90vh;
            width: 100%;
            color: forestgreen;
            font-family: Arial, Helvetica, sans-serif;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div>Hello, world!</div>

</body>
</html>'''

class HttpProcessor(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('content-type','text/html')
    self.end_headers()
    self.wfile.write(ind.encode())
    return

PORT = environ.get('PORT', "8029")

# serv = HTTPServer(int(PORT),HttpProcessor)
# serv.serve_forever()

def run(server_class=HTTPServer, handler_class=HttpProcessor):
    server_address = ('', int(PORT))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
