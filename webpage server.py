from http.server import BaseHTTPRequestHandler, HTTPServer

file = open("server.txt" , "r+")

whole_text = ""

#Create class that prints the file in a webserver
class CMUQEdgeServer(BaseHTTPRequestHandler):
    def make_content(self):
        whole_text = ""
        file.seek(0)
        for line in file:
            whole_text += line

        print(whole_text)
        return whole_text

    def do_GET(self):
        file = open("server.txt" , "r+")

        page_html = self.make_content()

        print(whole_text)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(page_html.encode())

myserver = HTTPServer(("0.0.0.0", 9039),CMUQEdgeServer)
myserver.serve_forever()



