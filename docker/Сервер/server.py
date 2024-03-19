import http.server
import random

from prometheus_client import start_http_server
from prometheus_client import Counter

REQUESTS = Counter('hello_worlds_total', 'Hello World request.')
EXCEPTION = Counter('hello_world_exception_total', 'Exceptions serving Hello World. ')
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        with EXCEPTION.count_exceptions():
            if random.random() < 0.2:
                raise Exception
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()