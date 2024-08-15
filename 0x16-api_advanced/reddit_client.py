#!/usr/bin/python3
import http.server
import socketserver
from auth import get_subscribers, get_top_ten

PORT = 5000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/subscribers/"):
            subreddit = self.path.split("/")[2]
            response = get_subscribers(subreddit)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f"Number of subscribers in {subreddit}: {response}".encode())
        elif self.path.startswith("/top_ten/"):
            subreddit = self.path.split("/")[2]
            response = get_top_ten(subreddit)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f"Top 10 hot posts in {subreddit}:<br>" + "<br>".join(response).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

