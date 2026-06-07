"""
ZEN - Utility Toolkit (Helpers)
===============================

Description:
------------
This module serves as the 'Helper Toolkit' for the Zen CLI. It encapsulates 
low-level system operations, providing a clean, platform-independent interface 
for filesystem manipulation, command execution, and environmental tasks. 
This keeps the core engine logic decoupled from specific OS calls.

Responsibilities:
-----------------
* System Abstraction: Wrapping Subprocess calls for cross-platform stability.
* Filesystem Helpers: Streamlining repetitive path and directory operations.
* Data Validation: Providing utility checks for file integrity and state.
* Error Handling: Standardizing how system-level errors are reported to the engine.

Technical Details:
------------------
* Module: core/utils.py
* Primary Classes: ZenUtils
* Dependencies: Subprocess, Os, Shutil, Pathlib.

Author:
-------
Ibrahim Said Abu Al-Roos (ibrahim.sisar@gmail.com)
Date: 07/06/2026

Last modified:
--------------
Date: 07/06/2026
Time: 10:40 AM
"""
# --------------------[ libraries ]---------------------
from pathlib import Path
impor
# --------------------[ classes ]---------------------
class ZenUtils:
  
    @staticmethod
    def create_dir(path):
      full_path = Path(path)
      full_path.mkdir(parents=True,exist_ok=True)
      
    @staticmethod
    def delete_dir(path):
      full_path = Path(path)
      if full_path.exists() and full_path.is_dir():
        full_path.rmdir()
        return True
      else: return False