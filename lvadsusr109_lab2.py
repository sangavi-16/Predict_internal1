# -*- coding: utf-8 -*-
"""LVADSUSR109_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1du0oOIFzZkikuHpevlUDrAN83NAP8-aP
"""

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import seaborn as sns
from sklearn.tree import BaseDecisionTree
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,precision_score,recall_score,accuracy_score,f1_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("/content/drive/MyDrive/Predictive/booking.csv")
print(df)

# Performing EDA
# Checking for the duplicate and nullvalues
print(df.isnull().sum())
print(df.duplicated().sum())
df.drop_duplicates()

# We have no null values here

df.info()

#Detecting Outlier
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
# Calculate IQR (Interquartile Range)
IQR = Q3 - Q1
outliers = (df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))
# Drop outliers
data_no_outliers = df[~outliers.any(axis=1)]

# Finding correlation between the features
# If any feature have less correlation we can drop that feature
corr=df.corr()
sns.heatmap(corr,annot=True)

encoder=LabelEncoder()
df['type of meal']=encoder.fit_transform(df['type of meal'])
df['room type']=encoder.fit_transform(df['room type'])
df['booking status']=encoder.fit_transform(df['booking status'])
df['market segment type']=encoder.fit_transform(df['market segment type'])
df['Booking_ID']=encoder.fit_transform(df['Booking_ID'])

print(df)

df.describe()

X=df.drop(columns=['booking status','date of reservation'],axis=1)

y=df['booking status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Development and Training for Logistic Regression
model = LogisticRegression(max_iter=1000)



## Sigmoid function actually performs with likelyhood in which the values ranges between 0 and 1.Based on the threshold it classify the values.
model.fit(X_train, y_train)

# Evaluating the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:\n", conf_matrix)

print(y_test.head())
print(y_pred)

plt.bar(y_test,y_pred)
plt.show()



# Model Development and Training for Decision Tree

x=df.drop(columns=['booking status','date of reservation'],axis=1)

Y=df['booking status']
x_train, x_test, Y_train, Y_test = train_test_split(x, Y, test_size=0.3, random_state=34)

tree = DecisionTreeClassifier(random_state=23,max_depth=2,)
tree.fit(x_train, Y_train)

# Evaluating the model
Y_pred = model.predict(x_test)

accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred, average='weighted')
recall = recall_score(Y_test, Y_pred, average='weighted')
f1 = f1_score(Y_test, Y_pred, average='weighted')
conf_matrix = confusion_matrix(Y_test, Y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:\n", conf_matrix)

# Now we completed the model building and evaluation .We can now do hyperparameter tuning.
# Like we can see our accuracy is arround 76 we can increase the train size,we can drop certain features based on the correlation.
# Then we can train the model again to get the better output.