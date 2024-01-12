import pprint

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.post("/tictactoe")
def TTT():
    file = open("static/ttt.html")
    content = '\n'.join(file.readlines())
    file.close()
    return jsonify({"text": content})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
