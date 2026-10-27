
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/info", methods=["GET"])
def get_info():
    return jsonify({
        "service": "Service A",
        "status": "running",
        "message": "Hello from Service A!",
        "technology": "Python Flask"
    }), 200


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Service A is running",
        "endpoint": "/info"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
