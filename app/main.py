from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import make_predictions

app = FastAPI()

class MilkQtyData(BaseModel):
    PH: float
    Temperature: int
    Taste: int
    Odor: int
    Fat: int
    Turbidity: int
    Colour: int

@app.get('/')
def home():
    return {"health_check": "OK"}

@app.post("/predict")
def predict_milk_qty(data: MilkQtyData):
    response = make_predictions(data)
    return {"Milk Quality": response}