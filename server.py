import http.server as h                                         # иморт модулей
import socketserver as s

PORT = 8070                                                     # порт прослушки
Handler = h.SimpleHTTPRequestHandler                            # обработчик запросов, отдает
                                                                # статичный файл в текущей папке

with s.TCPServer(("", PORT), Handler) as httpd:                 # описывает сервер
    print("serving at port", PORT)                              # отчет нормальной работы
    httpd.serve_forever()                                       # указзание работать постоянно
    h.send_response(200)
