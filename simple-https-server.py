import sys
import BaseHTTPServer, SimpleHTTPServer
import ssl

port=int(sys.argv[1])

print "Listening on port " + sys.argv[1]+" ..."


if len(sys.argv) < 2 :
 
        print "Usage: python "+ sys.argv[0]+" port"

else :
        httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', port),
                SimpleHTTPServer.SimpleHTTPRequestHandler)

        httpd.socket = ssl.wrap_socket (httpd.socket,
                keyfile="empire-priv.key",  # Path to key file
                certfile='cert.pem', server_side=True)   # Path to cert file

        httpd.serve_forever()
