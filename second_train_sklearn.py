import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree


ga_data = pd.read_csv('/home/barvin04/Desktop/second_forsk.txt', sep=',',header=None)

print(ga_data)
print(ga_data.shape)
print(ga_data.head())

X = ga_data.values[:, 3:9]
Y= ga_data.values[:, 9]
print(X)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

print(X_train)
print(X_test)

clf_gini = DecisionTreeClassifier(criterion='gini', random_state=100, max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)

clf_gini.predict([[17,-13,509,0,-816,-305]])  #walk
clf_gini.predict([[-43,27,-6,0,-967,-221]])   #abnormal

y_pred = clf_gini.predict(X_test)
print(y_pred)

acc = accuracy_score(y_test, y_pred)*100
print(acc)
