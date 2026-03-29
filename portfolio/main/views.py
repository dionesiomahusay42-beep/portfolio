from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm


# ─── Portfolio Data ────────────────────────────────────────────────────────────
# Edit all values below to personalize your portfolio

OWNER = {
    "name": "Dionesio Mahusay Jr.",
    "tagline": "Full-Stack Developer · Problem Solver · Tech Enthusiast",
    "short_bio": "Hi! I'm a passionate developer based in the Philippines, "
                 "building web applications that make an impact.",
    "about": (
        "I'm a Computer Science graduate with a deep love for backend systems "
        "and clean, maintainable code. Over the years I've worked with Python, "
        "Django, JavaScript, and a handful of cloud platforms. I enjoy turning "
        "complex business problems into elegant software solutions and am always "
        "eager to learn new technologies."
    ),
    "career_goals": (
        "My goal is to grow into a senior full-stack engineer and eventually "
        "lead engineering teams that ship products people genuinely love. "
        "I'm especially interested in SaaS products, developer tooling, and "
        "anything that improves developer experience."
    ),
    "email": "yourname@email.com",
    "github": "https://github.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourusername",
    "twitter": "https://twitter.com/yourusername",
    "profile_photo": None,   # Set to a URL string or leave None for initials avatar
}

SKILLS = [
    # (skill_name, proficiency_percent, category)
    ("Python",          90, "backend"),
    ("Django",          85, "backend"),
    ("JavaScript",      75, "frontend"),
    ("HTML & CSS",      80, "frontend"),
    ("PostgreSQL",      70, "database"),
    ("SQLite",          75, "database"),
    ("Git & GitHub",    85, "tools"),
    ("REST APIs",       80, "backend"),
    ("Bootstrap",       70, "frontend"),
    ("Linux / CLI",     65, "tools"),
    ("Docker",          55, "tools"),
    ("PythonAnywhere",  80, "tools"),
]

PROJECTS = [
    {
        "title": "Personal Portfolio Website",
        "description": (
            "A responsive portfolio website built with Django and deployed "
            "on PythonAnywhere. Features a contact form, dynamic project "
            "listings, and a clean modern design."
        ),
        "tech": ["Python", "Django", "HTML/CSS", "Bootstrap", "SQLite"],
        "github": "https://github.com/yourusername/portfolio",
        "live": "https://firstname_lastname.pythonanywhere.com",
        "emoji": "🌐",
    },
    {
        "title": "Task Management API",
        "description": (
            "A RESTful API built with Django REST Framework that allows users "
            "to create, update, and track tasks. Includes JWT authentication "
            "and full CRUD operations."
        ),
        "tech": ["Python", "Django REST Framework", "JWT", "PostgreSQL"],
        "github": "https://github.com/dionesiomahusay42-beep/task-api",
        "live": None,
        "emoji": "✅",
    },
    {
        "title": "Weather Dashboard",
        "description": (
            "A weather app that fetches real-time data from the OpenWeatherMap "
            "API and displays forecasts, humidity, and wind speed for any city "
            "in the world. Built with vanilla JavaScript and Django backend."
        ),
        "tech": ["JavaScript", "Python", "Django", "OpenWeatherMap API", "CSS"],
        "github": "https://github.com/yourusername/weather-dashboard",
        "live": None,
        "emoji": "🌤️",
    },
    {
        "title": "Blog Platform",
        "description": (
            "A full-featured blog platform with user authentication, rich text "
            "editing, categories, tags, and a comment system. Supports Markdown "
            "content and is fully mobile-responsive."
        ),
        "tech": ["Python", "Django", "Markdown", "SQLite", "Bootstrap"],
        "github": "https://github.com/dionesiomahusay42-beep/blog-platform",
        "live": None,
        "emoji": "📝",
    },
]

EDUCATION = [
    {
        "school": "University of the Philippines",
        "degree": "Bachelor of Science in Computer Science",
        "year": "2020 – 2024",
        "description": "Graduated with honors. Relevant coursework: Data Structures, "
                       "Algorithms, Web Development, Database Systems, Software Engineering.",
    },
    {
        "school": "NEGROS OCCIDENTAL HIGH SCHOOL",
        "degree": "Senior High School – CSS Strand",
        "year": "2018 – 2020",
        "description": "Completed the Science, Technology, Engineering, and Mathematics strand.",
    },
]
# ──────────────────────────────────────────────────────────────────────────────


def home(request):
    context = {"owner": OWNER, "skills": SKILLS[:6], "projects": PROJECTS[:3]}
    return render(request, "portfolio/home.html", context)


def about(request):
    context = {"owner": OWNER}
    return render(request, "portfolio/about.html", context)


def skills(request):
    backend  = [(s, p) for s, p, c in SKILLS if c == "backend"]
    frontend = [(s, p) for s, p, c in SKILLS if c == "frontend"]
    database = [(s, p) for s, p, c in SKILLS if c == "database"]
    tools    = [(s, p) for s, p, c in SKILLS if c == "tools"]
    context  = {
        "owner": OWNER,
        "backend": backend, "frontend": frontend,
        "database": database, "tools": tools,
        "all_skills": SKILLS,
    }
    return render(request, "portfolio/skills.html", context)


def projects(request):
    context = {"owner": OWNER, "projects": PROJECTS}
    return render(request, "portfolio/projects.html", context)


def education(request):
    context = {"owner": OWNER, "education": EDUCATION}
    return render(request, "portfolio/education.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            messages.success(request, "✅ Your message has been sent! I'll get back to you soon.")
            return redirect("contact")
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = ContactForm()
    context = {"owner": OWNER, "form": form}
    return render(request, "portfolio/contact.html", context)
