from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import Tools
from sqlmodel import Field, Session, SQLModel, create_engine, select

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/save-tool")
def save_tool(tool: Tools):
    tool1 = Tools(title=tool.title, room=tool.room, type=tool.type,)
    with Session(engine) as session:
        session.add(tool1)
        session.commit()

@app.get("/db-tools")
def get_tools():
    tools_list = []
    with Session(engine) as session:
        tools= session.exec(select(Tools))
        
        for tool in tools:
            tools_list.append({"id": tool.id, "title": tool.title, "room": tool.room, "type": tool.type})

        return tools_list
    
# @app.delete("/delete-tool")
# def delete_tool(tool: Tools):
#     with Session(engine) as session:
#         session.add(tool1)
#         session.commit()

@app.get("/delete-tool/{item_id}")
def delete_tool(item_id: int):   
    with Session(engine) as session:
        statement = select(Tools).where(Tools.id == item_id)
        results = session.exec(statement)
        hero = results.one()
        print("Tool: ", hero)

        session.delete(hero)
        session.commit()