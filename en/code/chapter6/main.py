from datetime import datetime

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, ValidationError

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

profiles = {
    "philipe": {
        "name": "Philipe Ackerman",
        "about": [
            "Hi! I'm a math professor, and a really good one at that.",
            "When I'm not teaching, you can find me cheering for my soccer team, Botafogo.",
        ],
        "skills": ["Math", "Having Long Hair", "Video Recording"],
        "email": "philipe@example.com",
    },
    "maria": {
        "name": "Maria Santos",
        "about": [
            "Software developer by day, guitarist by night.",
            "I believe code should be as elegant as music.",
        ],
        "skills": ["Python", "FastAPI", "Guitar", "Coffee Brewing"],
        "email": "maria@example.com",
    },
}


class GuestbookEntry(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    message: str = Field(min_length=1, max_length=500)


messages = []


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="profile.html",
        context={"profile": profiles["philipe"]},
    )


@app.get("/profile/{username}")
def show_profile(request: Request, username: str):
    """
    Display a user's profile page.

    - **username**: The unique username to look up
    """
    profile = profiles.get(username)
    if not profile:
        return templates.TemplateResponse(
            request=request,
            name="not_found.html",
            context={"username": username},
            status_code=404,
        )
    return templates.TemplateResponse(
        request=request,
        name="profile.html",
        context={"profile": profile},
    )


@app.get("/guestbook")
def show_guestbook(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="guestbook.html",
        context={"messages": messages},
    )


@app.post("/guestbook")
def handle_guestbook(request: Request, name: str = Form(), message: str = Form()):
    try:
        data = GuestbookEntry(name=name.strip(), message=message.strip())
    except ValidationError as e:
        errors = [err["msg"] for err in e.errors()]
        return templates.TemplateResponse(
            request=request,
            name="guestbook.html",
            context={
                "messages": messages,
                "errors": errors,
                "form_name": name,
                "form_message": message,
            },
        )

    messages.append({
        "name": data.name,
        "message": data.message,
        "time": datetime.now().strftime("%B %d, %Y at %I:%M %p"),
    })
    return RedirectResponse(url="/guestbook", status_code=303)


@app.post("/guestbook/delete/{index}")
def delete_message(index: int):
    if 0 <= index < len(messages):
        messages.pop(index)
    return RedirectResponse(url="/guestbook", status_code=303)
