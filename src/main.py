from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse("index.html", {"request": request, "text": "Hello World!"})
