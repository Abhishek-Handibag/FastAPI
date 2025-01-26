from fastapi import FastAPI

# command to activate venv: myenv\Scripts\activate
# command to run the fastapi server: uvicorn main:app --reload
# here we can replace the main with what ever is our file name
# by default the fastapi runs on the server 8000 

app=FastAPI() # to create an instance of FASTAPI

@app.get("/")
async def root():
    return {"message":"Hello world"}