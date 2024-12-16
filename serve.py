import http.server
import socketserver

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        httpd.server_close()
        print("Server closed successfully.")
