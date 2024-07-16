from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('LinearRegressionModel.pkl','rb'))
car= pd.read_csv("Final_dataset.csv")

@app.route('/',methods=['GET','POST'])
def index():
    companies= sorted(car['company'].unique())
    car_models= sorted(car['name'].unique())
    year= sorted(car['year'].unique(), reverse=True)
    fuel_types= sorted(car['fuel_type'].unique())
    companies.insert(0,"Select Company")
    return render_template('index.html', companies=companies, car_models=car_models, years= year
                           , fuel_type=fuel_types)

@app.route('/predict',methods=['POST'])
def predict():
    company = request.form.get('company', type=str)
    car_model = request.form.get('car_model',type=str)
    year = request.form.get('year', type=int)
    fuel_type = request.form.get('fuel_type',type=str)
    kms_driven = request.form.get('kms_driven', type=int)

    prediction = model.predict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]], 
                                          columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))
    print(prediction)
    return str(np.round(prediction[0],2))

if __name__=="__main__":
    app.run(debug=True)