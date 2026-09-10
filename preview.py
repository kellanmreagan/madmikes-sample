#!/usr/bin/env python3
"""Local preview server. Serves .php pages as HTML so the site works in a browser."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 8877


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def guess_type(self, path):
        if str(path).lower().endswith(".php"):
            return "text/html; charset=utf-8"
        return super().guess_type(path)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    os.chdir(ROOT)
    httpd = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Mad Mike's preview: http://127.0.0.1:{PORT}/")
    httpd.serve_forever()
