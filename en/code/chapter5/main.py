from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

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
