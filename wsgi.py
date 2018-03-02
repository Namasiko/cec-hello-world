import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    with open("/mnt/log_file.log") as my_file:
        my_file.write(socket.gethostname() + "  " + str(time.time()) + "\n")
 
application.run()
