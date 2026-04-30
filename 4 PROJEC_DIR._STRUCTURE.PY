"""
========================================
DJANGO PROJECT DIRECTORY STRUCTURE
========================================

Short Definition:
-----------------
• After creating a Django project, some folders and files are auto-generated
• These files together form the Django project structure
• Each file has a specific purpose in project working
"""

# --------------------------------------------------
# HOW PROJECT IS CREATED?
# --------------------------------------------------
"""
Command:

django-admin startproject myproject

After creation → open project folder
You will see structure like this:
"""

# --------------------------------------------------
# DEFAULT PROJECT STRUCTURE
# --------------------------------------------------
"""
myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
"""

# --------------------------------------------------
# FILE AND FOLDER EXPLANATION
# --------------------------------------------------


# 1) manage.py
"""
• Main command-line tool for Django project
• Helps in running server and migrations
• We execute most Django commands using this file

Example commands:
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
"""

# 2) myproject (inner folder)
"""
• Project package folder
• Contains main configuration files of project
• Name is same as project name
"""

# 3) __init__.py
"""
• Makes folder behave like Python package
• Tells Python that this folder contains modules
• File is usually empty
"""

# 4) settings.py
"""
• HEART of Django project
• Stores all project configurations like:

✔ Installed apps
✔ Database settings
✔ Static files settings
✔ Template settings
✔ Middleware
✔ Debug mode
✔ Allowed hosts

Without settings.py project cannot run
"""

# 5) urls.py
"""
• Stores project level URL routing
• Maps URL → View function

Example:
path('home/', views.home)
"""

# 6) asgi.py
"""
• Used for asynchronous deployment
• Supports async applications like chat, notifications
• Used by ASGI servers
"""

# 7) wsgi.py
"""
• Used for deployment on web servers
• Helps Django talk with web server
• Used by WSGI servers like Apache, Nginx + Gunicorn
"""

# --------------------------------------------------
# SIMPLE FLOW UNDERSTANDING
# --------------------------------------------------
"""
Browser request → urls.py → views → templates → response
Settings file controls whole project in background
"""

# --------------------------------------------------
# IMPORTANT NOTE
# --------------------------------------------------
"""
Do NOT delete or rename any default files blindly
Project will stop working
"""

# --------------------------------------------------
# SIMPLE SUMMARY
# --------------------------------------------------
"""
Project contains:

1) manage.py → command tool
2) settings.py → configuration center
3) urls.py → URL mapping file
4) asgi.py / wsgi.py → deployment files
5) __init__.py → package indicator
6) project folder → contains all main files
""" 

# --------------------------------------------------
# PRACTICE TASK FOR YOU
# --------------------------------------------------
"""
1. Create new Django project: demo_project
2. Open folder structure
3. Identify each file
4. Write short meaning in notebook
"""
