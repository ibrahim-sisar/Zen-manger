"""
ZEN - Project Logic Manager (Core)
==================================

Description:
------------
This module acts as the 'Brain' of the Zen CLI tool. It handles all backend 
operations including filesystem manipulation, directory structuring, and 
project lifecycle management. It is designed to be UI-agnostic, meaning it 
executes commands without direct interaction with the user terminal.

Responsibilities:
-----------------
* Filesystem Operations: Creating, deleting, and moving project folders.
* Config Parsing: Reading 'project_types.json' to determine structure.
* Validation: Checking project existence and path integrity.
* Scalability: Providing a generic engine to support any new project types 
  added via JSON configuration.

Technical Details:
------------------
* Module: core/manager.py
* Primary Classes: ZenManager
* Dependencies: Pathlib, Shutil, JSON.

Author:
-------
Ibrahim Said Abu Al-Roos (ibrahim.sisar@gmail.com)
Date: 24/4/2026

Last modified:
------------
Date: 24/4/2026
Time: 10:15 PM
"""
# --------------------[ libraries ]---------------------
# --------------------[ classes ]---------------------
