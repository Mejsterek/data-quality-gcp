from flask import Flask, jsonify
import pandas as pd
from validator import validate

app = Flask(__name__)

@app.get("/")
def health():
    return "Data Quality API is running"

@app.get("/report")
def report():

    df = pd.read_csv("data/sample.csv")

    result = validate(df)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)