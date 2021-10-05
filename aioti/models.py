import pickle
from numpy import array as nparray
from typing import List

MODEL_PATH = './model.pkl'
model = None

def _get_model():
    global model
    if model is None:
        model = pickle.load(open(MODEL_PATH, 'rb'))

    return model


def predict(data: dict) -> float:
    X = transform_data(data)

    y = _get_model().predict_proba(nparray(X))
    return y[0][1]


def transform_data(data: dict) -> List[List[int]]:
    # 0   temp    104 non-null    float64
    # 1   rain    104 non-null    int64  
    # 2   wind    104 non-null    float64
    # 3   RH      104 non-null    int64 
    # {'Lat': -6.329598542338873, 'Long': 106.72983194993282, 'DeviceId': 1, 'Humidity': 44.200001, 'Temp': 29.6, 'Fire': 1.695236}
    return [[data['Temp'], data['rain'], data['wind'] * 3.6, data['Humidity'] ]]
