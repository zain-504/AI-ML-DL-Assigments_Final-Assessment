# 1. Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report



df = pd.read_csv("Hospitals(3).csv")

print(df.head())
print(df.shape)
print(df.info())

# Analyze and Cleaning Data

print(df.isnull().sum())
df = df.replace("NOT AVAILABLE", np.nan)


df = df.drop([
    "X", "Y", "OBJECTID", "ID",
    "NAME", "ADDRESS", "TELEPHONE",
    "SOURCE", "SOURCEDATE", "VAL_DATE",
    "WEBSITE", "ALT_NAME", "TTL_STAFF"
], axis=1)


for col in df.columns:

    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])

    else:
        df[col] = df[col].fillna(df[col].median())


print("\nMissing values after cleaning:")
print(df.isnull().sum())


X = df.drop("STATUS", axis=1)
y = df["STATUS"]


X = pd.get_dummies(X, dtype=int)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)



# LOGISTIC REGRESSION

model1 = LogisticRegression(max_iter=1000)

model1.fit(X_train, y_train)

prediction1 = model1.predict(X_test)

accuracy1 = accuracy_score(y_test, prediction1)

print("\nLogistic Regression Accuracy:")
print(accuracy1)


# DECISION TREE

model2 = DecisionTreeClassifier(random_state=42)

model2.fit(X_train, y_train)

prediction2 = model2.predict(X_test)

accuracy2 = accuracy_score(y_test, prediction2)

print("\nDecision Tree Accuracy:")
print(accuracy2)


# RANDOM FOREST

model3 = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model3.fit(X_train, y_train)

prediction3 = model3.predict(X_test)

accuracy3 = accuracy_score(y_test, prediction3)

print("\nRandom Forest Accuracy:")
print(accuracy3)


# MODEL COMPARISON

print("\nMODEL COMPARISON")

print("Logistic Regression:", accuracy1)
print("Decision Tree:", accuracy2)
print("Random Forest:", accuracy3)


# CONFUSION MATRIX

cm = confusion_matrix(y_test, prediction3)

print("\nConfusion Matrix:")
print(cm)


# CLASSIFICATION REPORT

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        prediction3
    )
)

# CONFUSION MATRIX HEATMAP

plt.figure(figsize=(6, 5))
plt.imshow(cm)
plt.colorbar()
plt.xticks(
    [0, 1],
    ["CLOSED", "OPEN"]
)
plt.yticks(
    [0, 1],
    ["CLOSED", "OPEN"]
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix Heatmap")
plt.show()

# CORRELATION HEATMAP

corr = df.select_dtypes(
    include=np.number
).corr()
plt.figure(figsize=(10, 7))
plt.imshow(corr)
plt.colorbar()
plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=90
)
plt.yticks(
    range(len(corr.columns)),
    corr.columns
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()