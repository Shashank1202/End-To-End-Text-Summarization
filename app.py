from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import Response
from textSummarizer.pipeline.preditction import PredictionPipeline


#initialing fastAPi

text: str= "What is the text summarization?"

app= FastAPI()

@app.get("/", tags= ["authentication"])
async def index():
    return RedirectResponse(url="/doc")

@app.get("/train")
async def training():
    try:
        os.system("Python main.py")
        return Response("Training Successful !!")
    
    except Exception as e:
        return Response(f"Error Occured ! {e}")
    

@app.post("/predict")
async def predict_route(text):
    try:
        obj= PredictionPipeline()
        text= obj.predict(text)
    except Exception as e:
        raise e
    
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port= 8080)