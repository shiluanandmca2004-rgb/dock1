from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model (saved as model.pkl)
model = joblib.load("model.pkl")

@app.route("/", methods=["GET"])
def home():
    return "✅ Grade Calculator API is live on Render! Use /predict with POST JSON data."

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        # For browser test
        return """
        <h2>Grade Prediction API</h2>
        <p>Use POST request with JSON like:</p>
        <pre>{ "marks": [70, 80, 90] }</pre>
        """

    if request.method == "POST":
        try:
            data = request.get_json()
            marks = data.get("marks", [])
            if not marks:
                return jsonify({"error": "Please provide marks as a list"}), 400

            avg_marks = np.mean(marks)

            # Predict grade
            grade = model.predict([[avg_marks]])[0]

            return jsonify({
                "average_marks": avg_marks,
                "predicted_grade": grade
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
