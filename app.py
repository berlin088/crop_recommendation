from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('crop_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[x]) for x in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
        prediction = model.predict([features])[0]
        return render_template('result.html', prediction=prediction)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
