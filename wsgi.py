import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    return "Hello World! Greetings from "+socket.gethostname()+"\n"+"TEST"
    return window.requestFileSystem(LocalFileSystem.PERSISTENT, 0, onFileSystemSuccess, fail);


if __name__ == "__main__":
    application.run()
