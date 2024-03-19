import http.server
from http.server import  HTTPServer, BaseHTTPRequestHandler

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_Get(self):
        self.send_response(200)
        self.send_header()
        self.wfile.write(b"Hello World")

if __name__=="__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001) MyHandler)
    server.serve_forever()
