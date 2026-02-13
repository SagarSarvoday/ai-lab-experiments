# # ===================================
# # Import Libraries
# # ===================================

# import numpy as np
# import pandas as pd

# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# # ===================================
# # Create Dataset (Vehicle Example)
# # ===================================

# data = {
#     "engine_size": [1.0,1.2,1.5,1.6,1.8,2.0,2.2,2.5,2.8,3.0],
#     "weight": [800,900,1000,1100,1200,1300,1400,1500,1600,1700],
#     "mileage": [24,23,22,21,19,18,17,15,14,12]
# }

# df = pd.DataFrame(data)

# X_simple = df[["engine_size"]]
# X_multiple = df[["engine_size","weight"]]
# y = df["mileage"]

# # ===================================
# # Evaluation Function
# # ===================================

# def evaluate(y_true, y_pred, name):
#     print("\n==========", name, "==========")
#     print("R2   :", r2_score(y_true, y_pred))
#     print("MAE  :", mean_absolute_error(y_true, y_pred))
#     print("RMSE :", np.sqrt(mean_squared_error(y_true, y_pred)))

# # ===================================
# # 1️⃣ SIMPLE LINEAR REGRESSION
# # ===================================

# model_simple = LinearRegression()
# model_simple.fit(X_simple, y)

# y_pred_simple = model_simple.predict(X_simple)
# evaluate(y, y_pred_simple, "Simple Linear Regression")

# # ===================================
# # 2️⃣ MULTIPLE LINEAR REGRESSION
# # ===================================

# model_multiple = LinearRegression()
# model_multiple.fit(X_multiple, y)

# y_pred_multiple = model_multiple.predict(X_multiple)
# evaluate(y, y_pred_multiple, "Multiple Linear Regression")

# # ===================================
# # 3️⃣ POLYNOMIAL REGRESSION
# # ===================================

# poly = PolynomialFeatures(degree=2)
# X_poly = poly.fit_transform(X_simple)

# model_poly = LinearRegression()
# model_poly.fit(X_poly, y)

# y_pred_poly = model_poly.predict(X_poly)
# evaluate(y, y_pred_poly, "Polynomial Regression")

# # ===================================
# # USER INPUT PREDICTION
# # ===================================

# print("\n==============================")
# print("Enter Vehicle Details to Predict Mileage")
# print("==============================")

# engine = float(input("Engine size (e.g. 1.8): "))
# weight = float(input("Vehicle weight (e.g. 1200): "))

# user_data_simple = pd.DataFrame([[engine]], columns=["engine_size"])
# user_data_multiple = pd.DataFrame([[engine, weight]], columns=["engine_size","weight"])

# user_data_poly = poly.transform(user_data_simple)

# # Predictions
# pred_simple = model_simple.predict(user_data_simple)
# pred_multiple = model_multiple.predict(user_data_multiple)
# pred_poly = model_poly.predict(user_data_poly)

# print("\n------ Prediction Results ------")
# print("Simple Linear Regression :", round(pred_simple[0],2), "km/l")
# print("Multiple Linear Regression :", round(pred_multiple[0],2), "km/l")
# print("Polynomial Regression :", round(pred_poly[0],2), "km/l")

# print("\nExperiment Completed Successfully.")



# ===================================
# Import Libraries
# ===================================

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ===================================
# Load CSV Dataset
# ===================================

# ===================================
# Load Dataset From Internet
# ===================================

df = pd.read_csv(
    "https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv"
)

df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")
df = df.dropna()

print("Dataset Loaded Successfully!")
print(df.head())



print("\nDataset Loaded Successfully!")
print(df.head())

# ===================================
# Data Cleaning (VERY IMPORTANT)
# ===================================

# Convert horsepower to numeric (dataset has '?' values sometimes)
df["horsepower"] = pd.to_numeric(df["horsepower"], errors='coerce')

# Drop missing values
df = df.dropna()

# ===================================
# Select Features
# ===================================

# Simple Linear Regression → weight vs mpg
X_simple = df[["weight"]]

# Multiple Linear Regression → weight + horsepower vs mpg
X_multiple = df[["weight","horsepower"]]

# Target variable
y = df["mpg"]

# ===================================
# Evaluation Function
# ===================================

def evaluate(y_true, y_pred, name):
    print("\n==========", name, "==========")
    print("R2   :", r2_score(y_true, y_pred))
    print("MAE  :", mean_absolute_error(y_true, y_pred))
    print("RMSE :", np.sqrt(mean_squared_error(y_true, y_pred)))

# ===================================
# 1️⃣ SIMPLE LINEAR REGRESSION
# ===================================

model_simple = LinearRegression()
model_simple.fit(X_simple, y)

y_pred_simple = model_simple.predict(X_simple)
evaluate(y, y_pred_simple, "Simple Linear Regression")

# ===================================
# 2️⃣ MULTIPLE LINEAR REGRESSION
# ===================================

model_multiple = LinearRegression()
model_multiple.fit(X_multiple, y)

y_pred_multiple = model_multiple.predict(X_multiple)
evaluate(y, y_pred_multiple, "Multiple Linear Regression")

# ===================================
# 3️⃣ POLYNOMIAL REGRESSION
# ===================================

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X_simple)

model_poly = LinearRegression()
model_poly.fit(X_poly, y)

y_pred_poly = model_poly.predict(X_poly)
evaluate(y, y_pred_poly, "Polynomial Regression")

# ===================================
# USER INPUT PREDICTION
# ===================================

print("\n==============================")
print("Enter Vehicle Details to Predict MPG")
print("==============================")

weight = float(input("Enter vehicle weight (e.g. 3000): "))
horsepower = float(input("Enter horsepower (e.g. 120): "))

# Create DataFrame inputs (avoids sklearn warnings)
user_simple = pd.DataFrame([[weight]], columns=["weight"])
user_multiple = pd.DataFrame([[weight, horsepower]], columns=["weight","horsepower"])

user_poly = poly.transform(user_simple)

# Predictions
pred_simple = model_simple.predict(user_simple)
pred_multiple = model_multiple.predict(user_multiple)
pred_poly = model_poly.predict(user_poly)

print("\n------ Prediction Results ------")
print("Simple Linear Regression :", round(pred_simple[0],2), "mpg")
print("Multiple Linear Regression :", round(pred_multiple[0],2), "mpg")
print("Polynomial Regression :", round(pred_poly[0],2), "mpg")

print("\nExperiment Completed Successfully.")
