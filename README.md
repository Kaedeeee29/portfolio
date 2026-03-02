# 🚀 Personal Portfolio Website — Django

A modern, responsive Personal Portfolio Website with Admin Blog System built with **Django 4.2**.

> Built for: Computer Technician · Programming Instructor (CS I & II, IAS 1, Web Dev 2) · Full-Stack Developer

---

## ✨ Features

- **Hero Section** — animated intro with role badges and code card
- **About Me** — professional background, education, teaching roles
- **Skills** — organized by category with animated progress bars
- **Projects** — filterable project cards with GitHub & demo links
- **Blog** — full CMS via Django Admin (categories, tags, rich text)
- **Contact** — form with message stored to DB + optional email notification
- **Django Admin** — manage all content from `/admin/`
- **Responsive** — mobile-first design
- **Dark Theme** — professional dark color palette
- **Deployable** — Render, Railway, PythonAnywhere ready

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2, Python 3.11 |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Rich Text | django-ckeditor |
| Static Files | WhiteNoise |
| Frontend | Bootstrap 5, Font Awesome 6, Devicons |
| Fonts | Inter, Fira Code (Google Fonts) |
| Deployment | Gunicorn + Render/Railway |

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env and set your SECRET_KEY
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Seed Sample Data (Optional)
```bash
python manage.py seed_data
```

### 8. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 9. Run Development Server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** 🎉

---

## 🔧 Customization Guide

### Update Personal Info
Edit the following templates with your real information:
- `templates/base.html` — name, nav brand
- `portfolio/templates/portfolio/home.html` — hero name, about text, roles
- `contact/templates/contact/contact.html` — email, GitHub, LinkedIn URLs

### Add Content via Django Admin
1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Add **Skills**, **Projects**, **Social Links**, **Blog Posts**

### Add Your Photo
In `portfolio/templates/portfolio/home.html`, replace the `.about-image-placeholder` with:
```html
<img src="{% static 'images/your-photo.jpg' %}" alt="Your Name" class="about-actual-image">
```
Place your photo in `static/images/`.

---

## 📁 Project Structure

```
portfolio/
├── config/                  # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/               # Main portfolio app
│   ├── models.py            # Skill, Project, SocialLink
│   ├── views.py
│   ├── admin.py
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py
│   └── templates/portfolio/
│       └── home.html
├── blog/                    # Blog app
│   ├── models.py            # Post, Category, Tag
│   ├── views.py
│   ├── admin.py
│   └── templates/blog/
│       ├── post_list.html
│       └── post_detail.html
├── contact/                 # Contact app
│   ├── models.py            # ContactMessage
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   └── templates/contact/
│       └── contact.html
├── static/
│   ├── css/style.css
│   └── js/main.js
├── templates/
│   └── base.html
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
└── .env.example
```

---

## 🌐 Deployment

### Render
1. Push code to GitHub
2. Create new Web Service on Render
3. Set environment variables from `.env.example`
4. Build command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
5. Start command: `gunicorn config.wsgi:application`

### PythonAnywhere
1. Upload code via Git
2. Create a virtual environment and install requirements
3. Configure WSGI file to point to `config.wsgi`
4. Set environment variables in the `.env` file

---

## 📄 Django Admin — Content Management

| Model | Path | Purpose |
|-------|------|---------|
| Skills | `/admin/portfolio/skill/` | Add skills with categories & proficiency |
| Projects | `/admin/portfolio/project/` | Manage portfolio projects |
| Social Links | `/admin/portfolio/sociallink/` | GitHub, LinkedIn, Email links |
| Blog Posts | `/admin/blog/post/` | Write and publish blog posts |
| Categories | `/admin/blog/category/` | Blog categories |
| Tags | `/admin/blog/tag/` | Blog tags |
| Contact Messages | `/admin/contact/contactmessage/` | View submitted contact forms |

---

## 📬 Contact Form

Messages are saved to the database and viewable at `/admin/contact/contactmessage/`.

To enable email notifications, configure email settings in `.env`:
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST_USER=your@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
CONTACT_EMAIL=your@gmail.com
```

---

## 🎓 License

MIT — feel free to use and customize for your own portfolio!

---

*Built with ❤️ using Django — showcasing backend development, authentication, database design, and full-stack skills.*
