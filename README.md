# CropTop – Crop Recommendation API

CropTop is a simple Flask-based API that predicts the best or 'top' crop to grow based on soil and weather inputs. It uses a machine learning model trained on real agricultural data.

---

## Features

- Takes input like N, P, K, temperature, humidity, pH, and rainfall
- Returns the most suitable crop using a trained Random Forest model
- Easy to use with mobile apps or web frontends

---

## How to Use

### 1. Clone the project

```bash
git clone https://github.com/ak-2045/croptop-the-crop-rec-api.git
cd croptop-the-crop-rec-api
````

### 2. Set up and run

```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

API runs at `http://127.0.0.1:5000/`

---

## Files Included

* `app.py` – Flask server code
* `crop_rec_model.pkl` – Trained model
* `requirements.txt` – Project dependencies

---

## Requirements

* Python 3.7 or above
* Flask
* scikit-learn
* numpy

---

## Author

Made by **Akmal Hossain**
Project: Crop Recommendation using Machine Learning

```
