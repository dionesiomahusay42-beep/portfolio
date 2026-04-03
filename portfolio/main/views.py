from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm


# ─── Portfolio Data ────────────────────────────────────────────────────────────
# Edit all values below to personalize your portfolio

OWNER = {
    "name": "Dionesio Mahusay",
    "tagline": "IT Student · Web Developer · Hardware Technician",
    "short_bio": "Hi! I'm a 3rd year BSIT student based in the Philippines, "
                 "passionate about building systems that solve real world problems.",
    "about": (
        "I am a 3rd year college student taking Bachelor of Science in Information "
        "Technology. I have a strong interest in both software development and hardware "
        "systems. I enjoy building practical applications using Java, Python, and Django, "
        "and I also have hands-on experience in hardware installation, troubleshooting, "
        "and repair. I am always eager to learn new technologies and apply them to "
        "create solutions that make a difference."
    ),
    "career_goals": (
        "My goal is to become a well-rounded IT professional who can handle both "
        "software development and hardware systems. I aspire to work on enterprise-level "
        "applications, contribute to meaningful projects, and eventually lead a team of "
        "developers. I am especially interested in system development, database management, "
        "and network infrastructure."
    ),
    "email": "dionesiomahusay42@gmail.com",
    "github": "https://github.com/dionesiomahusay42-beep",
    "linkedin": "",
    "twitter": "",
    # To add your photo:
    # 1. Upload your photo to any image hosting site (e.g. imgur.com)
    # 2. Copy the direct image URL and paste it below
    # Example: "profile_photo": "https://i.imgur.com/yourphoto.jpg",
"profile_photo": "images/profile.png",
}

SKILLS = [
    # (skill_name, proficiency_percent, category)
    # Backend
    ("Python",                      80, "backend"),
    ("Django",                      75, "backend"),
    ("Java",                        85, "backend"),
    ("REST APIs",                   70, "backend"),
    # Frontend
    ("HTML & CSS",                  80, "frontend"),
    ("JavaScript",                  70, "frontend"),
    ("Bootstrap",                   75, "frontend"),
    # Database
    ("MySQL",                       85, "database"),
    ("Database Design",             80, "database"),
    # Tools
    ("Git & GitHub",                75, "tools"),
    ("PythonAnywhere",              70, "tools"),
    ("NetBeans / Eclipse",          80, "tools"),
    # Hardware
    ("Hardware Installation",       90, "hardware"),
    ("Hardware Troubleshooting",    90, "hardware"),
    ("PC Assembly & Repair",        90, "hardware"),
    ("Network Setup",               80, "hardware"),
    ("OS Installation",             85, "hardware"),
]

PROJECTS = [
    {
        "title": "Hotel Management System",
        "description": (
            "A comprehensive hotel management system that handles room reservations, "
            "guest check-in and check-out, billing, and room availability tracking. "
            "Designed to streamline hotel operations and improve guest experience."
        ),
        "tech": ["Java", "MySQL", "NetBeans", "JDBC"],
        "github": "",
        "live": None,
        "emoji": "🏨",
    },
    {
        "title": "Inventory System",
        "description": (
            "A Java-based inventory management system that tracks stock levels, "
            "manages product records, generates reports, and sends alerts for "
            "low-stock items. Built to help businesses manage their inventory efficiently."
        ),
        "tech": ["Java", "MySQL", "NetBeans", "JDBC"],
        "github": "",
        "live": None,
        "emoji": "📦",
    },
    {
        "title": "Santa Catalina Parking & Ticketing System",
        "description": (
            "A parking and ticketing system developed for Santa Catalina that manages "
            "vehicle entry and exit, generates parking tickets, computes fees based on "
            "duration, and maintains a log of all parking transactions."
        ),
        "tech": ["Java", "MySQL", "NetBeans", "JDBC"],
        "github": "",
        "live": None,
        "emoji": "🅿️",
    },
    {
        "title": "Personal Portfolio Website",
        "description": (
            "A responsive personal portfolio website built with Python and Django, "
            "deployed on PythonAnywhere. Features sections for skills, projects, "
            "education, and a working contact form."
        ),
        "tech": ["Python", "Django", "HTML/CSS", "Bootstrap", "SQLite"],
        "github": "https://github.com/dionesiomahusay42-beep/portfolio",
        "live": "https://dionesiomahusay.pythonanywhere.com",
        "emoji": "🌐",
    },
]

EDUCATION = [
    {
        "school": "NEGROS ORIENTAL STATES UNIVERSITY",  # ← Replace with your school name
        "degree": "Bachelor of Science in Information Technology",
        "year": "2026 – Present",
        "description": (
            "Currently in 3rd year. Relevant coursework includes: Data Structures, "
            "Web Development, Database Management Systems, Object-Oriented Programming, "
            "Computer Hardware Servicing, and Systems Analysis and Design."
        ),
    },
    {
        "school": "NEGROS OCCIDENTAL HIGHSCHOOL",   # ← Replace with your SHS name
        "degree": "Senior High School",
        "year": "2020 – 2022",
        "description": "Completed Senior High School education.",
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
    hardware = [(s, p) for s, p, c in SKILLS if c == "hardware"]
    context  = {
        "owner": OWNER,
        "backend": backend, "frontend": frontend,
        "database": database, "tools": tools,
        "hardware": hardware,
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