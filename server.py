from http.server import BaseHTTPRequestHandler as hand
from http.server import HTTPServer as hs                # import modules

PORT = 4000                                             # listening port

ind = '''
<html lang="en">
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
</html>
'''

class myHandler(hand):
   	def do_GET(self):
		#self.path = "index.html"                        # path to necessary file

		#f = open(self.path)                             # opening and reading file
		#ff = f.read()

		self.send_response(200)                         # answer for browser
		self.send_header('Content-type','text/html')    # info about file
		self.end_headers()
		self.wfile.write(ind.encode())                   # send file


def run():
    server = hs(('', PORT), myHandler)                  # handling request
    print('Started server on port: ', PORT)             # message about server's work
    server.serve_forever()                              # non-stop working

run()
