"""
ZEN - Utility Toolkit (zenkit)
===============================

Description:
------------
This module serves as the 'Helper Toolkit' for the Zen Manager. It encapsulates
low-level system operations, providing a clean, platform-independent interface
for filesystem manipulation and environmental tasks.

This keeps the core engine logic decoupled from specific OS calls.

Responsibilities:
-----------------
* System Abstraction: Wrapping system-level operations.
* Filesystem Helpers: Streamlining repetitive path and directory operations.
* Data Validation: Providing utility checks for file and directory state.
* Error Handling: Standardizing how system-level errors are reported to the engine.

Technical Details:
------------------
* Module: core/zenkit.py
* Dependencies: Shutil, Pathlib, yaml, jinja2

Author:
-------
Ibrahim Said Abu Al-Roos (ibrahim.sisar@gmail.com)
Date: 07/06/2026

Last modified:
--------------
Date: 26/08/2026
"""

# --------------------[ Libraries ]---------------------
from pathlib import Path
from jinja2 import Template
import shutil
import yaml
# --------------------[ Tools ]---------------------

# ==================== Folder Operations ====================

def is_exists(path: str) -> bool:
    return Path(path).exists()


def create_folder(name: str, path: str) -> bool:
    folder = Path(path) / name
    folder.mkdir(parents=True, exist_ok=True)
    return is_exists(folder)


def delete_folder(path: str) -> bool:
    shutil.rmtree(path)
    return not is_exists(path)


def copy(source: str, destination: str) -> bool:
    shutil.copytree(source, destination, dirs_exist_ok=True)
    return is_exists(destination)


def move(source: str, destination: str) -> bool:
    shutil.move(source, destination)
    return is_exists(destination)


def is_dir(path: str) -> bool:
    return Path(path).is_dir()


# ==================== File Operations ====================

def create_file(name: str, directory: str, content=None) -> bool:
    file = Path(directory) / name
    file.touch()

    if content is not None:
        file.write_text(content)

    return is_exists(file)


def delete_file(path: str) -> bool:
    file = Path(path)
    file.unlink()
    return not is_exists(file)


def is_file(path: str) -> bool:
    return Path(path).is_file()

# ==================== yaml Operations ====================
def load_ymal(yaml_path:str) -> dict:
    path = Path(yaml_path)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))  
    return data

def create_ymal(path:str, name:str, data:dict) -> bool:
    out_path = Path(path) / name
    out_path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    
    return is_exists(out_path)

def update_ymal(path:str, data:dict) -> bool:
    Path(path).write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    return is_exists(path)


# ==================== Jinja2 Operations ====================
def render_text(text:str, data:dict) -> str:
    t = Template(text)
    return t.render(data)

# ==================== template Operations ====================
def load_template(path: str, data: dict) -> dict:
    file = Path(path)
    text = file.read_text(encoding="utf-8")
    rendered_text = render_text(text, data)
    return yaml.safe_load(rendered_text)