import socket
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    with open("/mnt/log_file.log", "a") as my_file:
    #with open("log_file.log", "a") as my_file:
      my_file.write(socket.gethostname() + "  " + str(time.time()) + "\n")
    
     with open("/mnt/log_file.log") as my_file:
       for line in my_file:
         hello_string += line + "<br>"
    

	return "Hello World! Greetings from "+socket.gethostname()+"\n"+"TEST"


if __name__ == "__main__":
    application.run()
