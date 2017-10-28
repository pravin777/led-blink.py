from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import mraa
import time



# Setup
led = mraa.Gpio(31)
led.dir(mraa.DIR_OUT)

PORT_NUMBER = 8080


class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/off':
            self.do_off()
        elif self.path == '/on':
            self.do_on()
        return

    def do_on(self):
        global led
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "LED ON"
        try :
            led.write(1)
        except:
            message = "Error"

        self.wfile.write(message)
        return

    def do_off(self):
        global led
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "LED OFF"
        try :
            led.write(0)
        except:
            message = "Error"

        self.wfile.write(message)
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
