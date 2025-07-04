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
    data = request.get_json()

    N = float(data['N'])
    P = float(data['P'])
    K = float(data['K'])
    temperature = float(data['temperature'])
    humidity = float(data['humidity'])
    ph = float(data['ph'])
    rainfall = float(data['rainfall'])

    input_query = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    result = rec_model.predict(input_query)[0]

    return jsonify({'prediction': str(result)})


    input_query = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    result = rec_model.predict(input_query)[0]

    return jsonify({'predicted_crop': str(result)})


if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug=True)
