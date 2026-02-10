from datetime import datetime

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
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
    "lucas": {
        "name": "Lucas",
        "about": [
            "Applied math student at UFRJ and backend developer.",
            "Part of the computing team at the Applied Computing League.",
        ],
        "skills": ["Python", "FastAPI", "Docker", "Linux"],
        "email": "lucas@example.com",
    },
    "zico": {
        "name": "Zico",
        "about": [
            "Applied math student at UFRJ who likes low-level programming.",
            "Part of the computing team at the Applied Computing League.",
        ],
        "skills": ["Rust", "C", "Python", "Git"],
        "email": "zico@example.com",
    },
    "joao": {
        "name": "João",
        "about": [
            "Applied math student at UFRJ focused on data science.",
            "Part of the data science team at the Applied Computing League.",
        ],
        "skills": ["Python", "Pandas", "Machine Learning", "SQL"],
        "email": "joao@example.com",
    },
    "eduardo": {
        "name": "Eduardo",
        "about": [
            "Applied math student at UFRJ who turns data into insights.",
            "Part of the data science team at the Applied Computing League.",
        ],
        "skills": ["Python", "Data Visualization", "R", "Statistics"],
        "email": "eduardo@example.com",
    },
    "layza": {
        "name": "Layza",
        "about": [
            "Applied math student at UFRJ coordinating the league's projects.",
            "Part of the management team at the Applied Computing League.",
        ],
        "skills": ["Project Management", "Agile", "Data Analysis", "Leadership"],
        "email": "layza@example.com",
    },
    "arthur": {
        "name": "Arthur",
        "about": [
            "Applied math student at UFRJ working on AI engineering.",
            "Part of the computing team at the Applied Computing League.",
        ],
        "skills": ["Python", "Machine Learning", "LLMs", "AI Engineering"],
        "email": "arthur@example.com",
    },
    "matheus": {
        "name": "Matheus",
        "about": [
            "Applied math student at UFRJ interested in product and strategy.",
            "Part of the management team at the Applied Computing League.",
        ],
        "skills": ["Product Management", "UX Research", "Strategy", "Analytics"],
        "email": "matheus@example.com",
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
        name="home.html",
        context={"profiles": profiles},
    )


@app.get("/search")
def search(q: str = ""):
    results = {
        username: profile
        for username, profile in profiles.items()
        if q.lower() in profile["name"].lower()
    }
    return HTMLResponse(
        templates.get_template("partials/profile_results.html").render(
            profiles=results
        )
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
