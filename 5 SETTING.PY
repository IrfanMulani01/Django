"""
========================================
DJANGO settings.py FILE – COMPLETE GUIDE
========================================

Short Definition:
-----------------
• settings.py is the MAIN configuration file of a Django project
• It controls how the project works
• It contains all important settings like database, apps, templates, static files, etc.
• Without settings.py, Django project cannot run
"""

# --------------------------------------------------
# WHERE IS settings.py LOCATED?
# --------------------------------------------------
"""
Project Folder → inner project package → settings.py

Example:
myproject/
    myproject/
        settings.py
"""

# --------------------------------------------------
# IMPORTANT SECTIONS INSIDE settings.py
# --------------------------------------------------

# 1) SECRET_KEY
"""
• A unique key generated automatically
• Used for security and encryption
• Keep it secret always
• Do NOT share it publicly

Example:
SECRET_KEY = 'djfh34h8743hf8734hf783...'
"""

# 2) DEBUG
"""
• Controls error visibility

DEBUG = True
    → Shows detailed error messages (Development time)

DEBUG = False
    → Hides detailed errors (Production/Live website)

Note:
Keep DEBUG = False on live server for security
"""

# 3) ALLOWED_HOSTS
"""
• Specifies which domains can access project

Example:
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

On live server:
ALLOWED_HOSTS = ['mywebsite.com']
"""

# 4) INSTALLED_APPS
"""
• List of apps included in project
• Contains both built-in apps and user-created apps

Example default apps:
'django.contrib.admin'
'django.contrib.auth'
'django.contrib.sessions'
'django.contrib.messages'
'django.contrib.staticfiles'

When you create app:
add → 'myapp'
"""

# 5) MIDDLEWARE
"""
• Middleware sits between request and response
• Used for:
✔ security
✔ authentication
✔ session handling
✔ message handling

Example middleware:
'django.middleware.security.SecurityMiddleware'
'django.contrib.sessions.middleware.SessionMiddleware'
'django.middleware.common.CommonMiddleware'
"""

# 6) ROOT_URLCONF
"""
• Tells Django which urls.py file to use

Example:
ROOT_URLCONF = 'myproject.urls'
"""

# 7) TEMPLATES
"""
• Settings for HTML template rendering
• Tells Django where to find template files

Important parts:
DIRS → template folder paths
APP_DIRS → enable app template loading

Example:
'DIRS': ['templates']
"""

# 8) DATABASES
"""
• Stores database configuration

Default → SQLite database:

DATABASES = {
 'default': {
   'ENGINE':'django.db.backends.sqlite3',
   'NAME': BASE_DIR / 'db.sqlite3',
 }
}

You can change to:
✔ MySQL
✔ PostgreSQL
✔ Oracle
"""

# 9) AUTH_PASSWORD_VALIDATORS
"""
• Used for password strength checking
• Ensures strong passwords
• Mainly used in admin and auth system
"""

# 10) LANGUAGE_CODE
"""
• Sets default project language

Example:
LANGUAGE_CODE = 'en-us'
"""

# 11) TIME_ZONE
"""
• Sets project time zone

Example:
TIME_ZONE = 'Asia/Kolkata'
"""

# 12) STATIC_URL and STATICFILES_DIRS
"""
• Used for CSS, JS, images, etc.

STATIC_URL = '/static/'

STATICFILES_DIRS = ['static']

Static files example:
✔ style.css
✔ script.js
✔ images
"""

# 13) MEDIA_URL and MEDIA_ROOT
"""
• Used for uploading files (images, documents)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
"""

# 14) DEFAULT_AUTO_FIELD
"""
• Default primary key field type

Example:
BigAutoField used for id column
"""

# --------------------------------------------------
# SIMPLE UNDERSTANDING OF FLOW
# --------------------------------------------------
"""
settings.py controls:
✔ project behavior
✔ apps
✔ database
✔ security
✔ templates
✔ static files
✔ language & timezone
"""

# --------------------------------------------------
# DO NOT DO THIS
# --------------------------------------------------
"""
✖ Do not delete settings.py
✖ Do not share SECRET_KEY
✖ Do not keep DEBUG=True on live server
"""

# --------------------------------------------------
# SIMPLE SUMMARY
# --------------------------------------------------
"""
settings.py includes:

1) SECRET_KEY → project security
2) DEBUG → development/production mode
3) ALLOWED_HOSTS → allowed domains
4) INSTALLED_APPS → list of apps
5) MIDDLEWARE → request/response processing
6) DATABASES → database configuration
7) TEMPLATES → HTML template settings
8) STATIC & MEDIA → file handling
9) LANGUAGE & TIMEZONE → localization

It is the BRAIN of the Django project
"""

# --------------------------------------------------
# PRACTICE TASK FOR YOU
# --------------------------------------------------
"""
1. Open settings.py of your project
2. Identify all sections mentioned above
3. Write one-line meaning in notebook
4. Try changing TIME_ZONE to Asia/Kolkata
"""
3