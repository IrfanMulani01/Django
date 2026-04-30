"""
========================================
DJANGO GLOBAL INSTALLATION (WITHOUT VIRTUAL ENVIRONMENT)
========================================

Short Definition:
-----------------
• Global installation means installing Django directly on system Python
• It will be available for ALL projects on your computer
• You do NOT need virtual environment for global installation
• Beginners commonly use this method at start
"""

# --------------------------------------------------
# IMPORTANT NOTE
# --------------------------------------------------
"""
Global installation is easy but NOT recommended for big projects because:
• Version conflicts may happen
• Updating Django affects all projects
• Hard to manage multiple Django versions

Still useful for:
• Learning
• Small practice programs
"""

# --------------------------------------------------
# STEP 1 – CHECK PYTHON INSTALLED OR NOT
# --------------------------------------------------
"""
Type in Command Prompt:

python --version

If Python version appears → Python installed
If not → install Python first
"""

# --------------------------------------------------
# STEP 2 – UPGRADE PIP (RECOMMENDED)
# --------------------------------------------------
"""
Type:

python -m pip install --upgrade pip

This updates pip package manager.
"""

# --------------------------------------------------
# STEP 3 – INSTALL DJANGO GLOBALLY
# --------------------------------------------------
"""
Type:

pip install django

Django will be installed globally in system Python.
"""

# --------------------------------------------------
# STEP 4 – VERIFY DJANGO INSTALLATION
# --------------------------------------------------
"""
Type:

django-admin --version

You should see Django version number.
"""

# --------------------------------------------------
# WHERE DJANGO IS INSTALLED?
# --------------------------------------------------
"""
Django is installed in:
• System Python folder
• Accessible from any project
• No need to activate environment
"""

# --------------------------------------------------
# HOW TO CREATE PROJECT AFTER GLOBAL INSTALLATION
# --------------------------------------------------
"""
Type:

django-admin startproject myproject

Then open folder:

cd myproject

Run server:

python manage.py runserver
"""

# --------------------------------------------------
# UNINSTALLING GLOBALLY INSTALLED DJANGO
# --------------------------------------------------
"""
To remove Django from system completely:

pip uninstall django

Then press y

This removes Django globally.
"""

# --------------------------------------------------
# WHEN SHOULD YOU USE GLOBAL INSTALLATION?
# --------------------------------------------------
"""
Use global installation if:
• You are beginner
• You only learn Django basics
• You are not handling multiple projects
"""

# --------------------------------------------------
# WHEN SHOULD YOU AVOID GLOBAL INSTALLATION?
# --------------------------------------------------
"""
Avoid global installation if:
• You work on multiple projects
• You need different Django versions
• You collaborate in teams
• You deploy real-time projects

Then always use virtual environment.
"""

# --------------------------------------------------
# SIMPLE SUMMARY
# --------------------------------------------------
"""
1) Check Python version
2) Upgrade pip
3) Install Django globally
4) Verify installation
5) Create Django project
6) Run development server
7) Uninstall globally if needed
"""

# --------------------------------------------------
# PRACTICE SECTION
# --------------------------------------------------
"""
1. Install Django globally
2. Check installed version
3. Create project named: global_demo
4. Run server and observe output
5. Uninstall Django globally
"""
