import http.server as h                                         # иморт модулей
import socketserver as s
from os import environ
PORT = environ.get('PORT', "8080")


PORT = 8080                                                     # порт прослушки
Handler = h.SimpleHTTPServer                            # обработчик запросов, отдает
                                                                # статичный файл в текущей папке

with s.BaseHTTPServer(('', int(PORT)), Handler) as httpd:                 # описывает сервер
    print("serving at port", PORT)                              # отчет нормальной работы
    httpd.serve_forever()                                       # указзание работать постоянно
    h.send_response(200)
