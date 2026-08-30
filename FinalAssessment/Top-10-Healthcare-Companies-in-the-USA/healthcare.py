# Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


df = pd.read_csv("I:\\Fullstack-AI-BOOTCAMP-B-10\\FinalAssessment\\Top-10-Healthcare-Companies-in-the-USA\\Top 10 Healthcare Companies in the United States.csv")

# Cleaning and Analyzing Data

df = df[["Date", "Close", "High", "Low", "Volume"]]
print(df.head())
print(df.shape)

df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
df["High"] = pd.to_numeric(df["High"], errors="coerce")
df["Low"] = pd.to_numeric(df["Low"], errors="coerce")
df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")

df = df.dropna()
print("\nMissing values:")
print(df.isnull().sum())


df["Next_Close"] = df["Close"].shift(-1)
df = df.dropna()
X = df[["Close", "High", "Low", "Volume"]]
y = df["Next_Close"]

split = int(len(df) * 0.8)

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


y_scaler = StandardScaler()

y_train = y_scaler.fit_transform(
    y_train.values.reshape(-1, 1)
)

days = 30

X_train_new = []
y_train_new = []

for i in range(days, len(X_train)):
    X_train_new.append(X_train[i-days:i])
    y_train_new.append(y_train[i])

X_train_new = np.array(X_train_new)
y_train_new = np.array(y_train_new)

X_test_new = []
y_test_new = []

for i in range(days, len(X_test)):
    X_test_new.append(X_test[i-days:i])
    y_test_new.append(y_test.iloc[i])

X_test_new = np.array(X_test_new)
y_test_new = np.array(y_test_new)


model = Sequential()
model.add(
    LSTM(
        50,
        input_shape=(30, 4)
    )
)

model.add(Dense(1))
model.compile(
    optimizer="adam",
    loss="mse"
)


history = model.fit(
    X_train_new,
    y_train_new,
    epochs=20,
    batch_size=32,
    validation_split=0.1
)


# Predicting-------

prediction = model.predict(X_test_new)

prediction = y_scaler.inverse_transform(prediction)

actual = y_scaler.inverse_transform(
    np.array(y_test_new).reshape(-1, 1)
)


# Metrics

mae = mean_absolute_error(actual, prediction)
rmse = np.sqrt(
    mean_squared_error(actual, prediction)
)
r2 = r2_score(actual, prediction)
print("\nLSTM RESULTS")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

# Directional accuracy

actual_direction = np.diff(actual.flatten()) > 0
predicted_direction = np.diff(prediction.flatten()) > 0
accuracy = np.mean(
    actual_direction == predicted_direction
)
print("Directional Accuracy:", accuracy * 100, "%")

# Actual vs Predicted

plt.figure(figsize=(10, 5))
plt.plot(actual, label="Actual")
plt.plot(prediction, label="Predicted")
plt.title("LSTM Actual vs Predicted")
plt.xlabel("Days")
plt.ylabel("Close Price")
plt.legend()
plt.show()

# Heatmap

corr = df[
    ["Close", "High", "Low", "Volume"]
].corr()
plt.figure(figsize=(6, 5))
plt.imshow(corr)
plt.colorbar()
plt.xticks(
    range(4),
    ["Close", "High", "Low", "Volume"]
)
plt.yticks(
    range(4),
    ["Close", "High", "Low", "Volume"]
)
plt.title("Correlation Heatmap")
plt.show()