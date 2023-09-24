from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from flask import render_template, request
from sklearn.preprocessing import MinMaxScaler

app = FastAPI()

model = joblib.load('loanmodel_decision_tree_pruned.pkl')

class InputData(BaseModel):
    ApplicantIncome: int
    CoapplicantIncome: int
    LoanAmount: int
    Loan_Amount_Term: int
    Credit_History: bool
    Gender_Male: bool
    Married_Yes: bool
    Dependents_0: bool
    Dependents_1: bool
    Dependents_2: bool
    Dependents_3plus: bool
    Education_Graduate: bool
    Self_Employed_Yes: bool
    Property_Area_Rural: bool
    Property_Area_Semiurban: bool
    Property_Area_Urban: bool

@app.post("/predict")
def predict(data: InputData):
    input_data = [[
        data.ApplicantIncome,
        data.CoapplicantIncome,
        data.LoanAmount,
        data.Loan_Amount_Term,
        data.Credit_History,
        int(data.Gender_Male),
        int(data.Married_Yes),
        int(data.Dependents_0),
        int(data.Dependents_1),
        int(data.Dependents_2),
        int(data.Dependents_3plus),
        int(data.Education_Graduate),
        int(data.Self_Employed_Yes),
        int(data.Property_Area_Rural),
        int(data.Property_Area_Semiurban),
        int(data.Property_Area_Urban),
    ]]

    #minmaxscaler
    scaler = MinMaxScaler()
    input_data = scaler.fit_transform(input_data)

    predictions = model.predict(input_data)

    return {"predictions": predictions.tolist()}

'''
{
    "ApplicantIncome": 4232,
    "CoapplicantIncome": 24,
    "LoanAmount": 10,
    "Loan_Amount_Term": 5,
    "Credit_History": 1, 
    "Gender_Male": true,
    "Married_Yes": false,
    "Dependents_0": true,
    "Dependents_1": false,
    "Dependents_2": true,
    "Dependents_3plus": false,
    "Education_Graduate": true,
    "Self_Employed_Yes": false,
    "Property_Area_Rural": true,
    "Property_Area_Semiurban": false,
    "Property_Area_Urban": true
}
'''