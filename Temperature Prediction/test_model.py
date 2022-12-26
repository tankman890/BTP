import pickle

import sklearn

model = pickle.load(open('model_pickle', 'rb'))

print()
f = int(input("Enter feels like temperature: "))
print("Preferable temperature: " + str(round(model.predict([[f]])[0][0])))
