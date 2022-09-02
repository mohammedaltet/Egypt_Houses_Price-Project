import joblib
from flask import Flask, render_template, request
import preprocess  
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load('Models/model.h5')


@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET']) 
def get_prediction() :
    if request.method == 'POST' :
        City = request.form['Location_City']
        Beds = request.form['Bed_Rooms']
        Baths = request.form['Bath_Rooms']
        Space = request.form['Home_Space_SQM']
        furnished = request.form['Furnished']
        Property = request.form['Property_Type']
        
    data = {'Location_City' : City, 'Bed_Rooms' : Beds, 'Bath_Rooms' : Baths, 'Home_Space_SQM' : Space, 'Furnished' : furnished, 'Property_Type' : Property}
    
    final_data = preprocess.preprocess_data(data)
    prediction = model.predict([final_data])[0]
    
    # return str(round(prediction))
    return render_template('prediction.html', Houes_predict = int(prediction))
       
        

if __name__ == '__main__' :
    app.run(debug = True)
