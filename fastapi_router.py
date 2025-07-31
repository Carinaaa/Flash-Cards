from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from qa_data import questions
from enum import Enum

app = FastAPI()

items = []

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str

'''Can also be async + await'''
@app.get("/")
async def root():
    return {"questions" : questions[0].get('question'),
            "answer" : questions[0].get('answer')}

@app.post("/items")
def create_item(item: Item):
    items.append(item.name)
    return items

@app.get("/items/{index}")
def read_item(index: int):
    if 0 <= index < len(items):
        return {"item": items[index]}
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}