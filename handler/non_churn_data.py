# Sample data for customers who are unlikely to churn (NO CHURN)
# These are stable, long-term customers with low churn risk

# Example 1: Long-term family customer - no churn
stable_family_customer = {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "Yes",
    "tenure": 60.0,
    "PhoneService": "Yes",
    "MultipleLines": "Yes",
    "InternetService": "DSL",
    "OnlineSecurity": "Yes",
    "OnlineBackup": "Yes",
    "DeviceProtection": "Yes",
    "TechSupport": "Yes",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Two year",
    "PaperlessBilling": "No",
    "PaymentMethod": "Credit card (automatic)",
    "MonthlyCharges": 65.75,
    "TotalCharges": 3945.00
}

# Example 2: Loyal customer with automatic payments - No churn
loyal_customer = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 48.0,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "Yes",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "Yes",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Two year",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Bank transfer (automatic)",
    "MonthlyCharges": 89.10,
    "TotalCharges": 4276.80
}

# Example 3: Senior with good services - churn
senior_stable_customer = {
    "gender": "Male",
    "SeniorCitizen": 1,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 36.0,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "Yes",
    "OnlineBackup": "Yes",
    "DeviceProtection": "Yes",
    "TechSupport": "Yes",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "One year",
    "PaperlessBilling": "No",
    "PaymentMethod": "Bank transfer (automatic)",
    "MonthlyCharges": 55.20,
    "TotalCharges": 1987.20
}

# Example 4: Basic phone service loyal customer
phone_only_loyal = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "No",
    "Dependents": "No",
    "tenure": 72.0,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "No",
    "OnlineSecurity": "No internet service",
    "OnlineBackup": "No internet service",
    "DeviceProtection": "No internet service",
    "TechSupport": "No internet service",
    "StreamingTV": "No internet service",
    "StreamingMovies": "No internet service",
    "Contract": "Two year",
    "PaperlessBilling": "No",
    "PaymentMethod": "Credit card (automatic)",
    "MonthlyCharges": 20.05,
    "TotalCharges": 1443.60
}

# Example 5: Young professional with good contract
young_professional = {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "No",
    "Dependents": "No",
    "tenure": 24.0,
    "PhoneService": "Yes",
    "MultipleLines": "Yes",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "Yes",
    "OnlineBackup": "No",
    "DeviceProtection": "Yes",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "One year",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Credit card (automatic)",
    "MonthlyCharges": 95.50,
    "TotalCharges": 2292.00
}

# All non-churn customers in a list for easy testing
non_churn_customers = [
    stable_family_customer,
    loyal_customer,
    senior_stable_customer,
    phone_only_loyal,
    young_professional
]