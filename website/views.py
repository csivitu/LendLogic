import pandas as pd
import joblib
from flask import Flask,Blueprint,render_template,session,request,redirect,url_for,flash
views = Blueprint('views', __name__)

@views.route("/")
def form():
    return render_template("form.html")

@views.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        gender = request.form["gender"]
        married = request.form["married"]
        dependents = request.form["dependents"]
        education = request.form["education"]
        self_employed = request.form["self_employed"]
        applicant_income = request.form["applicant_income"]
        coapplicant_income = request.form["coapplicant_income"]
        loan_amount = request.form["loan_amount"]
        loan_amount_term = request.form["loan_amount_term"]
        credit_history = request.form["credit_history"]
        property_area = request.form["property_area"]

        responses = {
            "Gender": gender,
            "Married": married,
            "Dependents": dependents,
            "Education": education,
            "Self-Employed": self_employed,
            "Applicant Income": applicant_income,
            "Co-Applicant Income": coapplicant_income,
            "Loan Amount": loan_amount,
            "Loan Amount Term": loan_amount_term,
            "Credit History": credit_history,
            "Property Area": property_area,
        }

        input_data = pd.DataFrame({
            'ApplicantIncome': [0],
            'CoapplicantIncome': [0],
            'LoanAmount': [0],
            'Loan_Amount_Term': [0],
            'Credit_History': [0],
            'Gender_Male': [False],
            'Married_Yes': [False],
            'Dependents_0': [False],
            'Dependents_1': [False],
            'Dependents_2': [False],
            'Dependents_3+': [False],
            'Education_Graduate': [False],
            'Self_Employed_Yes': [False],
            'Property_Area_Rural': [False],
            'Property_Area_Semiurban': [False],
            'Property_Area_Urban': [False],
        })

        input_data['ApplicantIncome'] = applicant_income
        input_data['CoapplicantIncome'] = coapplicant_income
        input_data['LoanAmount'] = loan_amount
        input_data['Loan_Amount_Term'] = loan_amount_term
        if credit_history == "1":
            input_data['Credit_History'] = 1
        if gender == "Male":
            input_data['Gender_Male'] = True
        if married == "Yes":
            input_data['Married_Yes'] = True
        if dependents == "0":
            input_data['Dependents_0'] = True
        if dependents == "1":
            input_data['Dependents_1'] = True
        if dependents == "2":
            input_data['Dependents_2'] = True
        if dependents == "3+":
            input_data['Dependents_3+'] = True
        if education == "Graduate":
            input_data['Education_Graduate'] = True
        if self_employed == "Yes":
            input_data['Self_Employed_Yes'] = True
        if property_area == "Rural":
            input_data['Property_Area_Rural'] = True
        if property_area == "Semiurban":
            input_data['Property_Area_Semiurban'] = True
        if property_area == "Urban":
            input_data['Property_Area_Urban'] = True
        
        loan_model = joblib.load('loanmodel.pkl')
        predict = loan_model.predict(input_data)
        if predict == [True]:
            prediction = "APPROVED"
        else:
            prediction = "REJECTED"
        return render_template("predict.html", responses=responses,prediction=prediction)
