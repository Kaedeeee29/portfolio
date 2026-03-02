"""
Management command to populate the database with initial sample data.
Run with: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from portfolio.models import Skill, Project, SocialLink
from blog.models import Category, Tag, Post


class Command(BaseCommand):
    help = 'Seed the database with initial portfolio data'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding database...\n')
        self._seed_skills()
        self._seed_projects()
        self._seed_social_links()
        self._seed_blog()
        self.stdout.write(self.style.SUCCESS('\n✅ Database seeded successfully!\n'))

    def _seed_skills(self):
        skills_data = [
            # Languages
            ('Python', 'languages', 92, 'devicon-python-plain colored', 1),
            ('Java', 'languages', 78, 'devicon-java-plain colored', 2),
            ('C++', 'languages', 75, 'devicon-cplusplus-plain colored', 3),
            ('JavaScript', 'languages', 85, 'devicon-javascript-plain colored', 4),
            # Frameworks
            ('Django', 'frameworks', 90, 'devicon-django-plain', 1),
            ('React.js', 'frameworks', 80, 'devicon-react-original colored', 2),
            ('Vue.js', 'frameworks', 75, 'devicon-vuejs-plain colored', 3),
            ('Node.js', 'frameworks', 72, 'devicon-nodejs-plain colored', 4),
            # Frontend
            ('HTML5', 'frontend', 95, 'devicon-html5-plain colored', 1),
            ('CSS3', 'frontend', 90, 'devicon-css3-plain colored', 2),
            ('Vite', 'frontend', 70, 'devicon-vitejs-plain colored', 3),
            # Backend
            ('REST API Development', 'backend', 88, '', 1),
            ('Authentication Systems', 'backend', 85, '', 2),
            ('PostgreSQL', 'backend', 80, 'devicon-postgresql-plain colored', 3),
            ('Database Design', 'backend', 83, '', 4),
            # Tools
            ('Git & GitHub', 'tools', 90, 'devicon-github-original', 1),
            ('Linux', 'tools', 75, 'devicon-linux-plain', 2),
            ('Docker', 'tools', 65, 'devicon-docker-plain colored', 3),
        ]
        created = 0
        for name, category, proficiency, icon, order in skills_data:
            _, c = Skill.objects.get_or_create(
                name=name,
                defaults={'category': category, 'proficiency': proficiency, 'icon': icon, 'order': order}
            )
            if c: created += 1
        self.stdout.write(f'  ✓ Skills: {created} created')

    def _seed_projects(self):
        projects_data = [
            {
                'title': 'ApolloHome',
                'short_description': 'A full-featured web-based management system with role-based access control, real-time dashboards, and comprehensive admin tools.',
                'description': 'ApolloHome is a Django-powered web management system featuring authentication, role-based access control, and a clean admin interface.',
                'technologies': 'Django, Python, PostgreSQL, Bootstrap, JavaScript',
                'github_url': 'https://github.com/yourusername/apollohome',
                'demo_url': '',
                'featured': True,
                'order': 1,
            },
            {
                'title': 'Student Portal System',
                'short_description': 'Academic management platform integrating multiple services — built as a demonstration of system integration concepts from IAS 1.',
                'description': 'Academic management system with Django REST backend and React frontend.',
                'technologies': 'Django REST Framework, React, JWT Auth, PostgreSQL',
                'github_url': 'https://github.com/yourusername/student-portal',
                'demo_url': '',
                'featured': False,
                'order': 2,
            },
            {
                'title': 'Web Dev 2 Showcase',
                'short_description': 'A collection of advanced web applications built with Vue.js and Node.js, showcasing modern frontend and backend development patterns.',
                'description': 'Vue.js and Node.js projects showcase.',
                'technologies': 'Vue.js, Node.js, Vite, MongoDB, Express',
                'github_url': 'https://github.com/yourusername/webdev2-showcase',
                'demo_url': '',
                'featured': False,
                'order': 3,
            },
            {
                'title': 'Inventory Management System',
                'short_description': 'Web-based inventory system with real-time reporting, barcode support, and multi-user access designed for small to medium businesses.',
                'description': 'Django inventory system with reporting.',
                'technologies': 'Python, Django, SQLite, Chart.js, Bootstrap',
                'github_url': 'https://github.com/yourusername/inventory-system',
                'demo_url': '',
                'featured': False,
                'order': 4,
            },
            {
                'title': 'CS Learning Platform',
                'short_description': 'E-learning platform tailored for Computer Programming courses with interactive exercises, quizzes, and student progress tracking.',
                'description': 'Learning management system for CS courses.',
                'technologies': 'React, Django REST Framework, PostgreSQL, Redis',
                'github_url': 'https://github.com/yourusername/cs-learning-platform',
                'demo_url': '',
                'featured': True,
                'order': 5,
            },
        ]
        created = 0
        for data in projects_data:
            _, c = Project.objects.get_or_create(title=data['title'], defaults=data)
            if c: created += 1
        self.stdout.write(f'  ✓ Projects: {created} created')

    def _seed_social_links(self):
        links = [
            ('GitHub', 'https://github.com/yourusername', 'fab fa-github', 1),
            ('LinkedIn', 'https://linkedin.com/in/yourusername', 'fab fa-linkedin', 2),
            ('Email', 'mailto:your@email.com', 'fas fa-envelope', 3),
        ]
        created = 0
        for name, url, icon, order in links:
            _, c = SocialLink.objects.get_or_create(
                name=name,
                defaults={'url': url, 'icon_class': icon, 'order': order}
            )
            if c: created += 1
        self.stdout.write(f'  ✓ Social links: {created} created')

    def _seed_blog(self):
        # Categories
        categories = ['Django & Python', 'Web Development', 'Teaching & Education', 'System Architecture']
        cat_objs = {}
        for name in categories:
            cat, _ = Category.objects.get_or_create(name=name)
            cat_objs[name] = cat

        # Tags
        tags = ['Django', 'Python', 'Tutorial', 'REST API', 'React', 'Teaching', 'Architecture']
        tag_objs = {}
        for name in tags:
            tag, _ = Tag.objects.get_or_create(name=name)
            tag_objs[name] = tag

        # Sample post
        if not Post.objects.exists():
            post = Post.objects.create(
                title='Getting Started with Django: A Beginner\'s Guide',
                excerpt='Learn how to set up your first Django project, understand the MVT architecture, and build your first web application from scratch.',
                content='''
<h2>Introduction</h2>
<p>Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.</p>

<h2>Setting Up Your Environment</h2>
<p>First, make sure you have Python installed. Then create a virtual environment:</p>
<pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install django</code></pre>

<h2>Creating Your First Project</h2>
<p>Run the following command to create a new Django project:</p>
<pre><code>django-admin startproject myproject
cd myproject
python manage.py runserver</code></pre>

<p>Visit <code>http://127.0.0.1:8000</code> in your browser and you should see the Django welcome page!</p>

<h2>Understanding MVT Architecture</h2>
<p>Django follows the MVT (Model-View-Template) pattern:</p>
<ul>
<li><strong>Model</strong> - Defines your data structure (database tables)</li>
<li><strong>View</strong> - Business logic and data processing</li>
<li><strong>Template</strong> - HTML presentation layer</li>
</ul>

<p>This separation of concerns makes your code organized and maintainable — something I emphasize heavily in my Computer Programming classes.</p>

<h2>Conclusion</h2>
<p>Django is an excellent framework for both beginners and seasoned developers. Its "batteries included" philosophy means you get authentication, admin panel, ORM, and more out of the box.</p>
''',
                category=cat_objs['Django & Python'],
                published=True,
            )
            post.tags.set([tag_objs['Django'], tag_objs['Python'], tag_objs['Tutorial']])
            self.stdout.write(f'  ✓ Blog: 1 sample post created')
        else:
            self.stdout.write(f'  ✓ Blog: already has posts, skipping')
