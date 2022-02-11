from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.post("/postItem")
def post_item(item: Item):
    return {"item": item}


@app.post("/postItem/ItemName")
def give_Blogname(item: Item):
    return {"item": f" itemName is {item.name}"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
        <html>
            <head>
                <title>Vision X Backend APIII Server</title>
            </head>
            <body>
                <div style="width:800px; margin:0 auto;">
                  
                    <h1> Backend APIII Server</h1>
                    This is a backend API server, please get the API token then use these APIs.</br>
                    If you want to get the detail, please reference "http://host-ip:8000/docs".</br>
                    Remember to change the host ip address.</br>
                </div>
            </body>
        </html>
    """
# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=9000)
