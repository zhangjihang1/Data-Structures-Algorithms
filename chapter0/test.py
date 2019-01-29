from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    Page = '''\
            <html>
            <body>
            <p>hello, web!</p>
            </bosy>
            </html>
            '''

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))


if __name__ == '__main__':
    serverAddress = ('', 8000)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
