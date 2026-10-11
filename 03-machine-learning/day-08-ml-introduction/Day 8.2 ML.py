import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("car.data")
data.columns = [
    "buying",
    "maint",
    "doors",
    "persons",
    "lug_boot",
    "safety",
    "class"
]
#print(data.head())

features = data[[
    "buying",
    "maint",
    "safety"
]].values
label = data[["class"]]
#print(features, label)
#converting the data
Le = LabelEncoder()
for i in range(len(features[0])):
    features[:, i] = Le.fit_transform(features[:, i])

#print(features)
#converting label
label_maping = {
    "unacc" : 0,
    "acc" : 1,
    "good" : 2,
    "vgood" : 3
} 
label["class"] = label["class"].map(label_maping)
label = np.array(label)
#print(label)
#Create model
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights="uniform")
x_train, x_test, y_train, y_test = train_test_split(features, label , test_size=0.2)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)
accuracy = metrics.accuracy_score(y_test, predictions)
print("Predictions" , predictions)
print("Accuracy" , accuracy)

my_value = 20
print("Actual value: ", label[my_value])
print("Predicted value: ", knn.predict(features)[my_value])
