from http.server import BaseHTTPRequestHandler, HTTPServer

#Open file
file = open("server.txt" , "r+")

whole_text = ""

#Create class that prints the file in a webserver
class CMUQEdgeServer(BaseHTTPRequestHandler):
    def make_content(self):
        #Reset text and file
        whole_text = ""
        file.seek(0)

        #Generate content
        for line in file:
            whole_text += line

        #Check print
        print(whole_text)

        #Return the content of HTML
        return whole_text

    #Get Method
    def do_GET(self):
        #Open file
        file = open("server.txt" , "r+")

        #Create Content
        page_html = self.make_content()

        #Send response
        print(whole_text)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(page_html.encode())

#Activate Server
myserver = HTTPServer(("0.0.0.0", 9039),CMUQEdgeServer)
myserver.serve_forever()



