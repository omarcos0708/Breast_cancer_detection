import pickle
import uvicorn
import pandas as pd
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

# Inicia API
app = FastAPI()

# Carrega modelo
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Cria página inicial
@app.get('/')
def home():
    return 'Welcome to the Medical Insurance Prediction App!'

# Classifica custo (consumo do modelo)
@app.get('/predict')
def predict(radius_mean: float,
    texture_mean: float,
    perimeter_mean: float,
    area_mean: float,
    smoothness_mean: float,
    compactness_mean: float,
    concavity_mean: float,
    concavepoints_mean:float,
    symmetry_mean: float,
    fractal_dimension_mean: float):

    df_input = pd.DataFrame([dict(radius_mean=radius_mean,
    texture_mean=texture_mean,
    perimeter_mean=perimeter_mean,
    area_mean=area_mean,
    smoothness_mean=smoothness_mean,
    compactness_mean=compactness_mean,
    concavity_mean=concavity_mean,
    concavepoints_mean=concavepoints_mean,
    symmetry_mean=symmetry_mean,
    fractal_dimension_mean=fractal_dimension_mean)])
    output = model.predict(df_input)[0]
    return output

class Customer(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concavepoints_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    class Config:
        schema_extra = {
            'example': {
                "radius_mean": 17.99,
                "texture_mean": 10.38,
                "perimeter_mean": 122.8,
                "area_mean": 1001,
                "smoothness_mean": 0.1184,
                "compactness_mean": 0.2776,
                "concavity_mean": 0.3001,
                "concavepoints_mean": 0.1471,
                "symmetry_mean": 0.2419,
                "fractal_dimension_mean": 0.07871,
            }
        }

@app.post('/predict_with_json')
def predict(data: Customer):
    df_input = pd.DataFrame([data.dict()])
    output = model.predict(df_input)[0]
    return output

class CustomerList(BaseModel):
    data: List[Customer]

@app.post('/mult_predict_with_json')
def predict(data: CustomerList):
    df_input = pd.DataFrame(data.dict()['data'])
    output = model.predict(df_input).tolist()
    return output

# Executa API
if __name__ == '__main__':
    uvicorn.run(app)
