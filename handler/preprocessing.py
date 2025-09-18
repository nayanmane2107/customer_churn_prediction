import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import SMOTE
import joblib
import os

def preprocess_data(df):
    df.drop('customerID', axis=1, inplace=True)

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].mean())

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    return df

def scale_features(X_train, X_test, num_cols, save_scaler=True, scaler_path='models/scaler.pkl'):
    scaler = StandardScaler()

    X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
    X_test[num_cols] = scaler.transform(X_test[num_cols])

    # Save the scaler
    if save_scaler:
        os.makedirs(os.path.dirname(scaler_path), exist_ok=True)
        joblib.dump(scaler, scaler_path)
        print(f"Scaler saved to {scaler_path}")

    return X_train, X_test

def balance_data_smote(X_train, y_train):
    
    smote = SMOTE(random_state=1)
    
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
    return X_train_res, y_train_res