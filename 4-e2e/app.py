from flask import Flask, jsonify, request

app = Flask(__name__)

history = []


def parse_operands(req):
    """Parse and validate a and b from request JSON. Returns (a, b) or raises ValueError."""
    data = req.get_json(silent=True)
    if data is None:
        raise ValueError("Invalid or missing JSON body")
    if "a" not in data or "b" not in data:
        raise ValueError("Both 'a' and 'b' fields are required")
    a, b = data["a"], data["b"]
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Fields 'a' and 'b' must be numbers")
    return a, b


@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    try:
        a, b = parse_operands(request)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    result = a + b
    history.append({"operation": "add", "a": a, "b": b, "result": result})
    return jsonify({"result": result})


@app.route("/subtract", methods=["POST"])
def subtract():
    try:
        a, b = parse_operands(request)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    result = a - b
    history.append({"operation": "subtract", "a": a, "b": b, "result": result})
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def multiply():
    try:
        a, b = parse_operands(request)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    result = a * b
    history.append({"operation": "multiply", "a": a, "b": b, "result": result})
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def divide():
    try:
        a, b = parse_operands(request)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    if b == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    result = a / b
    history.append({"operation": "divide", "a": a, "b": b, "result": result})
    return jsonify({"result": result})


@app.route("/history")
def get_history():
    return jsonify(history)


if __name__ == "__main__":
    app.run(debug=True)
