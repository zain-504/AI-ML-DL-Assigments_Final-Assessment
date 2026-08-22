import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix




df = pd.read_csv("E:\\Fullstack-AI-BOOTCAMP-B-10\\FinalAssessment\\UCI-Heart-Disease-Dataset\\heart_disease_combined.csv")

print(df.head())

print("\nShape:")
print(df.shape)

print("\nInformation:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())


df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)



for column in df.columns:

    if df[column].dtype == "object":
        df[column] = df[column].fillna(
            df[column].mode()[0]
        )

    else:
        df[column] = df[column].fillna(
            df[column].median()
        )


print("\nMissing values after cleaning:")
print(df.isnull().sum())



df = pd.get_dummies(
    df,
    columns=["source"],
    drop_first=True
)

print("\nData after encoding:")
print(df.head())


X = df.drop("target", axis=1)
y = df["target"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)



scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)



model1 = LogisticRegression()

model1.fit(X_train, y_train)

prediction1 = model1.predict(X_test)

accuracy1 = accuracy_score(
    y_test,
    prediction1
)

print("\nLogistic Regression Accuracy:")
print(accuracy1)



model2 = DecisionTreeClassifier(
    random_state=42
)

model2.fit(X_train, y_train)

prediction2 = model2.predict(X_test)

accuracy2 = accuracy_score(
    y_test,
    prediction2
)

print("\nDecision Tree Accuracy:")
print(accuracy2)



model3 = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model3.fit(X_train, y_train)

prediction3 = model3.predict(X_test)

accuracy3 = accuracy_score(
    y_test,
    prediction3
)

print("\nRandom Forest Accuracy:")
print(accuracy3)




print("\nMODEL COMPARISON")

print("Logistic Regression :", accuracy1)
print("Decision Tree       :", accuracy2)
print("Random Forest       :", accuracy3)



cm = confusion_matrix(
    y_test,
    prediction3
)

print("\nConfusion Matrix:")
print(cm)



plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d"
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Random Forest Confusion Matrix")

plt.show()



plt.figure(figsize=(12, 8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()