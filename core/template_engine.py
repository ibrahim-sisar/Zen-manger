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
* Dependencies: PyYAML, Jinja2, ZenKit (internal).

Author:
-------
Ibrahim Said Abu Al-Roos (ibrahim.sisar@gmail.com)
Date: 27/8/2026

Last modified:
------------
Date: 27/8/2026
Time: -
"""
# --------------------[ libraries ]---------------------
