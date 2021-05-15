from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import joblib

app = Flask(__name__)
model = pickle.load(open("stroke_dataset_model.pkl"), "rb")

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # GENDER ----------------------------------------------
        gender = request.form["gender"]
        if(gender == "Male"):
            Male = 1
            Female = 0
            Other = 0

        elif (gender == "Female"):
            Male = 0
            Female = 1
            Other = 0
            
        elif (gender == "Other"):
            Male = 0
            Female = 0
            Other = 1

        else:
            Male = 0
            Female = 0
            Other = 0

        # HYPERTENSION ------------------------------------------
        hypertension = request.form["hypertension"]
        if (hypertension == "No"):
            No = 1
            Yes = 0

        elif (hypertension == "Yes"):       
            No = 0
            Yes = 1
        
        else:       
            No = 0
            Yes = 0


        # HEART_DISEASE ------------------------------------------
        heart_disease = request.form["heart_disease"]
        if (heart_disease== "No"):
            No = 1
            Yes = 0

        elif (heart_disease == "Yes"):       
            No = 0
            Yes = 1
        
        else:       
            No = 0
            Yes = 0

        # EVER_MARRIED ------------------------------------------
        ever_married = request.form["ever_married"]
        if (ever_married == "No"):
            No = 1
            Yes = 0

        elif (ever_married == "Yes"):       
            No = 0
            Yes = 1
        
        else:       
            No = 0
            Yes = 0

        # WORK_TYPE ------------------------------------------
        work_type = request.form["work_type"]
        if (work_type == "Private"):
            Private = 1
            Self_employed = 0
            Children = 0
            Government_job = 0
            Never_worked = 0

        elif (work_type == "Self-employed"):       
            Private = 0
            Self_employed = 1
            Children = 0
            Government_job = 0
            Never_worked = 0
        
        elif (work_type == "Children"):       
            Private = 0
            Self_employed = 0
            Children = 1
            Government_job = 0
            Never_worked = 0
        
        elif (work_type == "Government job"):       
            Private = 0
            Self_employed = 0
            Children = 0
            Government_job = 1
            Never_worked = 0
        
        elif (work_type == "Never worked"):       
            Private = 0
            Self_employed = 0
            Children = 0
            Government_job = 0
            Never_worked = 1
       
        else:       
            Private = 0
            Self_employed = 0
            Children = 0
            Government_job = 0
            Never_worked = 0

        # RESIDENCE TYPE------------------------------------------
        Residence_type = request.form["residence_type"]
        if (Residence_type == "Rural"):
            Rural = 1
            Urban = 0

        elif (Residence_type == "Urban"):       
            Rural = 0
            Urban = 1
        
        else:       
            No = 0
            Yes = 0
        

        # AVG GLUCOSE LEVEL ------------------------------------------
        avg_glucose_lvl = int(request.form["avg_glucose_level"])

        # BMI ------------------------------------------
        bmi = int(request.form["bmi"])

        # SMOKING STATUS ------------------------------------------
        smoking_status = request.form["smoking_status"]
        if (work_type == "never smoked"):
            never_smoked = 1
            Unknown = 0
            formerly_smoked = 0
            smokes = 0
            

        elif (work_type == "Unknown"):       
            never_smoked = 0
            Unknown = 1
            formerly_smoked = 0
            smokes = 0
        
        elif (work_type == "formerly smoked"):       
            never_smoked = 0
            Unknown = 0
            formerly_smoked = 1
            smokes = 0
        
        elif (work_type == "smokes"):       
            never_smoked = 0
            Unknown = 0
            formerly_smoked = 0
            smokes = 1
       
        else:       
            never_smoked = 0
            Unknown = 0
            formerly_smoked = 0
            smokes = 0

        prediction=model.predict([[
            gender, 
            age,
            hypertension,
            heart_disease,
            ever_married,
            work_type, 
            Residence_type,
            avg_glucose_level,
            bmi,
            smoking_status
        ]])

        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Stroke: {}".format(output))


    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)