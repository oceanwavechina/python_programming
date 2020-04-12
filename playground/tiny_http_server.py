#! coding:utf8

import socket
import StringIO

def parse_http(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split(' ')
    headers = dict(
        line.split(':', maxsplit=1) for line in headers
    )
    return method, path, protocol, headers, body

def process_response(response):
    return (
        'HTTP/1.1 200 OK\r\n'
        f'Content-Length: {len(response)}\r\n'
        'Content-Type: text/html\r\n'
        '\r\n'
        + response +
        '\r\n'
        )

def view(request):
    print(request)
    return """Hello, this is tiny http server"""

with socket.socket() as s:
    s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('localhost', 8000))
    s.listen(1)
    
    while True:
        try:
            conn, addr = s.accept()
            with conn:
                http_request = conn.recv(1024).decode('utf-8')
                request = parse_http(http_request)
                response = view(request)
                http_response = process_response(response)
                print(http_response)
                conn.sendall(http_response.encode('utf-8'))
                #conn.sendall('Hello World'.encode('utf-8'))
        except Exception as e:
            conn.close()