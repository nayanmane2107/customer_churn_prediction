from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from handler.chat_endpoint import generate_retention_email

app = FastAPI(title="Churn Prediction API")

# Pydantic model matching your test data
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: float
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# Load model on startup
model = None

@app.on_event("startup")
async def load_model():
    global model
    try:
        model = joblib.load('models/xgboost_model.pkl')
        print("✅ Model loaded successfully!")
    except Exception as e:
        print(f"⚠️ Could not load model: {e}")

def preprocess_customer_data(data: CustomerData):
    """Convert customer data to model input format"""
    df = pd.DataFrame([data.model_dump()])
    
    # Categorical mappings (same as training)
    mappings = {
        'gender': {'Male': 1, 'Female': 0},
        'Partner': {'Yes': 1, 'No': 0},
        'Dependents': {'Yes': 1, 'No': 0},
        'PhoneService': {'Yes': 1, 'No': 0},
        'MultipleLines': {'Yes': 2, 'No': 0, 'No phone service': 1},
        'InternetService': {'DSL': 0, 'Fiber optic': 1, 'No': 2},
        'OnlineSecurity': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'OnlineBackup': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'DeviceProtection': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'TechSupport': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'StreamingTV': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'StreamingMovies': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'Contract': {'Month-to-month': 0, 'One year': 1, 'Two year': 2},
        'PaperlessBilling': {'Yes': 1, 'No': 0},
        'PaymentMethod': {
            'Electronic check': 0, 
            'Mailed check': 1, 
            'Bank transfer (automatic)': 2, 
            'Credit card (automatic)': 3
        }
    }
    
    # Apply encodings
    for col, mapping in mappings.items():
        if col in df.columns:
            df[col] = df[col].map(mapping).fillna(0)
    
    return df.values

@app.post("/predict_churn")
async def predict_churn(customer: CustomerData):
    """Single route: Accept customer data, predict, return if churn or not"""
    
    # Check if model is loaded
    if model is None:
        raise HTTPException(status_code=503, detail="Model not available")
    
    try:
        # Preprocess the input data
        processed_data = preprocess_customer_data(customer)
        
        # Make prediction
        prediction = model.predict(processed_data)[0]
        probability = model.predict_proba(processed_data)[0][1]

        print(prediction)
        
        # Return simple churn result
        result = "CHURN" if prediction == 1 else "NO CHURN"
        
        return {
            "prediction": result,
            "probability": round(float(probability), 3),
            "will_churn": bool(prediction == 1)
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")

@app.post("/get_retention_email")
async def get_retention_email(customer: CustomerData):
    """Single route: Accept customer data, predict, return if churn or not"""

    # Check if model is loaded
    if model is None:
        raise HTTPException(status_code=503, detail="Model not available")
    
    try:
        # Preprocess the input data
        processed_data = preprocess_customer_data(customer)
        
        # Make prediction
        prediction = model.predict(processed_data)[0]
        result = True if prediction == 1 else False

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")

    if result:
        email = generate_retention_email(result)
    else:
        email = "Customer is not predicted to churn. No retention email needed."

    return {"retention_email": email}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)