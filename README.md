# DWDB-ECT
 
# 📊 Loan Prediction Data Preprocessing with ECT

This project demonstrates **Extraction, Cleansing, and Transformation (ECT)** of a real-world dataset using **NumPy** and **Pandas**, preparing it for data analysis or pushing it to a **Data Warehouse (DW)**.

---

## 📁 Dataset

- **Source:** [Kaggle - Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)
- **File Used:** `loan_train.csv`
- **Records:** 614 rows × 13 columns

---

## 🔍 What is ECT?

**ECT** stands for:

- **Extraction:** Reading and loading raw data from files or databases.
- **Cleansing:** Handling missing values, formatting issues, and inconsistent data.
- **Transformation:** Creating new features, encoding categories, and preparing data for analysis or modeling.

---

## 🧠 Libraries Used

### NumPy
NumPy is a Python library used for numerical operations and working with arrays. It provides high-performance data structures and mathematical functions to manipulate numerical data efficiently.

### Pandas
Pandas is a Python library designed for data manipulation and analysis. It provides two core data structures: `Series` and `DataFrame`, which make it easy to clean, analyze, and transform tabular data.

---

## 🛠️ Steps Performed

### 1. **Extraction**
- Loaded dataset using `pd.read_csv()` from pandas.

### 2. **Cleansing**
- Filled missing values using:
  - Mode for categorical variables (e.g., `Gender`, `Married`)
  - Median for numerical values (e.g., `LoanAmount`)
- Converted `Dependents` column's '3+' into integer `3`.

### 3. **Transformation**
- Engineered a new feature: `TotalIncome = ApplicantIncome + CoapplicantIncome`
- Applied one-hot encoding to categorical columns.
- Converted target variable `Loan_Status` from `Y/N` to `1/0`.

---

## 📜 Code

```python
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('loan_train.csv')

# Fill missing values
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Married'].fillna(df['Married'].mode()[0], inplace=True)
df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

# Transform Dependents
df['Dependents'].replace('3+', 3, inplace=True)
df['Dependents'] = df['Dependents'].astype(int)

# Create new feature
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

# Encode categorical variables
df = pd.get_dummies(df, columns=[
    'Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area'
], drop_first=True)

# Encode target variable
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

# Save transformed data
df.to_csv('processed_loan_data.csv', index=False)



| Loan_ID  | ApplicantIncome | CoapplicantIncome | LoanAmount | TotalIncome | Loan_Status | Gender_Male | Married_Yes | Education_Not Graduate | Self_Employed_Yes | Property_Area_Semiurban | Property_Area_Urban |
|----------|------------------|-------------------|------------|-------------|-------------|-------------|-------------|-------------------------|--------------------|---------------------------|----------------------|
| LP001002 | 5849             | 0.0               | 128.0      | 5849.0      | 1           | 1           | 0           | 0                       | 0                  | 0                         | 1                    |
| LP001003 | 4583             | 1508.0            | 128.0      | 6091.0      | 0           | 1           | 1           | 0                       | 0                  | 0                         | 1                    |
| LP001005 | 3000             | 0.0               | 66.0       | 3000.0      | 1           | 1           | 1           | 1                       | 0                  | 0                         | 1                    |
| LP001006 | 2583             | 2358.0            | 120.0      | 4941.0      | 1           | 1           | 1           | 0                       | 1                  | 1                         | 0                    |
| LP001008 | 6000             | 0.0               | 141.0      | 6000.0      | 1           | 1           | 1           | 0                       | 0                  | 0                         | 1                    |
