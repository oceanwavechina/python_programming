#! coding:utf8

import socket

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

def to_environ(method, path, protocol, headers, body):
    return {
    'REQUEST_METHOD': method,
    'PATH_INFO':path, 
    'SERVER_PROTOCOL':protocol,
    }

def start_response(status, headers):
    conn.sendall(f'HTTP/1.1 {status}\r\n'.encode('utf-8'))
    for (key, value) in headers:
        conn.sendall(f'{key}: {value}\r\n'.encode('utf-8'))
    conn.sendall('\r\n'.encode('utf-8'))


"""
    下边这个applicaitin实现wsgi portable的关键，所有的框架都在这个体系下实现
"""
def application(start_response, environ):
    response = view(environ)
    start_response('200 OK', [
        ('Content-Length', len(response))
    ])
    return [response]

def view(environ):
    path = environ['PATH_INFO']
    print(request)
    return f'Hello from {path}, this is tiny http server that compitable with wsgi'


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
                environ = to_environ(*request)
                response = application(start_response, environ)
                print(response)
                for data in response:
                    conn.sendall(data.encode('utf-8'))
        except Exception as e:
            raise e
            print(repr(e))
            conn.close()