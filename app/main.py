from flask import Flask, send_from_directory, jsonify, request
from app import config
from app.handlers import CandidateHandler
from app.helper import initializer
import time
import logging

app = Flask(__name__)

@app.before_first_request
def configure():
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers.extend(gunicorn_logger.handlers)
    app.logger.setLevel(logging.DEBUG)

    initializer.init()
    logging.info("Execute init")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/candidates", methods=["GET"])
def candidates():
    return jsonify(CandidateHandler.get_all_candidates(request)), 200


@app.route("/candidate", methods=["GET"])
def one_candidate():
    return jsonify(CandidateHandler.get_one_candidate(request)), 200


@app.route("/vote", methods=["GET", "POST"])
def votes():
    if request.method == "GET":
        return jsonify(CandidateHandler.get_all_votes(request)), 200

    if request.method == "POST":
        return jsonify(CandidateHandler.insert_candidate_vote(request)), 200


if __name__ == '__main__':
    initializer.init()
    app.run(port=config.APP.PORT, debug=config.APP.DEBUG, host=config.APP.HOST)
