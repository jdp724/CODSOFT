# -*- coding: utf-8 -*-
"""Task-3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QDg2wbnl2PmmvWboreSQe7ghkHJM8i0I
"""

from google.colab import files
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Upload the file
uploaded = files.upload()

# Load the dataset into a DataFrame, handling potential parser errors
try:
    df = pd.read_csv('sales_data.csv')  # Ensure this matches the uploaded file name
except pd.errors.ParserError:
    print("Parser error encountered. Trying with different parameters.")
    try:
        df = pd.read_csv('sales_data.csv', delimiter=',', encoding='latin1', on_bad_lines='skip')
    except Exception as e:
        print(f"Failed to load the dataset. Error: {e}")

# Data preprocessing
df = df.dropna()  # Drop rows with missing values
X = df[['TV' , 'Radio', 'Newspaper','Sales']]
y = df['Sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model selection and training
model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print("Root Mean Squared Error:", rmse)

# Model interpretation
coefficients = pd.DataFrame({'feature': X.columns, 'coefficient': model.coef_})
print("Coefficients:")
print(coefficients)