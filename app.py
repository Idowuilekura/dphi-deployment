from flask import Flask,request,render_template,jsonify,url_for
import joblib
from sklearn.ensemble import GradientBoostingClassifier
import json
import pandas as pd
import numpy as np
with open('map_dict.json','r') as f:
    map_dict = json.load(f)
with open('gb_model.pickle','rb') as f:
    model_loaded = joblib.load(f)
app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/predict",methods=["POST"])
def predict():
    Gender = map_dict['Gender'][str(request.form['Gender'])]
    Married = map_dict['Married'][str(request.form['Married'])]
    Dependents = map_dict['Dependents'][str(request.form['Dependents'])]
    Education = map_dict['Education'][str(request.form['Education'])]
    Self_Employed = map_dict['Self_Employed'][str(request.form['Self_Employed'])]
    ApplicantIncome = float(request.form['ApplicantIncome'])
    CoapplicantIncome = float(request.form['CoapplicantIncome'])
    LoanAmount = float(request.form['LoanAmount'])
    Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
    Credit_History = float(request.form['Credit_History'])
    Property_Area = map_dict['Property_Area'][str(request.form['Property_Area'])]
    final_array = np.array([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])
    col = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    data_unseen = pd.DataFrame([final_array],columns=col)
    prediction = model_loaded.predict(data_unseen)[0]
    labels = {'0':'Rejected','1':'Accepted'}
    label = labels[str(prediction)]
    if label == 'Accepted':
        return render_template('home.html',pred=f'Congratulations your loan application was successful')
    else:
        return render_template('home.html',pred=f"Sorry your loan application was not successful")

@app.route('/predict_api',methods=['POST'])
def predict_api():
    cat_list = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed','Property_Area']
    data = request.get_json(force=True)
    for col in cat_list:
        data[col] = map_dict[col][data[col]]
    data_2 = pd.DataFrame([data])
    prediction = model_loaded.predict(data_2)[0]
    labels = {'0':'Rejected','1':'Accepted'}
    label = labels[str(prediction)]
    return jsonify(label)

if __name__=='__main__':
    app.run(debug=True)