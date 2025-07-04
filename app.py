from flask import Flask, request, jsonify
import pickle
import numpy as np
rec_model = pickle.load(open('crop_rec_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')

def home():
    return "Hello World!"

@app.route('/predict', methods=['POST'])
def predict():
    N = float(request.form.get('N'))
    P = float(request.form.get('P'))
    K = float(request.form.get('K'))

    temperature = float(request.form.get('temperature'))
    humidity = float(request.form.get('humidity'))

    ph = float(request.form.get('ph'))
    rainfall = float(request.form.get('rainfall'))

    input_query = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    result = rec_model.predict(input_query)[0]

    return jsonify({'predicted_crop': str(result)})


if __name__ == '__main__':
    app.run(debug=True)