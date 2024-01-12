import pprint

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.post("/tictactoe")
def TTT():
    return jsonify({"text":"yes"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
