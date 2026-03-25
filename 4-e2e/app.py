from flask import Flask, jsonify, request

app = Flask(__name__)

history = []


@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    result = data["a"] + data["b"]
    history.append({"operation": "add", "a": data["a"], "b": data["b"], "result": result})
    return jsonify({"result": result})


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    result = data["a"] - data["b"]
    history.append({"operation": "subtract", "a": data["a"], "b": data["b"], "result": result})
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    result = data["a"] * data["b"]
    history.append({"operation": "multiply", "a": data["a"], "b": data["b"], "result": result})
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    if data["b"] == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    result = data["a"] / data["b"]
    history.append({"operation": "divide", "a": data["a"], "b": data["b"], "result": result})
    return jsonify({"result": result})


@app.route("/history")
def get_history():
    return jsonify(history)


if __name__ == "__main__":
    app.run(debug=True)
