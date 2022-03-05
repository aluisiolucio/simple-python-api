from datetime import date
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse
from src.service.people import get_people, post_people

app = FastAPI()


@app.post("/people", status_code=status.HTTP_201_CREATED)
async def post(name: str = Form(...), age: str = Form(...), birthday: date = Form(...)):
    form = {
        "name": name,
        "age": age,
        "birthday": birthday
    }

    return post_people(form)


@app.get("/")
async def get(request: Request, response_class=HTMLResponse):
    return get_people(request)
