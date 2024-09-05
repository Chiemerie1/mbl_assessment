from fastapi import FastAPI
from .utils import priority_pred
from .schemas import TextInput


app = FastAPI()


@app.post("/predict")
def make_predictions(payload: TextInput):

    if payload.text == "":
        return {
            "message": "Easy, give me a hand here"
        }
    else:
        prediction = priority_pred(payload.text)
        return {
            "prediction": prediction
        }