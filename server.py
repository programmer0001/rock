import http.server as h                                         # иморт модулей
import socketserver as s
from os import environ


PORT = environ.get('PORT', "8080")                                          # порт прослушки
Handler = h.SimpleHTTPRequestHandler                            # обработчик запросов, отдает
                                                                # статичный файл в текущей папке

with s.TCPServer(('', int(PORT)), Handler) as httpd:                 # описывает сервер
    print("serving at port", PORT)                              # отчет нормальной работы
    httpd.serve_forever()                                       # указзание работать постоянно
    h.send_response(200)
