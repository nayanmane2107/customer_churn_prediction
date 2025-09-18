from handler.data_loading import load_data
from handler.preprocessing import preprocess_data, scale_features, balance_data_smote
from handler.model_xgboost import train_xgboost
from handler.evaluation import evaluate_model
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    # Load data
    df = load_data('data/Vodafone_Customer_Churn_Sample_Dataset.csv')
    
    # Preprocess data
    df = preprocess_data(df)
    X = df.drop(columns=['Churn'])
    y = df['Churn'].values
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40, stratify=y)
    num_cols = ["tenure", 'MonthlyCharges', 'TotalCharges']
    X_train, X_test = scale_features(X_train, X_test, num_cols)
    
    # Train and Save XGBoost Model
    print("--- XGBoost Model ---")
    X_train, y_train = balance_data_smote(X_train, y_train)
    xgb_model = train_xgboost(X_train, y_train)
    evaluate_model(xgb_model, X_test, y_test)