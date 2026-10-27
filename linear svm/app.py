
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler pipeline
model = joblib.load("linear_svm_banknote.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        variance = float(request.form["variance"])
        skewness = float(request.form["skewness"])
        curtosis = float(request.form["curtosis"])
        entropy = float(request.form["entropy"])

        features = np.array([[
            variance, skewness, curtosis, entropy
        ]])

        prediction = int(model.predict(features)[0])

        if prediction == 0:
            result = "Counterfeit Banknote"
        else:
            result = "Genuine Banknote"

        return render_template(
            "index.html",
            prediction=result
        )

    except (ValueError, KeyError):
        return render_template(
            "index.html",
            prediction="Please enter valid numerical values."
        )


if __name__ == "__main__":
    app.run(debug=True)
