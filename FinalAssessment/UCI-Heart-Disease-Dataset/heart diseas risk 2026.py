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
from sklearn.metrics import classification_report



df = pd.read_csv("E:\\Fullstack-AI-BOOTCAMP-B-10\\FinalAssessment\\UCI-Heart-Disease-Dataset\\heart_disease_cleveland.csv")

"After loading the data here i am analyzing the data"

print(df.head())
print(df.info())
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

"After analyxing the data now i am cleaning the data"

df.drop_duplicates(inplace=True)

# Fill missing numerical values
num_cols = df.select_dtypes(include=np.number).columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())



X = df.drop(["target"], axis=1)
y = df["target"]


"here i am splitting the data in to x and y for the training of data"

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

"Applying standerd scaler on expanded data for compressing it "

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"Now i am applying logistic regression model"

print("\n---------------------")
print("LOGISTIC REGRESSION")
print("---------------")

lr = LogisticRegression(max_iter=1000)

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

print("Accuracy :", accuracy_score(y_test, lr_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, lr_pred))

print("\nClassification Report")
print(classification_report(y_test, lr_pred))


"Now i am applying decision tree model"


print("\n-----------------")
print("DECISION TREE")
print("---------------")

dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

print("Accuracy :", accuracy_score(y_test, dt_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, dt_pred))

print("\nClassification Report")
print(classification_report(y_test, dt_pred))


"Now i am applying random forest model"


print("\n-----------------")
print("RANDOM FOREST")
print("-------------------")

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("Accuracy :", accuracy_score(y_test, rf_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, rf_pred))

print("\nClassification Report")
print(classification_report(y_test, rf_pred))


"Here we are going to compare all the three models"

print("\n------------------")
print("MODEL COMPARISON")
print("--------------------")

print("Logistic Regression :", accuracy_score(y_test, lr_pred))
print("Decision Tree       :", accuracy_score(y_test, dt_pred))
print("Random Forest       :", accuracy_score(y_test, rf_pred))


"The Correlation HeatMap"

correlation = df.corr(numeric_only=True)

plt.figure(figsize=(12,8))

sns.heatmap(correlation,
            cmap="coolwarm",
            annot=False)

plt.title("Correlation Heatmap")
plt.show()



""" Three classification algorithms were used on the cleveland heart disease dataset, logistic regression,
decision tree, and random forest. Logistic regression got the highest accuracy of 88.52% followed by
random forest with 85.25%. Decision tree got 75.41%. Therefore, logistic regression performed the best on the test data"""