import pickle
from pathlib import Path
import pandas as pd

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/milkqty-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)
    
classes = ['High', 'Low', 'Medium']

def make_predictions(data):
    input_data = pd.DataFrame([data.dict().values()], 
                                           columns=data.dict().keys())
    predictions = model.predict(input_data)
    return classes[predictions[0]]