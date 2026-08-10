# -------------------- IMPORT LIBRARIES --------------------
from flask import Flask, render_template, request
import numpy as np
import pickle

# -------------------- LOAD MODEL --------------------
# model.pkl must be trained using sklearn and placed in same folder
model = pickle.load(open("model.pkl", "rb"))

# -------------------- FLASK APP --------------------
app = Flask(__name__)

# -------------------- HOME ROUTE --------------------
@app.route("/")
def index():
    return render_template("index.html")

# -------------------- PREDICTION ROUTE --------------------
@app.route("/predict", methods=["POST"])
def predict():
    # Get raw input from form
    raw_input = request.form.get("feature")

    # ---------- INPUT CLEANING ----------
    # Replace new lines with commas (important fix)
    raw_input = raw_input.replace("\n", ",")

    # Split input, strip spaces, remove empty values
    features_list = [x.strip() for x in raw_input.split(",") if x.strip()]

    # ---------- VALIDATION 1: FEATURE COUNT ----------
    if len(features_list) != 30:
        return render_template(
            "index.html",
            error="❌ Please enter exactly 30 numeric feature values."
        )

    try:
        # ---------- VALIDATION 2: NUMERIC ----------
        features_array = np.array(features_list, dtype=float)

        # Reshape for ML model (1 sample, 30 features)
        prediction = model.predict(features_array.reshape(1, -1))

        # Convert prediction to readable result
        result = "cancerous" if prediction[0] == 1 else "not cancerous"

        return render_template(
            "index.html",
            result=result
        )

    except ValueError:
        return render_template(
            "index.html",
            error="❌ Invalid input! Use only numbers separated by commas."
        )

# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app.run(debug=True)
