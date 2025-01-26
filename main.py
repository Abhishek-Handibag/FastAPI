from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

# command to activate venv: myenv\Scripts\activate
# command to run the fastapi server: uvicorn main:app --reload 
# here --reload make sure that each time we change the code our server gets restarted
# here we can replace the main with what ever is our file name
# by default the fastapi runs on the server 8000 


# pydantic is used for data validation
class Post(BaseModel):
    title: str
    content: str
    published : bool = True # here if no value is provided its default is true
    rating : Optional[int] = None # this is fully optional field

app=FastAPI() # to create an instance of FASTAPI

@app.get("/") #app is reference to the fastapi app, and get is http method
# following is just the regular function and async means the function is called asynchronously.
async def root():
    return {"message":"Hello world"}

@app.get("/result")
async def result():
    return ("Hey buddy you passed")



#post request

@app.post("/create_post")
# here payload is the variable name to store the data sent by the user in the post requrest
# dict is the datatype of the variable (payload in this case)
# also we imported Body from fastapi.params

# async def create_post(payload: dict = Body(...)):
#     print(payload)
#     return {"message":"post created successfully"}


# now here it is automatically going to validate the data it receives from the client so it will check whether specified fields are there and its datatype is correct
async def create_post(new_post:Post): # here Post reference to the class post to validate datatype.
    print(new_post)
    return {"message":"post created successfully"}