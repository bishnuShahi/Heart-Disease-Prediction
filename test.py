from django.shortcuts import render
from django.http import Http404, JsonResponse
import pandas as pd
import numpy as np
from scipy.stats import boxcox
from sklearn.preprocessing import StandardScaler
import joblib

model = joblib.load('C:/Users/frank/OneDrive/Desktop/MAJOR PROJECT/Project/Interface/svm_model.sav')
lambdas = np.load('C:/Users/frank/OneDrive/Desktop/MAJOR PROJECT/Project/Interface/lambda_values.npz')

all_categories = {
    'cp': [1, 2, 3], 
    'restecg': [1, 2], 
    'thal': [1, 2, 3] 
}

def preprocess(data, categorical_data):

    print(f"Converting 'Oldpeak' from {data['oldpeak'].dtype} to Float")
    data['oldpeak'] = data['oldpeak'].astype(float)
    print(f"Converted 'Oldpeak' to {data['oldpeak'].dtype}")


    for col in data.columns:
        if col != 'oldpeak':
            print(f"Converting '{col}' from {data[col].dtype} to int")
            data[col] = data[col].astype(int)
            print(f"Converted '{col}' to {data[col].dtype}")

    print("Converted datatypes")
    print(data.dtypes)

    continuous_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

    for feature, categories in all_categories.items():
        for category in categories:
            if (f"{feature}_{category}" not in data.columns):
                data[f"{feature}_{category}"] = 0



    # preprocessed_data_encoded = preprocessed_data_encoded.reindex(sorted(preprocessed_data_encoded.columns), axis=1)
    
    # preprocessed_data_encoded['oldpeak'] += 0.0001

    # for col, lambda_val in lambdas.items():
    #     preprocessed_data_encoded[col] = boxcox(preprocessed_data_encoded[col], lmbda=lambda_val)

    return data

data = {
    'age': ['34'],
    'sex': ['1'],
    'trestbps': ['120'],
    'chol': ['120'],
    'fbs': ['1'],
    'thalach': ['160'],
    'exang': ['0'],
    'oldpeak': ['1'],
    'slope': ['1'],
    'ca': ['2'],
}

categorical_data = {
    'restecg': '1',
    'cp': '1',
    'thal': '1'
}

# df = pd.DataFrame(data, categorical_data)

# pre_df = preprocess(df)

# print(pre_df.head(1).T)


# Define the column names and their corresponding data types
columns = ['age', 'sex', 'trestbps', 'chol', 'fbs', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'cp_1', 'cp_2', 'cp_3', 'restecg_1', 'restecg_2', 'thal_1', 'thal_2', 'thal_3']
dtypes = {'age': 'int64', 'sex': 'int32', 'trestbps': 'int64', 'chol': 'int64', 'fbs': 'int32', 'thalach': 'int64', 'exang': 'int32', 'oldpeak': 'float64', 'slope': 'int32', 'ca': 'int32', 'cp_1': 'int32', 'cp_2': 'int32', 'cp_3': 'int32', 'restecg_1': 'int32', 'restecg_2': 'int32', 'thal_1': 'int32', 'thal_2': 'int32', 'thal_3': 'int32'}

# Create an empty DataFrame with specified columns
df = pd.DataFrame(columns=columns)

# Set the data types for each column
df = df.astype(dtypes)

print(df.dtypes)
