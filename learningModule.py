import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

data = pd.read_csv("ml_data.csv")
inputs = data.drop('label', axis=1)
outputs = data['label']

train_input, test_input, train_output, test_output = train_test_split(
    inputs, outputs, test_size=0.3, random_state=10, stratify=outputs
)

classifier1 = DecisionTreeClassifier()
classifier1.fit(train_input, train_output)

train_pre1 = classifier1.predict(train_input)
print("Train Data : ", accuracy_score(train_pre1, train_output))

test_pre1 = classifier1.predict(test_input)
print("Test Data : ", accuracy_score(test_pre1, test_output))



with open('randomtree.pkl', 'wb') as f:
    pickle.dump(classifier1, f)
