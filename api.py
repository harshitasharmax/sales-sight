from flask import Flask, request, jsonify
import joblib
import os
import pandas as pd

MODEL_FILE = os.path.join("models", "sales_model.pkl")
app = Flask(__name__)

if not os.path.exists(MODEL_FILE):
    raise FileNotFoundError("Model not found. Run train_model.py first to create models/sales_model.pkl")

model_bundle = joblib.load(MODEL_FILE)
model = model_bundle["model"]
features = model_bundle["features"]

@app.route("/ping")
def ping():
    return "SalesSight API alive"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if data is None:
        return jsonify({"error": "Request must be JSON"}), 400
    try:
        df = pd.DataFrame([data])
        X = df[features]
        pred = model.predict(X)[0]
        return jsonify({"predicted_next_day_qty": float(pred)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
