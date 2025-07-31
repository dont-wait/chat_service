from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request 

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {}
    )
