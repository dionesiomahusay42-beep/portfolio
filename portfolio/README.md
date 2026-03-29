# 🌐 Django Portfolio Website

A personal portfolio website built with **Python + Django**, deployed on **PythonAnywhere**.

**Live URL:** `https://firstname_lastname.pythonanywhere.com`
*(Replace `firstname_lastname` with your actual PythonAnywhere username)*

---

## 📋 Sections

| Section | URL |
|---------|-----|
| Home | `/` |
| About | `/about/` |
| Skills | `/skills/` |
| Projects | `/projects/` |
| Education | `/education/` |
| Contact | `/contact/` |
| Admin | `/admin/` |

---

## 🚀 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

### 2. Create & activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create superuser (for admin panel)
```bash
python manage.py createsuperuser
```

### 6. Collect static files
```bash
python manage.py collectstatic
```

### 7. Run development server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## ✏️ Personalizing Your Portfolio

Open `main/views.py` and edit the `OWNER`, `SKILLS`, `PROJECTS`, and `EDUCATION` dictionaries at the top of the file. No database changes needed — everything is configured in one place.

```python
OWNER = {
    "name": "Your Full Name",
    "tagline": "Your Tagline Here",
    ...
}
```

---

## ☁️ Deploying to PythonAnywhere

### Step 1 — Sign up
Create a free account at [pythonanywhere.com](https://www.pythonanywhere.com) using the username format `firstname_lastname`.

### Step 2 — Open a Bash console
In your PythonAnywhere dashboard, open **Consoles → Bash**.

### Step 3 — Clone your repo
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

### Step 4 — Create a virtual environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 venv
pip install -r requirements.txt
```

### Step 5 — Update settings
In `portfolio/settings.py`, update `ALLOWED_HOSTS`:
```python
ALLOWED_HOSTS = ['firstname_lastname.pythonanywhere.com']
```

### Step 6 — Run migrations & collect static
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

### Step 7 — Configure Web App
1. Go to **Web** tab → **Add a new web app**
2. Choose **Manual configuration** → **Python 3.10**
3. Set **Source code**: `/home/firstname_lastname/portfolio`
4. Set **Working directory**: `/home/firstname_lastname/portfolio`
5. Set **Virtualenv**: `/home/firstname_lastname/.virtualenvs/venv`

### Step 8 — WSGI file
Click on the WSGI config file link and replace its contents with:
```python
import os
import sys

path = '/home/firstname_lastname/portfolio'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 9 — Static files
In the **Web** tab, under **Static files**:
| URL | Directory |
|-----|-----------|
| `/static/` | `/home/firstname_lastname/portfolio/staticfiles` |

### Step 10 — Reload
Click the green **Reload** button. Your site is live! 🎉

---

## 📁 Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3              # Created after migrations
├── portfolio/              # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                   # Main application
│   ├── models.py
│   ├── views.py            # ← Edit portfolio data here
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── templates/
│   └── portfolio/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       ├── skills.html
│       ├── projects.html
│       ├── education.html
│       └── contact.html
└── static/
    ├── css/style.css
    └── js/main.js
```

---

## 👨‍💻 Tech Stack

- **Backend:** Python 3.10, Django 4.2
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Database:** SQLite
- **Hosting:** PythonAnywhere
- **Version Control:** Git / GitHub

---

## 📄 License

MIT License — free to use and modify.
