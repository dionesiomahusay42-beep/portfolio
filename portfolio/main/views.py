from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SiteProfile, Skill, Project, Education, ContactMessage
from .forms import ContactForm

# ── Fallback data (used if database is empty) ──────────────────
OWNER_DEFAULT = {
    "name": "Dionesio Mahusay",
    "tagline": "IT Student · Web Developer · Hardware Technician",
    "short_bio": "Hi! I'm a 3rd year BSIT student based in the Philippines, passionate about building systems that solve real world problems.",
    "about": "I am a 3rd year college student taking Bachelor of Science in Information Technology. I have a strong interest in both software development and hardware systems. I enjoy building practical applications using Java, Python, and Django, and I also have hands-on experience in hardware installation, troubleshooting, and repair. I am always eager to learn new technologies and apply them to create solutions that make a difference.",
    "career_goals": "My goal is to become a well-rounded IT professional who can handle both software development and hardware systems. I aspire to work on enterprise-level applications, contribute to meaningful projects, and eventually lead a team of developers. I am especially interested in system development, database management, and network infrastructure.",
    "email": "dionesiomahusay42@gmail.com",
    "github": "https://github.com/dionesiomahusay42-beep",
    "linkedin": "",
    "twitter": "",
    "profile_photo": "images/profile.png",
}

SKILLS_DEFAULT = [
    ("Python", 80, "backend"), ("Django", 75, "backend"), ("Java", 85, "backend"), ("REST APIs", 70, "backend"),
    ("HTML & CSS", 80, "frontend"), ("JavaScript", 70, "frontend"), ("Bootstrap", 75, "frontend"),
    ("MySQL", 85, "database"), ("Database Design", 80, "database"),
    ("Git & GitHub", 75, "tools"), ("PythonAnywhere", 70, "tools"), ("NetBeans / Eclipse", 80, "tools"),
    ("Hardware Installation", 90, "hardware"), ("Hardware Troubleshooting", 90, "hardware"),
    ("PC Assembly & Repair", 90, "hardware"), ("Network Setup", 80, "hardware"), ("OS Installation", 85, "hardware"),
]

PROJECTS_DEFAULT = [
    {"title": "Hotel Management System", "description": "A comprehensive hotel management system that handles room reservations, guest check-in and check-out, billing, and room availability tracking.", "tech": ["Java", "MySQL", "NetBeans", "JDBC"], "github": "", "live": None, "emoji": "🏨"},
    {"title": "Inventory System", "description": "A Java-based inventory management system that tracks stock levels, manages product records, generates reports, and sends alerts for low-stock items.", "tech": ["Java", "MySQL", "NetBeans", "JDBC"], "github": "", "live": None, "emoji": "📦"},
    {"title": "Santa Catalina Parking & Ticketing System", "description": "A parking and ticketing system developed for Santa Catalina that manages vehicle entry and exit, generates parking tickets, and computes fees based on duration.", "tech": ["Java", "MySQL", "NetBeans", "JDBC"], "github": "", "live": None, "emoji": "🅿️"},
    {"title": "Personal Portfolio Website", "description": "A responsive personal portfolio website built with Python and Django, deployed on PythonAnywhere.", "tech": ["Python", "Django", "HTML/CSS", "Bootstrap", "SQLite"], "github": "https://github.com/dionesiomahusay42-beep/portfolio", "live": "https://dionesiomahusay.pythonanywhere.com", "emoji": "🌐"},
]

EDUCATION_DEFAULT = [
    {"school": "NEGROS ORIENTAL STATE UNIVERSITY", "degree": "Bachelor of Science in Information Technology", "year": "2022 - Present", "description": "Currently in 3rd year. Relevant coursework: Data Structures, Web Development, Database Management, OOP, Hardware Servicing."},
    {"school": "NEGROS OCCIDENTAL HIGH SCHOOL", "degree": "Senior High School", "year": "2020 - 2022", "description": "Completed Senior High School education."},
]


def get_owner():
    p = SiteProfile.objects.first()
    if not p:
        return OWNER_DEFAULT
    return {
        "name": p.name, "tagline": p.tagline, "short_bio": p.short_bio,
        "about": p.about, "career_goals": p.career_goals,
        "email": p.email, "github": p.github, "linkedin": p.linkedin,
        "twitter": p.twitter, "profile_photo": "images/profile.png",
    }


def get_skills():
    qs = Skill.objects.all()
    if qs.exists():
        return [(s.name, s.proficiency, s.category) for s in qs]
    return SKILLS_DEFAULT


def get_projects():
    qs = list(Project.objects.all().order_by('order'))
    if qs:
        result = []
        for p in qs:
            result.append({
                "title": p.title, "description": p.description,
                "tech": p.get_tech_list(), "github": p.github_url,
                "live": p.live_url or None, "emoji": p.emoji,
            })
        return result
    return PROJECTS_DEFAULT


def get_education():
    qs = list(Education.objects.all().order_by('order'))
    if qs:
        return [{"school": e.school, "degree": e.degree, "year": e.year, "description": e.description} for e in qs]
    return EDUCATION_DEFAULT


def home(request):
    skills = get_skills()[:6]
    return render(request, "portfolio/home.html", {
        "owner": get_owner(), "skills": skills, "projects": get_projects()[:3]
    })

def about(request):
    return render(request, "portfolio/about.html", {"owner": get_owner()})

def skills(request):
    all_skills = get_skills()
    return render(request, "portfolio/skills.html", {
        "owner": get_owner(),
        "backend":  [(s, p) for s, p, c in all_skills if c == "backend"],
        "frontend": [(s, p) for s, p, c in all_skills if c == "frontend"],
        "database": [(s, p) for s, p, c in all_skills if c == "database"],
        "tools":    [(s, p) for s, p, c in all_skills if c == "tools"],
        "hardware": [(s, p) for s, p, c in all_skills if c == "hardware"],
    })

def projects(request):
    return render(request, "portfolio/projects.html", {"owner": get_owner(), "projects": get_projects()})

def education(request):
    return render(request, "portfolio/education.html", {"owner": get_owner(), "education": get_education()})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            messages.success(request, "✅ Your message has been sent!")
            return redirect("contact")
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, "portfolio/contact.html", {"owner": get_owner(), "form": form})