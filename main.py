
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


items = {}

# CREATE
@app.post("/items")
async def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, "item": item}



# READ
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})



# UPDATE
@app.get("/items/{item_id}")
async def update_item(item_id: int, item:Item):
    if item_id in items:
        items[item_id] = item
        return {"message": 'Item updated', "items": item}
    return {"error": "Item not found"}



# Delete
@app.get("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items:
        deleted_item = items.pop(item_id)
        return {"message": 'Item deleted', "item": deleted_item}

    return {"error": "Item not found"}




# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.post("/greet")
# async def greet_user(name: str):
#     return {"message": f"Hello, {name}!"}


