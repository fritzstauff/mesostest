from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route("/getip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
