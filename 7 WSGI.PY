"""
========================================
WSGI – Web Server Gateway Interface
========================================

What is wsgi.py?
----------------
• File used when Django project is deployed on web servers
• Helps communication between:
   ✔ Django application
   ✔ Web server (Apache, Nginx, Gunicorn etc.)

Simple Meaning:
---------------
• wsgi.py = connector between Django and web server

Where is it used?
-----------------
• Production deployment (live website)
• Traditional web requests (synchronous)

Main purpose:
-------------
• Loads Django project settings
• Exposes WSGI application object to web server

Important concept:
------------------
WSGI is for:
• normal request/response websites
• not for real-time apps
"""

"""
When is wsgi.py active?
-----------------------
• When your website is hosted online
• When using WSGI server like:
  ✔ Gunicorn
  ✔ uWSGI
  ✔ mod_wsgi

You usually NEVER edit this file in learning stage
"""
 