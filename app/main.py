from flask import Flask, send_from_directory, jsonify, request
from app import config
from app.handlers import CandidateHandler
from app.helper import initializer

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/candidate", methods=["GET"])
def candidates():
    return jsonify(CandidateHandler.get_all_candidates(request)), 200


if __name__ == '__main__':
    initializer.init()
    app.run(port=config.APP.PORT, debug=config.APP.DEBUG, host=config.APP.HOST)
