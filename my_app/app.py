from fastapi import FastAPI
from controller.LoadModel import LoadModel
from controller.GetPredictions import GetPredictions

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

model_path = "model/youtube_comments_spam_detection_model.pkl"
model = LoadModel(model_path)

@app.get("/youtube_comments_spam_detection")
def spam_detection(comment:str):

    pred = GetPredictions(model, comment)

    return {"Prediction": pred}