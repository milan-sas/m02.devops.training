from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    raise NotImplementedError("Implement home endpoint using TDD")


@app.route("/health")
def health():
    raise NotImplementedError("Implement health endpoint using TDD")


@app.route("/add", methods=["POST"])
def add():
    raise NotImplementedError("Implement add endpoint using TDD")


@app.route("/subtract", methods=["POST"])
def subtract():
    raise NotImplementedError("Implement subtract endpoint using TDD")


@app.route("/multiply", methods=["POST"])
def multiply():
    raise NotImplementedError("Implement multiply endpoint using TDD")


@app.route("/divide", methods=["POST"])
def divide():
    raise NotImplementedError("Implement divide endpoint using TDD")


if __name__ == "__main__":
    app.run(debug=True)
