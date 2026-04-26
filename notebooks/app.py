from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


class LoanInput(BaseModel):
    age: float
    income: float
    loan_amount: float
    credit_score: float
    years_employed: float
    education: int   # 0=bachelor, 1=high_school, 2=master


@app.get("/")
def home():
    return {"message": "Loan Prediction API is running"}


@app.post("/predict")
def predict(data: LoanInput):
    features = [[
        data.age, data.income, data.loan_amount,
        data.credit_score, data.years_employed, data.education
    ]]
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]

    return {
        "approved": bool(prediction),
        "probability": round(float(probability), 4)
    }