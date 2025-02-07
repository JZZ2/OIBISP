# -*- coding: utf-8 -*-
"""Iris flower classification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13NkKe156GE0GIfVkfaRjkZOc8Z19w3ty

Importing Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""Loading DataSet"""

columns = ['Sepal length','Sepal width','Petal length','Petal width','Class_labels']
df = pd.read_csv('IRIS.csv', names=columns, header=0)

# Convert columns to numeric, handling errors and investigating problematic values
for col in ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']:
    try:
        df[col] = pd.to_numeric(df[col], errors='raise')
    except ValueError as e:
        print(f"Error converting column '{col}': {e}")
        # Print unique values in the column to investigate:
        print(f"Unique values in '{col}': {df[col].unique()}")

"""Visualization of DataSet"""

# Convert columns to numeric
for col in ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.describe()

sns.pairplot(df,hue='Class_labels')



"""Separiting Columns"""

data = df.values
X = data[:,0:4]
Y = data[:,4]
print(Y)

"""Splitting Data For Training And Tessting"""

#split the data into train and test datasets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
print(X_test)



"""Model1: Support Vector MAchine Algorithm"""

from sklearn.svm import SVC
svc_model = SVC()
svc_model.fit(X_train,Y_train)

prediction1 = svc_model.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,prediction1))
for i in range(len(prediction1)):
  print(Y_test[i],prediction1[i])

"""Model2: Logistic Regression"""

from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression()
lr_model.fit(X_train,Y_train)

prediction2 = lr_model.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,prediction2))
for i in range(len(prediction2)):
  print(Y_test[i],prediction2[i])



"""Model3: Decision Tree Classifier"""

from sklearn.tree import DecisionTreeClassifier
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train,Y_train)

prediction3 = dt_model.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,prediction3))
for i in range(len(prediction3)):
  print(Y_test[i],prediction3[i])



"""Classification Report"""

from sklearn.metrics import classification_report
print(classification_report(Y_test,prediction2))

X_new = np.array([[3,2,1,0.2],[4.9,2.2,3.8,1.1],[5.3,2.5,4.6,1.9]])

prediction = dt_model.predict(X_new)
print("Prediction: {}".format(prediction))

