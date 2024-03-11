from http.server import  HTTPServer, BaseHTTPRequestHandler

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_Get(self):
        self.send_response(200)
        self.send_header()