import socket
import datetime
from flask import Flask

application = Flask(__name__)
s = datetime.datetime.now().isoformat()

@application.route("/")
def hello():
    
    return "Hello World! Greetings from "+socket.gethostname()+"\n" 
	return(s)
	# '2017-07-24T23:54:45.203788'
  


if __name__ == "__main__":
    application.run()
