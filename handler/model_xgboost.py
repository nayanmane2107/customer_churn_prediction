from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import joblib
import os

def train_xgboost(X_train, y_train, save_path='models/xgboost_model.pkl'):
    model = XGBClassifier()
    model.fit(X_train, y_train)
    
    # Save the model
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(model, save_path)
    print(f"XGBoost model saved to {save_path}")
    
    return model

def load_xgboost_model(model_path='models/xgboost_model.pkl'):
    """Load a saved XGBoost model"""
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print(f"XGBoost model loaded from {model_path}")
        return model
    else:
        print(f"Model file not found: {model_path}")
        return None
