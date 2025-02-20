from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and vectorizer
try:
    model = joblib.load("fake_news_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
except FileNotFoundError:
    print("❌ Error: Model files not found. Make sure 'fake_news_model.pkl' and 'vectorizer.pkl' are in the same directory.")
    exit()

@app.route("/")
def home():
    return "📰 Fake News Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        text = [data["text"]]  # Convert text into a list
        
        # Transform input text using the vectorizer
        text_vec = vectorizer.transform(text)
        
        # Predict (1 = Fake, 0 = Real)
        prediction = model.predict(text_vec)[0]

        return jsonify({"fake_news": bool(prediction)})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
