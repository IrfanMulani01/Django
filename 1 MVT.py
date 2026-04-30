"""
========================================
MVT (MODEL–VIEW–TEMPLATE) – SIMPLE NOTES
========================================

MVT is a design pattern used in web development,
especially in Django.

It divides the program into three parts:
1) Model
2) View
3) Template

Purpose:
--------
To keep code clean, organized and easy to manage.
"""


# ---------------------------------------
# MODEL (Simple meaning)
# ---------------------------------------
          
"""
• Model works with the database
• It stores data
• It saves, updates, and deletes data
• It contains rules related to data

Example:
Student data, product data, user details etc.
"""

# ---------------------------------------
# VIEW (Simple meaning)
# ---------------------------------------
"""
• View receives user request
• It talks to the Model to get data
• It applies required logic
• It sends data to the Template

View = middleman between Model and Template
"""

# ---------------------------------------
# TEMPLATE (Simple meaning)
# ---------------------------------------
"""
• Template controls what user sees
• It displays data on webpage
• Uses HTML, CSS, JS, Bootstrap etc.
• No business logic inside Template

Template = only for design/UI
"""

# ---------------------------------------
# SIMPLE WORKING FLOW
# ---------------------------------------
"""
1. User sends request (clicks button, submits form)
2. View receives request
3. View asks Model for data
4. Model works with database
5. Model sends data to View
6. View sends data to Template
7. Template shows result to user
"""

# ---------------------------------------
# BENEFITS OF MVT
# ---------------------------------------
"""
• Easy to understand
• Clean and organized code
• Parts are separate:
   - Model → data
   - View → logic
   - Template → design
• Easy to change and maintain
• Many developers can work together
"""

# ---------------------------------------
# SMALL SUMMARY
# ---------------------------------------
"""
Model  = Data + Database
View   = Logic + Processing
Template = Design + Display

MVT helps build web apps fast, clean, and in a structured way.
"""
