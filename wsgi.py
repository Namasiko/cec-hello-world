import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    return "Hello World! Greetings from "+socket.gethostname()+"\n"+"TEST"
    return "+socket.gethostname()+"\n"+ "+socket.gettimestamp()+"\n"

if __name__ == "__main__":
    application.run()
