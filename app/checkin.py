from flask import Flask
import socket
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route("/getip", methods=["GET"])
def get_my_ip():
  if request.headers.getlist("X-REAL-IP"):
     ip = request.headers.getlist("X-REAL-IP")[0]
  else:
     ip = request.remote_addr
  
  return jsonify({'ip': ip}), 200

@app.route("/hostname/")
def return_hostname():
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
