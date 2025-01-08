
'''
docker image build -t svm /Users/tmuth/MODELS/Docker_containers/three_models/svm
docker run --name svm_container -p 80:80 -v ${pwd}:/src/code --rm svm
'''
import pandas as pd 
import numpy as np 
import joblib
from fastapi import FastAPI

from pydantic import BaseModel
from enum import Enum
from datetime import datetime
class QueryInput(BaseModel):
    x1: int
    x2: int

model = joblib.load("../SVM_model.joblib")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to One-Class SVM endpoint"}


@app.post("/predict/")
def predict(data: QueryInput):
    features = np.array([data.x1, data.x2]).reshape(1,-1)
    prediction = model.predict(features)
    return f"SVM output is {int(prediction)}"


