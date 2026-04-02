from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import SiteProfile, Skill, Project, Education, ContactMessage
from .forms import ContactForm


# ── Helpers ────────────────────────────────────────────────────
def get_profile():
    profile = SiteProfile.objects.first()
    if profile:
        return profile
    # Fallback if DB not seeded yet
    class Default:
        name          = "Dionesio Mahusay"
        tagline       = "IT Student · Web Developer · Hardware Technician"
        short_bio     = "Hi! I'm a 3rd year BSIT student based in the Philippines, passionate about building systems that solve real-world problems."
        about         = "I am a 3rd year college student taking Bachelor of Science in Information Technology."
        career_goals  = "My goal is to become a well-rounded IT professional."
        email         = "dionesiomahusay42@gmail.com"
        github        = "https://github.com/dionesiomahusay42-beep"
        linkedin      = ""
        twitter       = ""
        profile_photo = None
    return Default()


def owner_dict(profile):
    photo = None
    if hasattr(profile, 'profile_photo') and profile.profile_photo:
        try:
            photo = profile.profile_photo.url
        except Exception:
            photo = None
    return {
        "name":          profile.name,
        "tagline":       profile.tagline,
        "short_bio":     profile.short_bio,
        "about":         profile.about,
        "career_goals":  profile.career_goals,
        "email":         profile.email,
        "github":        profile.github,
        "linkedin":      getattr(profile, 'linkedin', ''),
        "twitter":       getattr(profile, 'twitter', ''),
        "profile_photo": photo,
    }


def fallback_skills():
    return {
        'backend':  [("Python",80),("Django",75),("Java",85),("REST APIs",70)],
        'frontend': [("HTML & CSS",80),("JavaScript",70),("Bootstrap",75)],
        'database': [("MySQL",85),("Database Design",80)],
        'tools':    [("Git & GitHub",75),("PythonAnywhere",70),("NetBeans",80)],
        'hardware': [("Hardware Installation",90),("PC Assembly & Repair",90),("Network Setup",80),("OS Installation",85)],
    }


def fallback_projects():
    from types import SimpleNamespace
    return [
        SimpleNamespace(emoji="🏨", title="Hotel Management System",
            description="A comprehensive hotel management system that handles room reservations, guest check-in and check-out, billing, and room availability tracking.",
            get_tech_list=lambda: ["Java","MySQL","NetBeans","JDBC"], github_url="", live_url=""),
        SimpleNamespace(emoji="📦", title="Inventory System",
            description="A Java-based inventory management system that tracks stock levels, manages product records, and generates low-stock reports.",
            get_tech_list=lambda: ["Java","MySQL","NetBeans","JDBC"], github_url="", live_url=""),
        SimpleNamespace(emoji="🅿️", title="Santa Catalina Parking & Ticketing System",
            description="A parking and ticketing system for Santa Catalina that manages vehicle entry/exit and computes parking fees.",
            get_tech_list=lambda: ["Java","MySQL","NetBeans","JDBC"], github_url="", live_url=""),
        SimpleNamespace(emoji="🌐", title="Personal Portfolio Website",
            description="A responsive personal portfolio website built with Python and Django, deployed on PythonAnywhere.",
            get_tech_list=lambda: ["Python","Django","HTML/CSS","Bootstrap","SQLite"],
            github_url="https://github.com/dionesiomahusay42-beep/portfolio",
            live_url="https://dionesiomahusay.pythonanywhere.com"),
    ]


def fallback_education():
    from types import SimpleNamespace
    return [
        SimpleNamespace(school="NEGROS ORIENTAL STATE UNIVERSITY",
            degree="Bachelor of Science in Information Technology",
            year="2022 – Present",
            description="Currently in 3rd year. Relevant coursework: Data Structures, Web Development, Database Management Systems, Object-Oriented Programming, Computer Hardware Servicing."),
        SimpleNamespace(school="NEGROS OCCIDENTAL HIGH SCHOOL",
            degree="Senior High School", year="2020 – 2022",
            description="Completed Senior High School education."),
    ]


# ── Views ───────────────────────────────────────────────────────
def home(request):
    profile  = get_profile()
    db_skills = list(Skill.objects.all()[:6])
    skills   = [(s.name, s.proficiency, s.category) for s in db_skills] if db_skills else \
               [(n,p,c) for cat in fallback_skills().values() for n,p in cat for c in ['']][:6]

    if not db_skills:
        fb = fallback_skills()
        skills = [(n,p,'backend') for n,p in fb['backend']][:6]

    db_projects = list(Project.objects.filter(featured=True).order_by('order')[:3])
    projects = db_projects if db_projects else fallback_projects()[:3]

    return render(request, "portfolio/home.html", {
        "owner": owner_dict(profile), "skills": skills, "projects": projects
    })


def about(request):
    return render(request, "portfolio/about.html", {"owner": owner_dict(get_profile())})


def skills(request):
    all_skills = Skill.objects.all()
    if all_skills.exists():
        fb = {
            'backend':  [(s.name, s.proficiency) for s in all_skills if s.category == 'backend'],
            'frontend': [(s.name, s.proficiency) for s in all_skills if s.category == 'frontend'],
            'database': [(s.name, s.proficiency) for s in all_skills if s.category == 'database'],
            'tools':    [(s.name, s.proficiency) for s in all_skills if s.category == 'tools'],
            'hardware': [(s.name, s.proficiency) for s in all_skills if s.category == 'hardware'],
        }
    else:
        fb = fallback_skills()

    return render(request, "portfolio/skills.html", {
        "owner": owner_dict(get_profile()), **fb
    })


def projects(request):
    db = list(Project.objects.all().order_by('order'))
    return render(request, "portfolio/projects.html", {
        "owner": owner_dict(get_profile()),
        "projects": db if db else fallback_projects()
    })


def education(request):
    db = list(Education.objects.all().order_by('order'))
    return render(request, "portfolio/education.html", {
        "owner": owner_dict(get_profile()),
        "education": db if db else fallback_education()
    })


def contact(request):
    profile = get_profile()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Save to database
            ContactMessage.objects.create(**data)

            # Send email notification to you
            try:
                send_mail(
                    subject=f"[Portfolio] New message from {data['name']}: {data['subject']}",
                    message=(
                        f"You received a new message from your portfolio contact form.\n\n"
                        f"Name:    {data['name']}\n"
                        f"Email:   {data['email']}\n"
                        f"Subject: {data['subject']}\n\n"
                        f"Message:\n{data['message']}\n\n"
                        f"---\nReply directly to: {data['email']}"
                    ),
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                # Send confirmation email to sender
                send_mail(
                    subject="Thanks for reaching out! — Dionesio Mahusay",
                    message=(
                        f"Hi {data['name']},\n\n"
                        f"Thank you for your message! I have received it and will get back to you soon.\n\n"
                        f"Here's a copy of what you sent:\n"
                        f"Subject: {data['subject']}\n"
                        f"Message: {data['message']}\n\n"
                        f"Best regards,\nDionesio Mahusay\n"
                        f"dionesiomahusay42@gmail.com"
                    ),
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[data['email']],
                    fail_silently=True,
                )
                messages.success(request, "✅ Message sent! I'll get back to you soon.")
            except Exception:
                # Email failed but message still saved in DB
                messages.success(request, "✅ Message received! I'll get back to you soon.")

            return redirect("contact")
        else:
            messages.error(request, "❌ Please fix the errors below.")
    else:
        form = ContactForm()

    return render(request, "portfolio/contact.html", {
        "owner": owner_dict(profile), "form": form
    })