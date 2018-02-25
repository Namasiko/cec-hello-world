import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    return "Hello World! Greetings from "+socket.gethostname()+"\n"+"TEST"+"timestamp":2016-09-08T05:04:46Z"


if __name__ == "__main__":
    application.run()
