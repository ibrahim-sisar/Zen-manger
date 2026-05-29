# --------------------[ Project Header & Docstring ]--------------------
"""
ZEN - Minimalist Project Manager CLI
====================================

Description:
------------
Zen is a specialized Command Line Interface (CLI) tool designed to streamline
the development workflow. It serves as a central hub for managing programming
projects (Django, Python, etc.) within a Linux environment, prioritizing
automation, organization, and a minimalist user experience.

Core Objectives:
----------------
* Lifecycle Management: Automate project creation, deletion, and listing.
* Scalability: Provide a modular framework for adding new project types and git-syncing.
* Aesthetics: Deliver a high-quality visual experience in the terminal using Rich.

Technical Architecture:
-----------------------
* Dev Environment: Linux (Debian-based)
* Language: Python 3.12.3
* UI Components: Rich (formatting), Questionary (interactive prompts), Pyfiglet (ASCII).
* Filesystem Ops: Pathlib (modern path handling), Shutil (advanced file operations).

Author:
-------
Ibrahim Said Abu Al-Roos (ibrahim.sisar@gmail.com)
Date: 17/4/2026

Last modified:
------------
Date: 22/4/2026
Time: 9:36 PM

Usage:
------
Run 'python zen.py' and follow the interactive prompts to manage your workspace.

Todo for me:
------------
[ ] Create the start menu and welcome screen.
[ ] Handle user errors.
[ ] Create the file structure for every type.
"""

# --------------------[ Libraries & Imports ]---------------------
from pathlib import Path
import shutil
import os
import questionary  # pyright: ignore[reportMissingImports]


# --------------------[ Classes & Logic ]---------------------
class ZenManager: 
    def __init__(self, BASE_DIR):
        self.base_dir = Path(BASE_DIR)

    # --------------------[ Helper Functions ]---------------------
    def _is_project_exists(self, project_name: str, project_type: str):
        full_path = self.base_dir / project_type / project_name
        return full_path.exists()

    # --------------------[ Main Functions ]---------------------
    def welcome_menu(self):
        
    
    def create_new_project(self):
        project_name = questionary.text("What is your project name?: ").ask()
        project_type = questionary.select(
            "Project type: ",
            choices=["django", "python", "frontend", "other"],
            style=questionary.Style(
                [
                    ("pointer", "fg:cyan bold"),
                    ("highlighted", "fg:cyan bold"),
                    ("selected", "fg:green"),
                ]
            ),
        ).ask()
        
        if self._is_project_exists(project_name, project_type):
            print("This name already exists")
        else:            
            new_project_folder = self.base_dir / project_type / project_name
            new_project_folder.mkdir(parents=True, exist_ok=True)


my_project = ZenManager("/mnt/C4DE4D4BDE4D36C8/ibrahim_project")
my_project.create_new_project()