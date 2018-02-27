import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! Greetings  "+socket.gethostname()+"\n"+"TEST"
	
	if __name__ == "__main__":
    application.run()
