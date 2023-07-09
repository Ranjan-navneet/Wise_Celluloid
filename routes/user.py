from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter()
data=[]

@user.get("/")
async def read_data():
   return {"hellooooo"}


@user.post("/")
async def write_data(user: User):
    data.append(user.dict())
    return data

@user.get("/{id}")
async def read_data(id: int):
    return data[id]


@user.put("/user/{id}")
async def update_data(id: int ,user: User):
    data[id] = user
    return data


@user.delete("/delete/user/{id}")
async def delete_data(id : int):
    data.pop(id)
    return data