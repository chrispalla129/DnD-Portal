import http.server
import socketserver


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """Custom handler to be tested"""
    def do_GET(self):
        # print just to confirm that this method is being called
        print("executing do_GET") # just to confirm...

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Here's where all the complicated logic is done to generate HTML.
        # For clarity here, replace with a simple stand-in:
        html_file = open('index.html','rb')
        response = html_file.read()

        self.wfile.write(response)
        html_file.close()


PORT = 8080
Handler = RequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


