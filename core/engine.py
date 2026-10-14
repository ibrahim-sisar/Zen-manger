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

Todo:
-----
[ ] conect ui with engine to show data
[ ] bulid full templete white data from user 

Author:
-------
Ibrahim Said Abu Al-Roos (ibrahim.sisar@gmail.com)
Date: 24/4/2026

Last modified:
------------
Date: 14/10/2026
Time: 9:00 PM
"""
# --------------------[ libraries ]---------------------
import zenkit
from template_engine import *
import json
from pathlib import Path
# --------------------[ classes ]---------------------

def bulid_tree(nodes, crrent_path):                                                 #   _ _   _         _                   _ 
                                                                                    #  (_) | ( )       | |                 | |
    for node in nodes:                                                              #   _| |_|/ ___    | |__   __ _ _ __ __| |
      if node['type'] == 'file':                                                    #  | | __| / __|   | '_ \ / _` | '__/ _` |
        zenkit.create_file(node['name'], crrent_path, node['content'])              #  | | |_  \__ \   | | | | (_| | | | (_| |
                                                                                    #  |_|\__| |___/   |_| |_|\__,_|_|  \__,_|
      elif node['type'] == 'folder':                                                #
        zenkit.create_folder(node['name'],crrent_path)                              #
      else:                                                                         #
        print("no case")                                                            #
      new_path = Path(crrent_path) / Path(node['name'])                             #
      bulid_tree(node.get('children',[]),new_path)                                  #


if __name__ == "__main__":
  cache_templ()
  Path('s.json').write_text(json.dumps(load_template(get_template("c++-basic")['template_dir'])))