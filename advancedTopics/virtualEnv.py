"""
Python Virtual Environment (venv) Demonstration
================================================

This program explains:
1. What a virtual environment is
2. Why it is useful
3. Basic commands
4. Common usage workflow
5. Advantages of virtual environments

Author: Example Educational Script
"""

import sys
import os
import platform


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. Introduction
# ---------------------------------------------------------
print_header("WHAT IS A PYTHON VIRTUAL ENVIRONMENT?")

print("""
A Virtual Environment (venv) is an isolated Python environment.

It allows a project to:
✓ Have its own Python packages
✓ Avoid conflicts with other projects
✓ Maintain consistent dependencies

Without virtual environments:
- Project A may require Django 4.0
- Project B may require Django 5.0

Installing both globally can create version conflicts.

Virtual environments solve this problem.
""")


# ---------------------------------------------------------
# 2. Display Current Python Information
# ---------------------------------------------------------
print_header("CURRENT PYTHON INFORMATION")

print(f"Python Version : {sys.version}")
print(f"Python Executable : {sys.executable}")
print(f"Operating System : {platform.system()}")

# Check whether running inside a virtual environment
is_venv = sys.prefix != sys.base_prefix

print(f"\nRunning inside virtual environment? : {is_venv}")

if is_venv:
    print("Virtual Environment Path:", sys.prefix)
else:
    print("Currently using system/global Python.")


# ---------------------------------------------------------
# 3. Commands to Create a Virtual Environment
# ---------------------------------------------------------
print_header("HOW TO CREATE A VIRTUAL ENVIRONMENT")

print("""
Step 1: Open Terminal / Command Prompt

Step 2: Navigate to your project folder

Step 3: Create virtual environment

Windows:
    python -m venv myenv

Linux/Mac:
    python3 -m venv myenv

This creates a folder named 'myenv'
containing an isolated Python installation.
""")


# ---------------------------------------------------------
# 4. Activation Commands
# ---------------------------------------------------------
print_header("HOW TO ACTIVATE A VIRTUAL ENVIRONMENT")

print("""
Windows CMD:
    myenv\\Scripts\\activate

Windows PowerShell:
    .\\myenv\\Scripts\\Activate.ps1

Linux/Mac:
    source myenv/bin/activate

After activation, the terminal usually shows:

    (myenv)

indicating that the environment is active.
""")


# ---------------------------------------------------------
# 5. Package Installation Example
# ---------------------------------------------------------
print_header("INSTALLING PACKAGES")

print("""
After activation:

Install a package:
    pip install requests

Check installed packages:
    pip list

Show package information:
    pip show requests

Freeze dependencies:
    pip freeze > requirements.txt
""")


# ---------------------------------------------------------
# 6. requirements.txt Example
# ---------------------------------------------------------
print_header("REQUIREMENTS.TXT")

requirements_example = """
requests==2.32.0
numpy==2.0.0
pandas==2.2.0
"""

print("Example requirements.txt:\n")
print(requirements_example)

print("""
Install all dependencies:

    pip install -r requirements.txt
""")


# ---------------------------------------------------------
# 7. Deactivation
# ---------------------------------------------------------
print_header("DEACTIVATING THE ENVIRONMENT")

print("""
To leave the virtual environment:

    deactivate

This returns you to the system Python.
""")


# ---------------------------------------------------------
# 8. Advantages
# ---------------------------------------------------------
print_header("ADVANTAGES OF VIRTUAL ENVIRONMENTS")

advantages = [
    "Dependency isolation",
    "No package version conflicts",
    "Easy project deployment",
    "Reproducible environments",
    "Cleaner system Python installation",
    "Safer package experimentation",
    "Better collaboration among developers"
]

for i, advantage in enumerate(advantages, start=1):
    print(f"{i}. {advantage}")


# ---------------------------------------------------------
# 9. Common Project Workflow
# ---------------------------------------------------------
print_header("COMPLETE WORKFLOW")

print("""
1. Create project folder
       mkdir myproject

2. Move into folder
       cd myproject

3. Create virtual environment
       python -m venv venv

4. Activate environment
       source venv/bin/activate
       OR
       venv\\Scripts\\activate

5. Install packages
       pip install requests

6. Develop application

7. Save dependencies
       pip freeze > requirements.txt

8. Share project

9. Other users install dependencies
       pip install -r requirements.txt

10. Deactivate when done
       deactivate
""")


# ---------------------------------------------------------
# 10. Summary
# ---------------------------------------------------------
print_header("SUMMARY")

print("""
Virtual Environment (venv):
---------------------------
- Creates isolated Python environments.
- Prevents package conflicts.
- Allows different projects to use different versions.
- Makes projects portable and reproducible.

Key Commands:
-------------
Create:
    python -m venv myenv

Activate:
    myenv\\Scripts\\activate
    OR
    source myenv/bin/activate

Install Package:
    pip install package_name

Save Packages:
    pip freeze > requirements.txt

Deactivate:
    deactivate
""")

print("\nEnd of Demonstration.")