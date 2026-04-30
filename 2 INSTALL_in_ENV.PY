"""
========================================
DJANGO INSTALLATION IN VIRTUAL ENVIRONMENT
========================================

Short Definition:
-----------------
• A virtual environment is a separate Python workspace
• It keeps project packages isolated from other projects
• We install Django inside a virtual environment
• This avoids version conflicts and errors
"""

# --------------------------------------------------
# WHAT IS VIRTUAL ENVIRONMENT? (Simple)
# --------------------------------------------------
"""
• It is like a separate box for each project
• Every project can have its own Django version
• Other projects do not get affected
"""

# --------------------------------------------------
# STEPS BEFORE INSTALLATION
# --------------------------------------------------
"""
Make sure you have:
• Python installed
• Command prompt / terminal access
• Internet connection
"""

# --------------------------------------------------
# STEP 1 – CREATE PROJECT FOLDER
# --------------------------------------------------
"""
Create a folder anywhere (Desktop recommended)

Example:
• Folder Name: django_projects
"""

# --------------------------------------------------
# STEP 2 – OPEN COMMAND PROMPT / TERMINAL
# --------------------------------------------------
"""
Open CMD inside the folder

Windows:
Right-click → Open in Terminal / Open PowerShell
"""

# --------------------------------------------------
# STEP 3 – CREATE VIRTUAL ENVIRONMENT
# --------------------------------------------------
"""
Type:

python -m venv env

Here:
• python → Python interpreter
• -m venv → module to create virtual environment
• env → virtual environment name (you can change)
"""

# --------------------------------------------------
# STEP 4 – ACTIVATE VIRTUAL ENVIRONMENT
# --------------------------------------------------
"""
Windows command:

env\Scripts\activate

After activation:
• You will see (env) before path
• Now Django will install only inside env
"""

# --------------------------------------------------
# STEP 5 – INSTALL DJANGO
# --------------------------------------------------
"""
Type:

pip install django

It will download and install Django package
inside your virtual environment only.
"""

# --------------------------------------------------
# STEP 6 – VERIFY DJANGO INSTALLED
# --------------------------------------------------
"""
Type:

django-admin --version

It will show installed Django version.
"""

# --------------------------------------------------
# STEP 7 – DEACTIVATE VIRTUAL ENVIRONMENT (WHEN DONE)
# --------------------------------------------------
"""
Type:

deactivate

This will exit virtual environment.
"""

# --------------------------------------------------
# UNINSTALLING DJANGO (IMPORTANT CONCEPT)
# --------------------------------------------------
"""
You may need to uninstall Django when:
• You installed wrong version
• You want to clean environment
• You are reinstalling Django

Make sure virtual environment is ACTIVATED first.
"""

# --------------------------------------------------
# STEP 1 – UNINSTALL DJANGO USING PIP
# --------------------------------------------------
"""
Type:

pip uninstall django

Then press: y

This removes Django from current virtual environment only.
"""

# --------------------------------------------------
# STEP 2 – CHECK DJANGO IS REMOVED OR NOT
# --------------------------------------------------
"""
Type:

python -m django --version

If uninstalled, it will show:

ModuleNotFoundError: No module named 'django'
"""

# --------------------------------------------------
# STEP 3 – REMOVE COMPLETE VIRTUAL ENVIRONMENT (OPTIONAL)
# --------------------------------------------------
"""
Just delete the virtual environment folder

Example:
• Delete folder: env

This removes Django and all packages inside it.
"""

# --------------------------------------------------
# SIMPLE SUMMARY
# --------------------------------------------------
"""
1) Create folder
2) Create virtual environment
3) Activate environment
4) Install Django
5) Check version
6) Deactivate when finished
7) Uninstall Django if needed
8) Or delete full virtual environment

Virtual environment keeps each project separate and safe.
"""

# --------------------------------------------------
# PRACTICE SECTION
# --------------------------------------------------
"""
1. Create a folder named django_practice
2. Create virtual environment inside it
3. Activate the environment
4. Install Django
5. Check Django version installed
6. Uninstall Django
7. Delete virtual environment folder
"""
