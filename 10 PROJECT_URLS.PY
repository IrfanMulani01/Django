"""
========================================
PROJECT-BASED URLs IN DJANGO
========================================

Short Definition:
-----------------
• Project-based URLs are written in urls.py file of the main Django project
• They control which web page opens for which URL
• They work like a road map for the website

File Location:
--------------
Project folder → urls.py

Example:
myproject/
    manage.py
    myproject/
        urls.py
        settings.py

Simple Meaning:
---------------
• urls.py tells Django:
  "If user visits this URL, open this page"

Example Understanding:
----------------------
User enters in browser:
http://127.0.0.1:8000/home

urls.py decides:
--> Which view function should run
--> Which page should be shown

Role of Project URLs:
---------------------
• Connect browser request to views
• Handle website navigation
• Map URLs to apps
• Redirect pages

Default urls.py Content (Simple View):
--------------------------------------
When project is created, urls.py contains:

• import statements
• urlpatterns list

Important Term:
---------------
urlpatterns = list of all URL paths in project

Basic URL Example:
------------------
path('home/', views.home)

Meaning:
--------
• If user enters /home
• run home() function from views

Including App URLs in Project URLs:
-----------------------------------
We do not write all URLs in project file
We connect app URLs like:

path('student/', include('student.urls'))

Meaning:
--------
• All student related URLs are stored in student app
• Project URLs only link them

Important Functions in urls.py:
-------------------------------
1) path() → used to define URL
2) include() → used to include app URLs

Simple Flow of Request:
-----------------------
Browser URL → Project urls.py → App urls.py → View → Template → Output

Why Project URLs are Important:
-------------------------------
• They control whole website routing
• Without URLs, user cannot open pages
• They connect apps inside project

Real-Life Example:
------------------
• Project URLs are like:
  ✔ Main index of book
  ✔ Road map of city
They tell:
“Which road goes where?”

Common Mistakes to Avoid:
-------------------------
✖ Forgetting to import include
✖ Wrong path names
✖ Space or comma missing
✖ Not adding app URL inside project URLs

Simple Summary:
---------------
• urls.py is main route controller
• It maps URLs to views
• It connects apps to main project
• It controls website navigation

Practice Task:
--------------
1) Create Django project
2) Open project-level urls.py
3) Add path('home/', ...)
4) Create simple home view and print "Welcome"
5) Run server and test URL in browser
"""
