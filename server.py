import http.server
import socketserver

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("executing do_GET")

        self.send_response(200)                         # 200 is code for success
        self.send_header("Content-type", "text/html")   # Standard Header
        self.end_headers()

        html_file = open('index.html','rb')             # Open the given file in read-mode in bytes format
        response = html_file.read()

        self.wfile.write(response)                      # Write the response
        html_file.close()


PORT = 8080
Handler = RequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


