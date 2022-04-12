from flask import Flask, request
from flasgger import Swagger
from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)
Swagger(app)

pickled_model = open('pickle_diabetes.pkl','rb')
regression = pickle.load(pickled_model)

@app.route('/')
def home():
    return 'Know Diabetes Outcome'

@app.route('/predict')
def predict_diabetes():
    
    """Lets try the Swagger from Flasgger
    ---
    parameters: 
        - name: age
          in: query
          type: number
          required: true
        - name: sex
          in: query
          type: number
          required: true
        - name: bmi
          in: query
          type: number
          required: true
    responses: 
        200: 
            description: The outcome is
    """
    age = request.args.get('age')
    sex = request.args.get('sex')
    bmi = request.args.get('bmi')

    result = regression.predict([[age,sex,bmi]])


    return f'Diabetes is {result}'

if __name__ == "__main__":
    app.run(debug = True)