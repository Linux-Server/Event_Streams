from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def one():
    return "hello service one"
