import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn import tree
import joblib 
data = pd.read_csv("music.csv")
data["age_group"] = pd.cut(  #Creating new feature
    data["age"],
    bins=[0, 20, 30, 100],
    labels=["Teen", "Young Adult", "Adult"]
)
data = pd.get_dummies(data, columns=["age_group"]) #Used to convert categorical/text data into numerical columns
#print(data.isnull().sum())   #Check missing values
#print(data)
#Removing genre but new dataset will be created, original stays the same
new = data.drop(columns=["genre"])
#new = data.drop(columns=["genre", "gender"]) #To check accuracy without gender
new2 = data["genre"]
x_train, x_test, y_train, y_test = train_test_split(new, new2, test_size=0.2, random_state=42)

def decisionModel():
    model1 = DecisionTreeClassifier()
    model1.fit(x_train, y_train) 
    predictions1 = model1.predict(x_test)
    return predictions1

def logisticRegressionModel():
    model2 = LogisticRegression(max_iter=1000)
    model2.fit(x_train, y_train)
    predictions2 = model2.predict(x_test)
    return predictions2

def randomForestModel():
    model3 = RandomForestClassifier()
    model3.fit(x_train, y_train)
    predictions3 = model3.predict(x_test)
    return predictions3
#joblib: has a function of saving and loading models
#joblib.dump(model1, "music-recommender.joblib")
#trained_model = joblib.load("music-recommender.joblib")

def checkMetrics(predictions):
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average="weighted")
    recall = recall_score(y_test, predictions, average="weighted")
    f1 = f1_score(y_test, predictions, average="weighted")

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1:", f1)


predictions1 = decisionModel()
predictions2 = logisticRegressionModel()
predictions3 = randomForestModel()

print(predictions1)
print(predictions2)
print(predictions3)

print("Model : Decision Tree")
checkMetrics(predictions1)

print("Model : Logistic Regression")
checkMetrics(predictions2)

print("Model : Random Forest")
checkMetrics(predictions3)

# tree.export_graphviz(model, 
#                     out_file= "music-recommender.dot",
#                     feature_names= ["age" , "gender"],
#                     class_names= sorted(new2.unique()),
#                     label= "all",
#                     rounded= True,
#                     filled= True)