import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    with open("/MNT/log_file.log") as my_file:
	my_file.write(socket.gethostname() + " " + str(time.time()) + "\n")

	if __name__ == "__main__":
    application.run()
