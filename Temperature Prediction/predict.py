import requests
import json
import pickle
import sklearn

model = pickle.load(open('model_pickle', 'rb'))

res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=26.9154576&lon=75.8189817&appid=969d0b21b05fc9d13d4c75029066e6da").json()

c = float(res["main"]["temp"]) - 273.15

h = res["main"]["humidity"]
f = float(res["main"]["feels_like"]) - 273.15

print("Current temperature: " + str(c))
print("Humidity: " + str(h) + "%")
print("Feels like temperature: " + str(f))
print("Preferable temperature: " + str(round(model.predict([[f]])[0][0])))
