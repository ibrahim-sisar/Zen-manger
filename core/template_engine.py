"""
ZEN - Template Engine (Core)
==================================

Description:
------------
This module acts as the 'Brain' of ZEN's Template System. It handles all 
logic related to loading template definitions, exposing user prompts to 
the interface layer, resolving variables, evaluating conditions, and 
generating the final project structure. It is designed to be UI-agnostic, 
meaning it never interacts with the user directly — it only prepares data 
for the interface and executes generation once answers are provided.

Responsibilities:
-----------------
* Template Loading: Reading and parsing template definition files (YAML).
* Prompt Extraction: Exposing required user prompts (name_id, type, options) 
  without asking them itself.
* Variable Resolution: Rendering placeholders using Jinja2 based on 
  collected answers.
* Condition Handling: Evaluating if/else logic for tasks and file tree nodes.
* Structure Generation: Building the final folder/file tree via ZenKit.
* Task Execution: Running post-generation commands (e.g. django-admin, git init).

Technical Details:
------------------
* Module: core/template_engine.py
* Primary Classes: TemplateEngine, Template, Question, Task
* Dependencies: pathlib, json, ZenKit (internal).


Todo:
-----
[/] read template system
[/] list all template
[/] cash all template

Future Improvements:
--------------------
- Input Validation: Validate template data and required fields.
- Schema Validation: Enforce a consistent template structure.
- Error Handling: Provide clear, meaningful error messages.
- Cache Management: Detect stale or corrupted cache and rebuild it.
- Metadata Parsing: Define a consistent format for template metadata.
- Template Filtering: Filter supported file types and sort templates.
- Jinja2 Validation: Detect missing variables and template syntax errors.
- Task Execution Security: Validate commands before execution.
- Automated Testing: Cover edge cases, invalid inputs, and cache behavior.
-------------------------------------------------------------------------------
Author:
-------
Ibrahim Said Abu Al-Roos (ibrahim.sisar@gmail.com)
Date: 27/8/2026

Last modified:
------------
Date: 14/10/2026
Time: 8:00 pm
---------------------------------------------------------------------------------
"""
# --------------------[ libraries ]---------------------
import zenkit
from pathlib import Path
import json

# --------------------[ DIRS ]---------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT_DIR / "templates"
TEMPLATES_CACHE_DIR = TEMPLATES_DIR / "template_cache"
CACHE_FILE_PATH = TEMPLATES_CACHE_DIR / "template_cache.json"

# --------------------[ Template_func ]---------------------

def load_template(template_file:str) -> dict:
  data = zenkit.load_ymal(template_file)
  return {'questions':data["questions"], 'commands':data["tasks"], 'file_tree':data['file_tree']}

def list_template():
  data= zenkit.read_json(CACHE_FILE_PATH)
  return data

def get_template(template_name):
  data = list_template()
  for item in data:
    if item['template_name'].strip() == template_name:
      return item
  else:
      print("file not found", template_name)


def cache_templ():
  def read_first_two_lines(file_path):
      path = Path(file_path)
  
      with path.open("r") as file:
        lines = {}
        for _ in range(2):
            line = next(file, "")
            line = line.rstrip("\n")
            if ":" in line:
              key_value = line.split(":")
              
              lines[key_value[0]]= key_value[1]
              lines["template_dir"] = str(file_path)
        return lines
  
      
    
  temp_list = zenkit.list_files(TEMPLATES_DIR)
  config_data=[]
  for file in temp_list:
    config_data.append(read_first_two_lines(file))
  
  path = Path(CACHE_FILE_PATH)
  path.write_text(
    json.dumps(config_data, indent=4),
    encoding="utf-8"
  )

