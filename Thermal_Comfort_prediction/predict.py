import requests
import json
import pickle
import sklearn
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

def predict_temp(model_name):
	model = pickle.load(open(model_name, 'rb'))

	res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=26.9154576&lon=75.8189817&appid=969d0b21b05fc9d13d4c75029066e6da").json()

	f = float(res["main"]["feels_like"]) - 273.15

	return round(model.predict([[f]])[0][0])
