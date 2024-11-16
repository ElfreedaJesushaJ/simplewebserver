from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body>
        <h1 align="center">Device specifications</h1>
        <h2 align="center">J Elfreeda Jesusha</h2>
        <h3 align="center">24900146</h3>
        <ol type="I" start="1">
            <li>Device name:DESKTOP-7MAJ1KU</li>
            <li>Processor:13th Gen Intel(R) Core(TM) i7-1360P   2.20 GHz</li>
            <li>Installed RAM:16.0 GB (15.7 GB usable) </li>
            <li>Device ID:8A6A1ACD-1799-4660-9056-219ABE8B3B04</li>
            <li>Product ID:00342-42687-00372-AAOEM</li>
            <li>System type:64-bit operating system, x64-based processor</li>
            <li>Pen and Touch:No pen or touch input is available for this display</li>

        </ol>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()