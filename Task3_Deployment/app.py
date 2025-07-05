from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(x) for x in request.form.values()]
    final_input = scaler.transform([input_data])
    prediction = model.predict(final_input)
    return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction[0]:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
