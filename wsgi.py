import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    return "Hello World! Greetings from "+socket.gethostname()+"\n"+"TEST"
    import time;
	ts = time.time()
	print(ts)
	# 1519322772.43	
return (ts)

if __name__ == "__main__":
    application.run()
