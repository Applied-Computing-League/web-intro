from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

profile = {
    "name": "Philipe Ackerman",
    "about": [
        "Hi! I'm a math professor, and a really good one at that.",
        "When I'm not teaching, you can find me cheering for my soccer team, Botafogo.",
    ],
    "skills": ["Math", "Having a Long Hair", "Video Recording"],
}


@app.get("/", response_class=HTMLResponse)
def home():
    skills_html = "".join(f"<li>{skill}</li>" for skill in profile["skills"])
    about_html = "".join(f"<p>{para}</p>" for para in profile["about"])

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{profile["name"]} - Profile</title>
        <link rel="stylesheet" href="/static/profile.css">
    </head>
    <body>
        <header>
            <h1>{profile["name"]}</h1>
            <nav>
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
            </nav>
        </header>

        <main>
            <section id="about">
                <h2>About Me</h2>
                {about_html}
            </section>

            <section id="skills">
                <h2>Skills</h2>
                <ul>
                    {skills_html}
                </ul>
            </section>
        </main>

        <footer>
            <p>&copy; 2025 {profile["name"]}</p>
        </footer>
    </body>
    </html>
    """
