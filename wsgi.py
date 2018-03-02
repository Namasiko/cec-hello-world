import socket
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    with open("/mnt/log_file.log", "a") as my_file:
    #with open("log_file.log", "a") as my_file:
        my_file.write(socket.gethostname() + "  " + str(time.time()) + "\n")

    

if __name__ == "__main__":
    application.run()
