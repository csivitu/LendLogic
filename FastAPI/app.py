from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from flask import render_template, request, jsonify

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

    predictions = model.predict(input_data)

    return {"predictions": predictions.tolist()}

@app.route("/predictapi", methods=["GET", "POST"])
def predictapi():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        data = request.form.to_dict()

        input_data = [[
            int(data["ApplicantIncome"]),
            int(data["CoapplicantIncome"]),
            int(data["LoanAmount"]),
            int(data["Loan_Amount_Term"]),
            int(data["Credit_History"]),
            int(data["Gender_Male"]),
            int(data["Married_Yes"]),
            int(data["Dependents_0"]),
            int(data["Dependents_1"]),
            int(data["Dependents_2"]),
            int(data["Dependents_3plus"]),
            int(data["Education_Graduate"]),
            int(data["Self_Employed_Yes"]),
            int(data["Property_Area_Rural"]),
            int(data["Property_Area_Semiurban"]),
            int(data["Property_Area_Urban"]),
        ]]

        predictions = model.predict(input_data)

        prediction = predictions[0]
        prediction_text = "The predicted loan status is {}".format("Approved" if prediction == 1 else "Denied")

        return render_template("predict.html", prediction_text=prediction_text)