import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    with open("/mnt/log_file.log", "a") as my_file:
        my_file.write(socket.gethostname() + "  " + str(time.time()) + "\n")
    return "test"

if __name__ == "__main__":
    application.run()
