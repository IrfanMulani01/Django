"""
========================================
MANAGE.PY IN DJANGO – COMPLETE NOTES
========================================

Short Definition:
-----------------
• manage.py is the command-line tool of a Django project
• It allows you to run important Django commands
• It helps to start server, create apps, manage database, etc.
• It is created automatically when a Django project is created

Location:
---------
• manage.py is present in the outer main project folder

Example:
myproject/
    manage.py
    myproject/
        settings.py

Simple Meaning:
---------------
• manage.py is like the remote control of the Django project
• Using it, we talk to Django through commands
• Without it, project cannot be controlled

Main Uses of manage.py:
-----------------------
• Run development server
• Create Django apps
• Handle database migrations
• Create admin user
• Open Django shell
• View available commands

Important Commands Using manage.py:
-----------------------------------
1) Run Django development server
   python manage.py runserver

2) Create new Django app
   python manage.py startapp myapp

3) Make database migrations
   python manage.py makemigrations

4) Apply migrations to database
   python manage.py migrate

5) Create admin/superuser
   python manage.py createsuperuser

6) Open Django shell
   python manage.py shell

7) See all available commands
   python manage.py help

How manage.py Works Internally (Simple):
----------------------------------------
• It loads Django project settings
• Connects project with Python environment
• Executes the command entered in terminal

Simple Flow:
Command → manage.py → Django → Output

Why manage.py is Important:
---------------------------
• Without manage.py:
  ✖ cannot run Django server
  ✖ cannot create apps
  ✖ cannot use admin panel
  ✖ cannot handle migrations

So it is a very important file.

Do We Edit manage.py?
---------------------
• Beginners: No need to edit
• It already has required code
• Advanced developers may customize it later

Real-Life Example:
------------------
• manage.py is like the steering wheel of a car
• Car exists, but without steering it cannot be controlled

Simple Summary:
---------------
• manage.py is the controller of Django project
• It runs commands
• It loads project environment
• It is required for almost every Django operation

Practice Task:
--------------
1) Open your Django project folder
2) Locate manage.py file
3) Run this command in terminal:
   python manage.py runserver
4) Observe what happens
5) Write any 5 manage.py commands in notebook
"""
