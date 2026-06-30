from flask import Flask, jsonify, request
import pandas as pd
from validator import validate

app = Flask(__name__)

@app.get("/")
def health():
    return "Data Quality API is running"

@app.post("/validate")
def validate_csv():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    df = pd.read_csv(file)

    result = validate(df)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)