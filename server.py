import http.server as h
import socketserver as s

PORT = 8080           #environ.get('PORT', '8080')              # порт прослушки
Handler = h.SimpleHTTPRequestHandler                            # обработчик запросов, отдает
                                                                # статичный файл в текущей папке
try:
  with s.TCPServer(("", PORT), Handler) as httpd:                 # описывает сервер
      print("serving at port", PORT)                              # отчет нормальной работы
      httpd.serve_forever()                                       # указзание работать постоянно
      #h.send_response(200)
except:
  print('Error!')





'''
from os import environ
from http.server import BaseHTTPRequestHandler,HTTPServer

class HttpProcessor(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('content-type','text/html')
    self.end_headers()
    self.wfile(index.html)#write("hello !")

PORT = environ.get('PORT', "8080")

# serv = HTTPServer(int(PORT),HttpProcessor)
# serv.serve_forever()

def run(server_class=HTTPServer, handler_class=HttpProcessor):
    server_address = ('', int(PORT))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
'''
