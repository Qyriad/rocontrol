from http.server import BaseHTTPRequestHandler, HTTPServer
import nanoid
import os
import sys
import subprocess
import base64
import json
import argparse
import webbrowser

# default hostname and ports
srvHostname = "127.0.0.1"
srvPort = 1533

# argument parsing, yay!
parser = argparse.ArgumentParser(description="An interface for fusée gelée.")
parser.add_argument('--port', '-p', type=int)
parser.add_argument('--host', '--hostname', type=str)

args = parser.parse_args()

if args.host:
    srvHostname = args.host

if args.port:
    srvPort = args.port

# path building for ./web/
web_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'web')

# index.html caching
indexFileObj = open(os.path.join(web_dir, "index.html"), "rb")
indexFile = indexFileObj.read().decode('utf8') # utf8 needed for "é", and the well being of my mind
indexFileObj.close()

# fusee error/result code explainer messages
fuseeCodeMessages = ["Done!", "It seems like your Switch isn't plugged in.", "No access to USB. (you should probably re-run the interface script with sudo or Administrator privileges)", "Hmm, it seems like the data I got back is bad. Try again please.", "Unknown filesystem error. (maybe you're out of space?)", "Unknown Fusée Gelée error. (try running it on it's own and see what's up)"]

class IDFRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes(indexFile, "utf8"))
        return
    
    def do_POST(self):
        # get POST JSON data
        contentLen = int(self.headers.get('Content-Length'))
        postBody = self.rfile.read(contentLen)
        postObj = json.loads(postBody)

        fuseeResult = fuseeExec(postObj["payload"])
        
        self.send_response(400 if fuseeResult > 0 else 200)

        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        message = fuseeCodeMessages[fuseeResult] # get response message

        self.wfile.write(bytes(message, "utf8"))
        return

def fuseeExec(payload):
    """
    Executes fusée gelée from a Base64 payload.

    Arguments:
     * payload - Payload in Base64
    
    Returns: return code
     * 0: A-OK
     * 1: Your Switch isn't plugged in.
     * 2: No access to USB. (re-run w/ sudo, probably)
     * 3: Bad Base64.
     * 4: Unknown FS error. (you're probably out of space)
     * 5: Unknown Fusée Gelée error.
    """

    result = 0 # default result

    tempBinFile = nanoid.generate(alphabet="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-") + ".bin" # generate a temporary .bin filename
    tempBinPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), tempBinFile) # get full path for that generated file name

    file = open(tempBinPath, "wb") # open the temp file in binary mode
    try:
        file.write(base64.b64decode(payload)) # write b64 binary data to it
    except TypeError: # if bad b64
        result = 3
    except:
        result = 4
    
    file.close()

    if result != 0: # if an error already happened
        os.remove(tempBinPath)
        return result

    fuseeFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fusee-launcher/fusee-launcher.py") # build path for fusee-launcher file

    # cwd trickery, for fusée's well being with intermezzo (TODO: Test if this is needed for sure)
    os.chdir(os.path.dirname(fuseeFilePath))

    p = subprocess.Popen([sys.executable, fuseeFilePath, tempBinPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # run fusée gelée
    p.wait() # wait for it to close

    if p.returncode != 0: # if it failed
        output = p.stdout.read().decode("utf-8")
        errout = p.stderr.read().decode("utf-8")
        if output.lower().startswith("no") and p.returncode == 255: # No TegraRCM device found?
            result = 1
        elif "errno 13" in errout.lower() and p.returncode == 1: # Errno 13: Access Denied (for USB)
            result = 2
        else:
            result = 5
    
    os.remove(tempBinPath)

    return result

if __name__ == "__main__":
    server_address = (srvHostname, srvPort)
    httpd = HTTPServer(server_address, IDFRequestHandler)
    print("Listening on host {}, and on port {}. Have fun!".format(server_address[0], server_address[1]))
    webbrowser.open("http://{}:{}".format(srvHostname, srvPort))
    httpd.serve_forever()