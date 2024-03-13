from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.post("/")
async def post():
    return {"message": "Hello from post route"}


@app.get("/items")
async def list_items():
    return {"message": "List Items Route"}


# with Path Param
@app.get("/items/{item_id}")
async def get_list_by_id(item_id: int):
    return {"message": f"List Item {item_id}"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you're healthy"}
    if food_name == FoodEnum.fruits:
        return {"food_name": food_name, "message": "you're still healthy but like sweet things"}

    return {"food_name": food_name, "message": "I like chocolate milk"}
