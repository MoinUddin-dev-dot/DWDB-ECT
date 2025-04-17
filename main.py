# Required Libraries
import pandas as pd
import numpy as np

# Step 1: Data Extraction (Reading the Dataset)
df = pd.read_csv("Loan_Train.csv")  # Make sure the CSV file is in your working directory

# Step 2: Initial Data Info
print("Initial Data Shape:", df.shape)
print("Missing Values Before Cleaning:\n", df.isnull().sum())

# Step 3: Data Cleansing
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0])
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])


# Step 4: Data Transformation (Feature Engineering)
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']  # NumPy not needed here but okay
df['LoanAmount_log'] = np.log(df['LoanAmount'])

# Step 5: One-hot Encoding for Categorical Variables
df_encoded = pd.get_dummies(df, columns=['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area', 'Dependents'])

# Drop Unnecessary Columns
df_encoded.drop(['Loan_ID', 'ApplicantIncome', 'CoapplicantIncome'], axis=1, inplace=True)

# Step 6: Final Output
print("\nCleaned & Transformed Data Sample:")
print(df_encoded.head())

# Step 7: Ready to Push to Data Warehouse or ML Pipeline
print("\nFinal Data Shape:", df_encoded.shape)
